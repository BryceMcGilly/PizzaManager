from flask import Flask
import os

from .routes import main
from .db import db

def create_app():
    app = Flask(__name__)

    uri = os.environ.get('DATABASE_URL')
    #Make URI compatible with Heroku
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)

    app.config['SQLALCHEMY_DATABASE_URI'] = uri
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    db.init_app(app)
    app.register_blueprint(main)
    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run()