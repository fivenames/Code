import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    id = session.get("user_id")

    stocks = db.execute("SELECT * FROM stocks WHERE user_id = ?", id)
    cash = db.execute("SELECT cash FROM users WHERE id = ?", id)

    cash = cash[0]['cash']
    cash = round(cash, 2)
    cash = "{:.2f}".format(cash)
    return render_template("index.html", stocks=stocks, cash=cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")

    elif request.method == "POST":
        symbol = request.form.get("symbol")
        symbol = symbol.upper()

        price = lookup(symbol)
        if not price:
            return apology("Invaild stock symbol")

        share = request.form.get("share")
        if not share:
            return apology("Invaild input of shares")

        try:
            share = int(share)
        except ValueError:
            return apology("Invaild input of shares")

        if share <= 0:
            return apology("Invalid input of shares")

        price = price["price"]
        amount = price * share

        id = session.get('user_id')

        balance = db.execute("SELECT cash FROM users WHERE id = ?", id)
        balance = balance[0]["cash"]

        if balance - amount < 0:
            return apology("Insufficient balance to buy stock")

        balance -= amount
        # Update remaining balance
        db.execute("UPDATE users SET cash = ? WHERE id = ?", balance, id)

        # Update stock held
        stocks = db.execute("SELECT symbol FROM stocks WHERE user_id = ?", id)
        symbols = list(map(lambda x: x['symbol'], stocks))
        if symbol in symbols:
            held = db.execute("SELECT shares FROM stocks WHERE user_id = ? AND symbol = ?", id, symbol)

            new_share = share + held[0]['shares']
            db.execute("UPDATE stocks SET shares = ? WHERE user_id = ? AND symbol = ?", new_share, id, symbol)
        else:
            db.execute("INSERT INTO stocks (user_id, symbol, shares) VALUES (?, ?, ?)", id, symbol, share)

        # Update transaction history
        typ = "Bought"
        amount = -amount
        amount = round(amount, 2)
        db.execute("INSERT INTO history (type, symbol, shares, user_id, amount) VALUES (?, ?, ?, ?, ?)", typ, symbol, share, id, amount)

        return redirect("/")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    id = session.get("user_id")

    transactions = db.execute("SELECT * FROM history WHERE user_id = ?", id)
    cash = db.execute("SELECT cash FROM users WHERE id = ?", id)

    cash = cash[0]['cash']
    cash = round(cash, 2)
    cash = "{:.2f}".format(cash)
    return render_template("history.html", transactions=transactions, cash=cash)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")

    elif request.method == "POST":
        quote = request.form.get("quote")

        if not quote:
            return apology("Empty quote")

        quote = quote.upper()
        stock_info = lookup(quote)
        if not stock_info:
            return apology("Invalid stock symbol")

        return render_template("quote_info.html", stock=stock_info)

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "GET":
        return render_template("register.html")

    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        recheck = request.form.get("confirm_password")

        if not username or not password or not recheck:
            return apology("Fill in all required fields")

        if password != recheck:
            return apology("Passwords entered do not match")

        username_check = db.execute("SELECT username FROM users WHERE username = ?", username)
        if username_check:
            return apology("Username already taken!")

        password = generate_password_hash(password)
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, password)

        id = db.execute("SELECT id FROM users WHERE username = ?", username)
        session["user_id"] = id[0]['id']
        return redirect("/")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        id = session.get('user_id')
        stocks = db.execute("SELECT * FROM stocks WHERE user_id = ?", id)
        return render_template("sell.html", stocks=stocks)

    if request.method == "POST":
        symbol = request.form.get("symbol")
        price = lookup(symbol)
        share = request.form.get("share")

        if not share:
            return apology("Invaild input of shares")

        try:
            share = int(share)
        except ValueError:
            return apology("Invaild input of shares")

        if share <= 0:
            return apology("Invalid input of shares")

        id = session.get('user_id')

        balance = db.execute("SELECT shares FROM stocks WHERE user_id = ? AND symbol = ?", id, symbol)
        balance = balance[0]["shares"]

        if balance - share < 0:
            return apology("Insufficient shares balance")

        balance -= share

        price = price["price"]
        amount = price * share

        cash = db.execute("SELECT cash FROM users WHERE id = ?", id)
        cash = cash[0]['cash']
        cash += amount

        # Update stock held
        if balance > 0:
            db.execute("UPDATE stocks SET shares = ? WHERE user_id = ? AND symbol = ?", balance, id, symbol)
        elif balance == 0:
            db.execute("DELETE FROM stocks WHERE user_id = ? AND symbol = ?", id, symbol)

        # Update remaining balance
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, id)

        # Update transaction history
        typ = "Sold"
        amount = round(amount, 2)
        db.execute("INSERT INTO history (type, symbol, shares, user_id, amount) VALUES (?, ?, ?, ?, ?)", typ, symbol, share, id, amount)

        return redirect("/")
