"""Set up flask configuration"""
import os

# App conf
FLASK_APP = os.environ['FLASK_APP']
FLASK_ENV = os.environ['FLASK_ENV']
SECRET_KEY = os.environ['SECRET_KEY']

# DB conf
POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
POSTGRES_HOST = os.environ['POSTGRES_HOST']
POSTGRES_PORT = os.environ['POSTGRES_PORT']
POSTGRES_DB = os.environ['POSTGRES_DB']
SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
INIT_DB = int(os.environ['INIT_DB'])
SQLALCHEMY_TRACK_MODIFICATIONS = False
