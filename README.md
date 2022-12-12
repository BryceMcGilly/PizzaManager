# PizzaManager

To build locally:

Install python.

Create a virtual environment with:
python -m venv venv

Activate the virtual environment with:  venv\Scripts\Activate

run:
pip install flask

run:
pip install flask-sqlalchemy

run:
pip install python-dotenv

create a .env file in the root directory that contains:

DATABASE_URL=sqlite:///pizzas.sqlite3

SECRET_KEY=makeupakey

create a .flaskenv in the root directory that contains:

FLASK_APP=pizzamanager

To run application:  flask run



User Stories:

Manage Toppings

As a pizza store owner I should be able to manage toppings available for my pizza chefs.

It should allow me to see a list of available toppings

It should allow me to add a new topping

It should allow me to delete an existing topping

It should allow me to update an existing topping

It should not allow me to enter duplicate toppings



Manage Pizzas

As a pizza chef I should be able to create new pizza master pieces.

It should allow me to see a list of existing pizzas and their toppings

It should allow me to create a new pizza and add toppings to it

It should allow me to delete an existing pizza

It should allow me to update an existing pizza

It should allow me to update toppings on an existing pizza

It should not allow me to enter duplicate pizzas
