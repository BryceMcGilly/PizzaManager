from .db import db

pizza_topping = db.Table('pizza_topping',
    db.Column('topping_id', db.Integer, db.ForeignKey('topping.id')),
    db.Column('pizza_id', db.Integer, db.ForeignKey('pizza.id'))
)

class Topping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    toppings = db.relationship('Topping', secondary=pizza_topping, lazy='dynamic')
