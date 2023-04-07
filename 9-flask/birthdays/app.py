import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# While storing the data in a global variable works, but everytime the server stops(be it proactively or due to system crash or power failiure), the memory is cleared.
# To safely store data, databases and sqlite can be used.
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# A second param: methods=['POST', 'GET'] (with only post or get works as well) can be passed to the decorator, it indicates that the route will handle both POST and GET request.
# Using only one route, the default request to server is always GET; eg. going to the URL www.domain.com/ sends a GET request to the server requesting to access the data.
# POST request is made only when a form is submitted or something similar.
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # For POST, use requests.form.get() instead to retrieve the intended data.
        name = request.form.get('name')
        month = request.form.get('month')
        day = request.form.get('day')

        if name and month and day:
            db.execute("INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?);", name, month, day)

        return redirect("/")

    else:

        birthdays = db.execute("SELECT name, month, day FROM birthdays;")

        return render_template("index.html", birthdays=birthdays)
