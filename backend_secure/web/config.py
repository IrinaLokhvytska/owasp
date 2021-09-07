""" Set up flask configuration """
import os

from datetime import timedelta


# App conf
FLASK_APP = os.environ['FLASK_APP_OWASP']
FLASK_ENV = os.environ['FLASK_ENV_OWASP']
SECRET_KEY = os.environ['SECRET_KEY_OWASP']
PERMANENT_SESSION_LIFETIME = timedelta(minutes=15)

# DB conf
POSTGRES_USER = os.environ['POSTGRES_USER_OWASP']
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD_OWASP']
POSTGRES_HOST = os.environ['POSTGRES_HOST_OWASP']
POSTGRES_PORT = os.environ['POSTGRES_PORT_OWASP']
POSTGRES_DB = os.environ['POSTGRES_DB_OWASP']
SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'

# postgresql+psycopg2://owasp_user:LmYCWUWWyGQxfIZ@backend_secure_db:5433/backend_secure_db
INIT_DB = int(os.environ['INIT_DB_OWASP'])
SQLALCHEMY_TRACK_MODIFICATIONS = False
