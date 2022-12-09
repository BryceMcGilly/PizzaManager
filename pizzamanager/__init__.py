from flask import Flask
import os
from dotenv import load_dotenv

from .routes import main
from .db import db

def create_app():
    app = Flask(__name__)

    load_dotenv()

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('HEROKU_POSTGRESQL_OLIVE_URL')
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    db.init_app(app)
    app.register_blueprint(main)
    with app.app_context():
        db.create_all()

    return app