from flask import Flask, render_template, request
from flask import url_for
import sqlite3
import sqlalchemy
from datetime import datetime 

app  = Flask(__name__)

# index page route
@app.route("/")
def index():
    return render_template("index.html")


# app page route
@app.route("/app")
def m_app():
    return render_template("app.html")


# store page route
@app.route("/shop")
def shop():
    return render_template("shop.html")




if __name__ == "__main__":
    app.run(debug=True)
