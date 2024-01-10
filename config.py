"""
Config Script - Loaded upon app initialization

Developed by Selman Tabet @ https://selman.io/
------------------------------------------------
Developed for Coursework 2 of the CMT120 course at Cardiff University

Based on a config script that I developed during my time as the architect
of the Shopify Integration Gateway for Snoonu Qatar's Fleet Management System (FalconFlex)
"""
from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.absolute() # /Cardiff_2324_CMT120_Flask
ENV_PATH = BASE_DIR / ".env"

try:
    if ENV_PATH.exists():
        load_dotenv(dotenv_path = ENV_PATH)
        print("*** env vars initialized from config file successfully! ***")
    else:
        raise FileNotFoundError("No .env file detected. Using environment variables instead.")
except Exception as e:
    print(f"*** Error while loading .env file: {e} *** ")
    
class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Suppresses SQLAlchemy warnings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'FOR_TEST_64c81e139e3c113ecf8393abeaf83028196ca82e2acf2a3a'
    
    # PROD Mode
    if os.environ.get("ENV_TYPE") == "PROD":
        print("*** PROD deployment detected ***")
        try:
            DB_USER = os.environ["MYSQL_USER"]
            DB_PSW = os.environ["MYSQL_PASSWORD"]
            DB_HOST = os.environ["MYSQL_ADDRESS"]
            DB_NAME = os.environ["MYSQL_DB_NAME"]
            SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PSW}@{DB_HOST}/{DB_NAME}'
        except Exception as e:
            print(f"*** Error while loading DB env vars in OpenShift PROD Deployment Mode: {e} *** ")
    
    # Dev Mode
    elif os.environ.get("ENV_TYPE") == "DEV":
        print("*** DEV deployment detected ***")
        try:
            DB_USER = os.environ["MYSQL_USER"]
            DB_PSW = os.environ["MYSQL_PASSWORD"]
            DB_HOST = os.environ["MYSQL_ADDRESS"]
            DB_NAME = os.environ["MYSQL_DB_NAME"]
            SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PSW}@{DB_HOST}/{DB_NAME}'
        except Exception as e:
            print(f"*** Error while loading DB env vars in Local DEV Mode: {e} *** ")
    # Local Mode
    else:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(BASE_DIR / 'portfolio_dev.db')

        

