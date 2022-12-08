from flask import Blueprint, request, url_for, redirect, render_template, flash

from .models import Topping, Pizza
from .db import db

main = Blueprint('main', __name__)

@main.route('/')
def home():
    pass

    return redirect(url_for('main.manage_pizzas'))

@main.route('/manage_pizzas')
def manage_pizzas():
    pizzas = Pizza.query.all()
    flash("Click the Update button to modify an existing pizza or Delete to remove it.")

    return render_template('manage_pizzas.html', pizzas=pizzas)

@main.route('/delete_pizza/<int:pizza_id>', methods=['POST'])
def delete_pizza(pizza_id):
    pizza = Pizza.query.get_or_404(pizza_id)
    db.session.delete(pizza)
    db.session.commit()
    flash(pizza.name + " has been removed.")

    return redirect(url_for('main.manage_pizzas'))

@main.route('/edit_pizza/<int:pizza_id>', methods=['POST'])
def edit_pizza(pizza_id):
    pizza = Pizza.query.get_or_404(pizza_id)
    pizzas = Pizza.query.all()
    toppings = Topping.query.all()
    pizza_toppings = pizza.toppings
    flash("Modify the name or toppings of " + pizza.name + " and click Create Pizza to save your changes.")

    return render_template('create_pizza.html', pizzas=pizzas, pizza=pizza, toppings=toppings, pizza_toppings=pizza_toppings)

@main.route('/create_pizza')
def create_pizza():
    pizzas = Pizza.query.all()
    toppings = Topping.query.all()
    flash("Type a name for your new pizza, select the toppings you want on it and click Create Pizza to save it.")

    return render_template('create_pizza.html', pizzas=pizzas, pizza=None, toppings=toppings)

@main.route('/create_pizza', methods=['POST'])
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

            #Author: Bryce McGilly

    elif pizza_name:
        new_pizza = Pizza(name=pizza_name)

        for topping_id in pizza_topping_ids:
            new_pizza.toppings.append(Topping.query.get_or_404(topping_id))

        db.session.add(new_pizza)

    try:
        if pizza_name:
            db.session.commit()
            flash(pizza_name + " created or modified!")
        else:
            flash("Not able to save pizza, name is blank.")
    except:
        flash("Not able to save pizza, does " + pizza_name + " already exist?")

    return redirect(url_for('main.manage_pizzas'))

@main.route('/manage_toppings')
def manage_toppings():
    toppings = Topping.query.all()
    flash("Enter a topping name and click Add to save it.")
    flash("Click Update to modify or Delete to remove an existing topping.")

    return render_template('manage_toppings.html', toppings=toppings, topping=None)

@main.route('/manage_toppings', methods=['POST'])
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
        if topping_name:
            db.session.commit()
            flash(topping_name + " created or modified!")
        else:
            flash("Not able to save topping, name is blank.")
    except:
        flash("Not able to save topping, does " + topping_name + " already exist?")

    return redirect(url_for('main.manage_toppings'))

@main.route('/delete_topping/<int:topping_id>', methods=['POST'])
def delete_topping(topping_id):
    topping = Topping.query.get_or_404(topping_id)
    db.session.delete(topping)
    db.session.commit()
    flash(topping.name + " has been removed.")

    return redirect(url_for('main.manage_toppings'))

@main.route('/edit_topping/<int:topping_id>', methods=['POST'])
def edit_topping(topping_id):
    topping = Topping.query.get_or_404(topping_id)
    toppings = Topping.query.all()
    flash("Modify the name of the topping " + topping.name + " and click Add to save your changes.")

    return render_template('manage_toppings.html', toppings=toppings, topping=topping)