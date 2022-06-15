from flask import make_response, request, jsonify, render_template, redirect
from flask_login import login_user
from werkzeug.security import  check_password_hash

from app import app, db, user_schema
from src.models.user import User

import json

@app.route("/login", methods =['POST', 'GET'])
def login():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        user = db.session.query(User).filter(User.login == login).first()
        if user and check_password_hash(user.password, password):
            if login_user(user):
                return redirect('/lot/other')
            else:
                return '', 405
    else:
        return render_template('login.html')