"""
Flask routes for the portfolio app

Developed by Jerry Yu @ https://github.com/jeyu54217
------------------------------------------------
Developed for Coursework 2 of the CMT120 course at Cardiff University

References:
    1. Flask SQLAlchemy: https://flask.palletsprojects.com/en/2.0.x/patterns/sqlalchemy/
    2. SQLAlchemy: https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html
    3. flask_login: https://flask-login.readthedocs.io/en/latest/
    4. werkzeug.security: https://werkzeug.palletsprojects.com/en/3.0.x/utils/#module-werkzeug.security
"""
from flask import Blueprint, render_template, url_for, redirect, session, send_file, flash, request
from . import app, db
from .models import User, Experience, Education, Msg_board 
from .forms import Login_form, Edu_form, Exp_form, Msg_form
from flask_login import login_user, logout_user, current_user, login_required

bp_home = Blueprint('/', __name__, template_folder='templates', static_folder='static')

@app.route("/home")
@app.route("/")
def home():
    admin = User.query.filter_by(name="admin").first()
    return render_template('home.html', 
                           edus = admin.education, 
                           exps = admin.experience,
                           )
    
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = Login_form()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.username.data).first()
        remember = True if request.form.get('remember') else False
        if user is not None and user.verify_password(form.password.data):
            login_user(user, remember=remember)
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password!', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('Logout successful!', 'success')
    return redirect(url_for('home'))

@app.route("/edu_edit", methods=['GET', 'POST'])
@login_required
def edu_edit():
    admin = User.query.filter_by(name="admin").first()
    edu_form = Edu_form()
    # Add new education
    if edu_form.validate_on_submit():
        education = Education(
            start_date=edu_form.start_date.data,
            end_date=edu_form.end_date.data,
            school=edu_form.school.data,
            degree=edu_form.degree.data,
            description=edu_form.description.data,
            user_id=current_user.id,
            )
        db.session.add(education)
        db.session.commit()
        flash('Add Education successful!', 'success')
        return redirect(url_for('edu_edit'))
    return render_template('edu_edit.html', 
                           edus = admin.education, 
                           edu_form = edu_form,
                           )

@app.route("/exp_edit", methods=['GET', 'POST'])
@login_required
def exp_edit():
    admin = User.query.filter_by(name="admin").first()
    exp_form = Exp_form()
    # Add new experience
    if exp_form.validate_on_submit():
        experience = Experience(
            start_date=exp_form.start_date.data,
            end_date=exp_form.end_date.data,
            company=exp_form.company.data,
            position=exp_form.position.data,
            description=exp_form.description.data,
            user_id=current_user.id,
            )
        db.session.add(experience)
        db.session.commit()
        flash('Add Experience successful!', 'success')
        return redirect(url_for('exp_edit'))
    return render_template('exp_edit.html', 
                           exps = admin.experience, 
                           exp_form = exp_form,
                           )

@app.route('/delete_experience', methods=['POST'])
@login_required
def delete_experience():
    selected_ids = request.form.getlist('selected')
    for id in selected_ids:
        exp = Experience.query.get(id)
        db.session.delete(exp)
    db.session.commit()
    flash('Delete Experience successful!', 'success')
    return redirect(url_for('exp_edit'))

@app.route('/delete_education', methods=['POST'])
@login_required
def delete_education():
    selected_ids = request.form.getlist('selected')
    for id in selected_ids:
        edu = Education.query.get(id)
        db.session.delete(edu)
    db.session.commit()
    flash('Delete Education successful!', 'success')
    return redirect(url_for('edu_edit'))