from flask import Flask, request, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizzas.sqlite3'
app.config['SECRET_KEY'] = "1234567890"

db = SQLAlchemy(app)

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

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    pass

    return redirect(url_for('manage_pizzas'))

@app.route('/manage_pizzas')
def manage_pizzas():
    pizzas = Pizza.query.all()

    return render_template('manage_pizzas.html', pizzas=pizzas)

@app.route('/delete_pizza/<int:pizza_id>', methods=['POST'])
def delete_pizza(pizza_id):
    pizza = Pizza.query.get_or_404(pizza_id)
    db.session.delete(pizza)
    db.session.commit()

    return redirect(url_for('manage_pizzas'))

@app.route('/edit_pizza/<int:pizza_id>', methods=['POST'])
def edit_pizza(pizza_id):
    pizza = Pizza.query.get_or_404(pizza_id)
    pizzas = Pizza.query.all()
    toppings = Topping.query.all()
    pizza_toppings = pizza.toppings

    return render_template('create_pizza.html', pizzas=pizzas, pizza=pizza, toppings=toppings, pizza_toppings=pizza_toppings)

@app.route('/create_pizza')
def create_pizza():
    pizzas = Pizza.query.all()
    toppings = Topping.query.all()

    return render_template('create_pizza.html', pizzas=pizzas, pizza=None, toppings=toppings)

@app.route('/create_pizza', methods=['POST'])
def create_pizza_post():
    pizza_name = request.form.get('pizza-name')
    pizza_id = request.form.get('pizza-id')
    pizza_topping_ids = request.form.getlist('pizza-topping-ids')

    if pizza_id and pizza_name:
        pizza = Pizza.query.get_or_404(pizza_id)
        pizza.name = pizza_name

        for topping in Topping.query.all():
            #if topping is no longer selected remove topping
            if not(str(topping.id) in pizza_topping_ids) and (topping in pizza.toppings):
                pizza.toppings.remove(topping)
                
            #if toppping is newly selected add topping
            elif (str(topping.id) in pizza_topping_ids) and not(topping in pizza.toppings):
                pizza.toppings.append(topping)

    elif pizza_name:
        new_pizza = Pizza(
            name=pizza_name
        )

        for topping_id in pizza_topping_ids:
            new_pizza.toppings.append(
                Topping.query.get_or_404(topping_id)
            )

        db.session.add(new_pizza)

    try:
        db.session.commit()
    except:
        print("Not able to commit() database probably due to duplicate Pizza Name: " + pizza_name)

    return redirect(url_for('manage_pizzas'))

@app.route('/manage_toppings')
def manage_toppings():
    toppings = Topping.query.all()

    return render_template('manage_toppings.html', toppings=toppings, topping=None)

@app.route('/manage_toppings', methods=['POST'])
def manage_toppings_post():
    topping_name = request.form.get('topping-name')
    topping_id = request.form.get('topping-id')

    if topping_id and topping_name:
        topping = Topping.query.get_or_404(topping_id)
        topping.name = topping_name

    elif topping_name:
        new_topping = Topping(
            name=topping_name
        )

        db.session.add(new_topping)

    try:
        db.session.commit()
    except:
        print("Not able to commit() database probably due to duplicate Topping Name: " + topping_name)

    return redirect(url_for('manage_toppings'))

@app.route('/delete_topping/<int:topping_id>', methods=['POST'])
def delete_topping(topping_id):
    topping = Topping.query.get_or_404(topping_id)
    db.session.delete(topping)
    db.session.commit()

    return redirect(url_for('manage_toppings'))

@app.route('/edit_topping/<int:topping_id>', methods=['POST'])
def edit_topping(topping_id):
    topping = Topping.query.get_or_404(topping_id)
    toppings = Topping.query.all()

    return render_template('manage_toppings.html', toppings=toppings, topping=topping)