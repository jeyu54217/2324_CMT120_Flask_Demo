"""
Flask Forms for the portfolio app

Developed by Jerry Yu @ https://github.com/jeyu54217
------------------------------------------------
Developed for Coursework 2 of the CMT120 course at Cardiff University

Reference: 
    1. wtforms fields : https://wtforms.readthedocs.io/en/3.1.x/fields/
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired

class Login_form(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class Edu_form(FlaskForm):
    start_date = DateField('Start_date', validators=[DataRequired()] )
    end_date = DateField('End_date', validators=[DataRequired()])
    school = StringField('School', validators=[DataRequired()])
    degree = StringField('Degree', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit Education')

class Exp_form(FlaskForm):
    start_date = DateField('Start_date', validators=[DataRequired()])
    end_date = DateField('End_date', validators=[DataRequired()] )
    company = StringField('Company', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit Experience')

# class Msg_form(FlaskForm):
#     name = StringField('Name', validators=[DataRequired()])
#     title = StringField('Title', validators=[DataRequired()])
#     content = StringField('Content', validators=[DataRequired()])
#     create_date = DateField('Create Date', validators=[DataRequired()])
#     submit = SubmitField('Submit Message')

