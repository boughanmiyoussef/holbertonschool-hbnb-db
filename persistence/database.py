#!/usr/bin/python3
import os
from model.base import Base
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)

config_class = 'config.DevelopmentConfig' if os.getenv('ENV') == 'development' else 'config.ProductionConfig'
app.config.from_object(config_class)

try:
    app.config.from_object(config_class)
except ImportError as e:
    raise ImportError(f"Could not import '{config_class}': {e}")

db = SQLAlchemy(app)

@app.teardown_appcontext
def remove_session(exception=None):
    db.session.remove()

with app.app_context():
    db.create_all()