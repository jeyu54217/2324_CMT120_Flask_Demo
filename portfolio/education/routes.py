"""
Flask routes for the main app

Developed by Jerry Yu @ https://github.com/jeyu54217
------------------------------------------------
Developed for Coursework 2 of the CMT120 course at Cardiff University

References:
    1. Flask SQLAlchemy: https://flask.palletsprojects.com/en/2.0.x/patterns/sqlalchemy/
    2. SQLAlchemy: https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html
    3. flask_login: https://flask-login.readthedocs.io/en/latest/
    4. werkzeug.security: https://werkzeug.palletsprojects.com/en/3.0.x/utils/#module-werkzeug.security
"""

from flask import render_template, url_for, redirect, session, send_file
from blog import app
from flask_login import current_user

from blog.utils.settings import *
from blog.utils.errors import *
from blog.utils.formatting import *

import json

# Import all routes
from blog.routes.accounts import *
from blog.routes.auth import *
from blog.routes.comments import *
from blog.routes.posts import *


@app.route("/")
@app.route("/home")  # Main portfolio page, with all admin posts showing up.
def home():
    # The current_page session key will be used by the color mode toggler to return to the same page
    session['current_page'] = url_for('home')
    from blog.models import User
    admin = User.query.filter_by(username="admin").first()
    avatar = url_for('static', filename='img/' + 'admin.jpg')
    return render_template('home.html', posts=admin.post, avatar=avatar)


@app.route("/about")
def about():
    session['current_page'] = url_for('about')
    return render_template('about.html', title='About')


@app.route("/toggle_mode")
def toggle_mode():
    if session.get('mode') is None:
        session['mode'] = 'dark'
    else:
        session['mode'] = 'dark' if session.get('mode') == 'light' else 'light'
    if current_user.is_authenticated:
        settings = json.loads(current_user.settings_json)
        settings['mode'] = session['mode']
        current_user.settings_json = json.dumps(settings)
        from blog import db
        db.session.commit()
    return redirect(session['current_page'])


@app.route("/cv_download")
def cv_download():
    return send_file('static/cv.pdf', as_attachment=True)
