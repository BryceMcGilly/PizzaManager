import os
from dotenv import load_dotenv

load_dotenv('.env')

uri = os.environ.get('HEROKU_POSTGRESQL_OLIVE_URL')
#Make URI compatible with Heroku
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

SQLALCHEMY_DATABASE_URI = uri
SECRET_KEY = os.environ.get('SECRET_KEY')