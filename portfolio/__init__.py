"""
Initialization file for the portfolio app

Developed by Jerry Yu @ https://github.com/jeyu54217
------------------------------------------------
Developed for Coursework 2 of the CMT120 course at Cardiff University

Reference:
    1. flask_login: https://flask.palletsprojects.com/en/2.0.x/patterns/sqlalchemy/ 
"""
import sys
import os
from pathlib import Path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Include the parent directory of the current file's directory.
sys.path.append(str(Path(__file__).resolve().parent.parent))
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# LoginManager
login_manager = LoginManager()
login_manager.login_view = 'login'  # Tells Flask-Login where to redirect users who attempt to access restricted pages while not logged in.
login_manager.init_app(app)

if os.environ.get("ENV_TYPE") == "PROD":
    print("*** Now the app is on the PROD mode ***")
    print(f"*** The app is connected to MySQL server: {os.environ['MYSQL_DB_NAME']} on {os.environ['MYSQL_ADDRESS']} ***")
elif os.environ.get("ENV_TYPE") == "DEV":
    print("*** Now the app is on the DEV mode ***")
    print(f"*** The app is connected to {app.config['SQLALCHEMY_DATABASE_URI']} ***")
else:
    print("*** Now the app is on the LOCAL mode ***")
    print(f"*** The app is connected to {app.config['SQLALCHEMY_DATABASE_URI']} ***")
