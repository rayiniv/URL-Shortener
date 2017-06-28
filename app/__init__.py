# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()

app = Flask(__name__, instance_relative_config=True)

from app import views
from app import models

app.config.from_object('config')