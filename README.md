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
