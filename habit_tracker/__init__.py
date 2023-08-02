# __init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from flask_migrate import Migrate
from flask_session import Session
from .config import Config, TestConfig

# Load the environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Use the appropriate config based on whether we're testing or not.
if os.getenv('FLASK_ENV') == 'test':
    app.config.from_object(TestConfig)
else:
    app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Configure Flask-Session
Session(app)

# Import and register main routes
from .routes import *
from .auth import *

# import classes from models.py
from .models import *

with app.app_context():
    db.create_all()
