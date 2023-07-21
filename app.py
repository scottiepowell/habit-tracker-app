# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from flask_migrate import Migrate
from flask_session import Session

# Load the environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # or 'mysql://user:password@localhost/dbname'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'site.db')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Configure Flask-Session
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Import and register main routes
from routes import *
from auth import *
# import classes from models.py
from models import *

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)