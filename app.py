from flask import Flask, render_template, request
from flask import url_for, redirect
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

app  = Flask(__name__)

# database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db = SQLAlchemy(app)

# database models
class ContactForm(db.Model):
    __tablename__ = 'contact_form'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    message = db.Column(db.String, nullable=False)

class Ebook(db.Model):
    __tablename__ = 'EBOOKS'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    price = db.Column(db.String, nullable=False)
    image_path = db.Column(db.String, nullable=False)

class PepperSpray(db.Model):
    __tablename__ = 'PEPPERSPRAY'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    price = db.Column(db.String, nullable=False)
    image_path = db.Column(db.String, nullable=False)

class StunDevice(db.Model):
    __tablename__ = 'STUNDEVICES'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    price = db.Column(db.String, nullable=False)
    image_path = db.Column(db.String, nullable=False)

class Wearable(db.Model):
    __tablename__ = 'WEARABLES'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    price = db.Column(db.String, nullable=False)
    image_path = db.Column(db.String, nullable=False)


# index page route
@app.route("/", methods=["POST", "GET"] )
def index():
    return render_template("index.html")


# app page route
@app.route("/app")
def m_app():
    return render_template("app.html")


# store page route
@app.route("/shop", methods=["GET"])
def shop():
    return render_template("shop.html")




if __name__ == "__main__":
    app.run(debug=True)
