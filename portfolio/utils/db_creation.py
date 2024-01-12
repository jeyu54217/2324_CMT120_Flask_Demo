"""
Database Test Data Creation Script

Developed by Jerry Yu @ https://github.com/jeyu54217
------------------------------------------------
Developed for Coursework 2 of the CMT120 course at Cardiff University

This script is designed to generate test data for the database.
"""
import time
import datetime
from dotenv import load_dotenv

# Include the parent directory of the current file's directory.
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from portfolio import app, db
from portfolio.models import User, Education, Experience #, Msg_board


def load_env_vars():
    """
    Initializes the environment variables from the .env file.
    """
    try:
        base_dir = Path(__file__).resolve().parent.parent.parent.absolute() # /Cardiff_2324_CMT120_Flask
        env_path = base_dir / ".env"
        if env_path.exists():
            load_dotenv(dotenv_path = env_path)
            print("*** env vars initialized in db_creation_dev file successfully! ***")
        else:
            raise FileNotFoundError("No .env file detected. Using environment variables instead.")
    except Exception as e:
        print(f"*** Error while loading .env in db_creation_dev : {e} *** ")  
              
def create_db():
    try:
        input(" Press Enter to create the database...")
        db.create_all()
        print("*** Database created! ***")
    except Exception as e:
        print(f"*** Error when creating database: {e} ***")
        
def create_admin_user():
    """
    Creates an admin user if it doesn't already exist in the database.
    The admin user is assigned the name "admin" and a default password.
    """
    try:
        admin_user = User.query.filter_by(name="admin").first()
        if admin_user is None:
            admin_user = User(name="admin")
            admin_user.set_password("123")
            db.session.add(admin_user)
            db.session.commit()
            print("*** Admin user created! ***")
        else:
            print("*** Admin user already exists! ***")
    except Exception as e:
        print(f"*** Error when creating admin user: {e} ***")
        
def create_edu():
    """
    Creates test education data and adds it to the database.

    This function creates two instances of the Education class with example data,
    and adds them to the database session. It then commits the changes to the database.
    """
    try:
        test_edu_1 = Education(
            start_date = "2009-09",
            end_date = "2013-06",
            school = "Thung Hai University, Taiwan",
            degree = "Bachelor of Arts",
            description = "This is an example education in Thung Hei University",
            user_id = 1,
        )
        test_edu_2 = Education(
            start_date = "2023-09-01",
            end_date = "2024-06-01",
            school = "Cardiff University, UK",
            degree = "Master of Science",
            description = "This is an example education in Cardiff University",
            user_id = 1,
        )
        for i in (test_edu_1, test_edu_2):
            db.session.add(i)
            time.sleep(0.2)
        db.session.commit()
        print("*** test edu data created! ***")
    except Exception as e:
        print(f"*** Error when creating test edu data: {e} ***")
        
def create_exp():
    """
    Creates test experience data and adds it to the database.

    This function creates two instances of the Experience class with predefined values
    and adds them to the database session. It then commits the changes to the database.
    """
    try:
        test_exp_1 = Experience(
            start_date="2021-02-01",
            end_date="2022-03-01",
            company="FUCO",
            position="Assistant Software Engineer",
            description="This is an example experience in FUCO",
            user_id=1,
        )
        test_exp_2 = Experience(
            start_date="2022-03",
            end_date="2023-05",
            company="CTBC BANK",
            position="Data Engineer",
            description="This is an example experience in CTBC BANK",
            user_id=1,
        )

        for i in (test_exp_1, test_exp_2):
            db.session.add(i)
            time.sleep(0.2)
        db.session.commit()
        print("*** test exp data created! ***")
    except Exception as e:
        print(f"*** Error when creating test exp data: {e} ***")
    
def create_msg():
    """
    Creates test message data and adds it to the database.

    This function creates two test messages with predefined values for name, title, content, create_date, and user_id.
    It adds the test messages to the database session and commits the changes.
    """
    try:
        test_msg_1 = Msg_board(
            name="Amy",
            title="Where are you from?",
            content="Hi there, I am Amy. Where are you from?",
            create_date=datetime.datetime.now(),
            user_id=1,
        )
        test_msg_2 = Msg_board(
            name="Bob",
            title="What's your hobby?",
            content="Hi there, I am Bob. I like playing basketball. What's your hobby?",
            create_date=datetime.datetime.now(),
            user_id=1,
        )
        for i in (test_msg_1, test_msg_2):
            db.session.add(i)
            time.sleep(0.2)
        db.session.commit()
        print("*** test msg data created! ***")
    except Exception as e:
        print(f"*** Error when creating test msg data: {e} ***")
        
def main():
    """
    The main function of the script.
    """
    with app.app_context():
        # load_env_vars()
        create_db()
        create_admin_user()
        create_edu()
        create_exp()
        # create_msg()

if __name__ == "__main__":
    main()
