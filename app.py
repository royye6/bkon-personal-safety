from flask import Flask, render_template, request, jsonify
from flask import url_for, redirect
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from datetime import datetime

app  = Flask(__name__)

class Base(DeclarativeBase):
    pass

# database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db = SQLAlchemy(model_class=Base)

db.init_app(app)

# database models
class ContactForm(db.Model):
    __tablename__ = 'contact_form'

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String, nullable=False)
    email: Mapped[str] = mapped_column(db.String, unique=True, nullable=False)
    message = db.Column(db.String(500), nullable=False)


class Ebook(db.Model):
    __tablename__ = 'ebooks'

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    title: Mapped[str] = mapped_column(db.String, nullable=False)
    price: Mapped[str] = mapped_column(db.String, nullable=False)
    image_path: Mapped[str] = mapped_column(db.String, nullable=False)

    def __repr__(self) -> str:
        return f"<Ebook('{self.id}', '{self.title}', '{self.price}', '{self.image_path}>)"
    

class PepperSpray(db.Model):
    __tablename__ = 'pepperspray'

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    title: Mapped[str] = mapped_column(db.String, nullable=False)
    price: Mapped[str] = mapped_column(db.String, nullable=False)
    image_path: Mapped[str] = mapped_column(db.String, nullable=False)

    def __repr__(self) -> str:
        return f"<PepperSpray('{self.id}', '{self.title}', '{self.price}', '{self.image_path}>)"
    

class StunDevice(db.Model):
    __tablename__ = 'stundevices'

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    title: Mapped[str] = mapped_column(db.String, nullable=False)
    price: Mapped[str] = mapped_column(db.String, nullable=False)
    image_path: Mapped[str] = mapped_column(db.String, nullable=False)

    def __repr__(self) -> str:
        return f"<StunDevice('{self.id}', '{self.title}', '{self.price}', '{self.image_path}>)"
    

class Wearable(db.Model):
    __tablename__ = 'wearables'

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    title: Mapped[str] = mapped_column(db.String, nullable=False)
    price: Mapped[str] = mapped_column(db.String, nullable=False)
    image_path: Mapped[str] = mapped_column(db.String, nullable=False)

    def __repr__(self) -> str:
        return f"<Wearable('{self.id}', '{self.title}', '{self.price}', '{self.image_path}>)"


class Review(db.Model):
    __tablename__ = 'reviews'

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String, nullable=False)
    comment: Mapped[str] = mapped_column(db.String, nullable=False)
    dp: Mapped[str] = mapped_column(db.String, nullable=False)

    def __str__(self):
        return f"Review('{self.id}', '{self.name}', '{self.comment}', '{self.dp}')"


# index page route
@app.route("/", methods=['POST', 'GET']) 
def index():
    if request.method == 'POST':
        return handle_message()
    return render_template("index.html")


@app.route("/message", methods=['POST', 'GET'])
def handle_message():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    if name != '' and email != '' and message != '':
        new_message = ContactForm(name=name, email=email, message=message)
        db.session.add(new_message)
        db.session.commit()
        print('Message was sent successfully!')
        return jsonify({'success': True})
        # return redirect('/')
    else:
        return jsonify({'success': False, 'error': 'Please fill in all the required fields'})  
        # return redirect('/')


# app page route
@app.route("/app", methods=['POST', 'GET'])
def m_app():
    reviews = db.session.execute(db.select(Review).order_by(Review.id)).scalars()
    return render_template("app.html", reviews=reviews)


# store page route
@app.route("/shop", methods=['GET'])
def shop():
    ebooks = db.session.execute(db.select(Ebook).order_by(Ebook.id)).scalars()
    pepperspray = db.session.execute(db.select(PepperSpray).order_by(PepperSpray.id)).scalars()
    stundevices = db.session.execute(db.select(StunDevice).order_by(StunDevice.id)).scalars()
    wearables = db.session.execute(db.select(Wearable).order_by(Wearable.id)).scalars()
    return render_template("shop.html", ebooks=ebooks, pepperspray=pepperspray, 
                           stundevices=stundevices, wearables=wearables)




if __name__ == "__main__":
    app.run(debug=True)
