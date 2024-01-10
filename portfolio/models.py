"""
Flask Database Models for the portfolio app

Developed by Jerry Yu @ https://github.com/jeyu54217
------------------------------------------------
Developed for Coursework 2 of the CMT120 course at Cardiff University

References:
    1. Flask SQLAlchemy: https://flask.palletsprojects.com/en/2.0.x/patterns/sqlalchemy/
    2. SQLAlchemy: https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html
    3. flask_login: https://flask-login.readthedocs.io/en/latest/
    4. werkzeug.security: https://werkzeug.palletsprojects.com/en/3.0.x/utils/#module-werkzeug.security
"""
from datetime import datetime
from portfolio import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=True, nullable=False)
    hashed_psw = db.Column(db.String(128))
    education = db.relationship('Education', backref='user', lazy=True, cascade="all, delete")
    experience = db.relationship('Experience', backref='user', lazy=True, cascade="all, delete")
    msg_board = db.relationship('Msg_board', backref='user', lazy=True, cascade="all, delete")
    
    @property # Allows the method to be accessed like an attribute.
    def password(self): 
        """
        A security measure to prevent the password from being accessed directly.
        """
        raise AttributeError('Password is not allowed to read.')
    
    @password.setter # Allows the method to be called when you assign a value to the property.
    def password(self, psw):
        """
        A security measure to hashes the password and stores the hash in the hashed_psw attribute. 
        """
        self.hashed_psw = generate_password_hash(psw)
        return None

    def verify_password(self, psw) -> bool:
        """
        It hashes the input password as the stored hash and checks if the results match. 
        """
        return check_password_hash(self.hashed_psw, psw)
    
class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.String(7), nullable=False, default=datetime.utcnow().strftime('%Y-%m'))
    end_date = db.Column(db.String(7), nullable=False, default=datetime.utcnow().strftime('%Y-%m'))
    school = db.Column(db.Text, nullable=False)
    degree = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
                return f"Education of user {self.user_id} on {self.school}'"

class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.String(7), nullable=False, default=datetime.utcnow().strftime('%Y-%m'))
    end_date = db.Column(db.String(7), nullable=False, default=datetime.utcnow().strftime('%Y-%m'))
    company = db.Column(db.Text, nullable=False)
    position = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Experience of user {self.user_id} on {self.company}'"

class Msg_board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"Msg to user {self.user_id} about {self.title} from {self.name}"
    
@login_manager.user_loader # This callback is used to reload the user object from the user ID stored in the session.
def load_user(user_id) -> User(object)| None:
    """
    Load a user from the database based on the user_id stored in the session.
    """
    return User.query.get(int(user_id))
