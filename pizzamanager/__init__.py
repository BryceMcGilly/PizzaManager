from flask import Flask
import os

from .routes import main
#from .db import db

def create_app():
    app = Flask(__name__)

    #app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('HEROKU_POSTGRESQL_OLIVE_URL')
    #print("DB: " + app.config.get('SQLALCHEMY_DATABASE_URI'))
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    print("Secret: " + app.config.get('SECRET_KEY'))

    #db.init_app(app)
    app.register_blueprint(main)
    #with app.app_context():
    #    db.create_all()

    return app