import os
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s

    # Return apology.html after escaping special characters.
    return render_template("apology.html", top=code, bottom=escape(message)), code

# This defines a decorator, used to decorate a function. Everytime time the decorated function is called, this function is called instead. It takes in the function it decorates;
def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    # @wraps decorator is used to preserve the original function's name and documentation.
    @wraps(f)
    # Check if session exist, if not, redirect, if yes, carry on with the original function
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        # Calling the original function with all of the arguments.
        return f(*args, **kwargs)

    # The login_required function returns a function that check for a condition before the decorated funtion is called. Essentially taking in a function and returning a function.
    return decorated_function


def lookup(symbol):
    """Look up quote for symbol."""

    # Contact API
    try:
        api_key = os.environ.get("API_KEY")
        url = f"https://cloud.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/quote?token={api_key}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        quote = response.json()
        return {
            "name": quote["companyName"],
            "price": float(quote["latestPrice"]),
            "symbol": quote["symbol"]
        }
    except (KeyError, TypeError, ValueError):
        return None


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"



# export API_KEY=pk_7ad779c133d54be4ae045627c0bbf17e