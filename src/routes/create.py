from unicodedata import name
from flask import jsonify, redirect, session, request, render_template
from flask_login import login_required
from pyparsing import FollowedBy


from app import app, db, lot_schema
from src.models.lot import Lot
from src.models.user import User

import json


@app.route('/lot', methods=['POST', 'GET'])
@login_required
def create_lot():
    id_user = int(session['_user_id'])
    user = db.session.query(User).get(id_user).login
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        new_lot = Lot(id_author=id_user, name=name, description=description, price=price, status=False)
        try:
            db.session.add(new_lot)
            db.session.commit()
            return redirect('/lot/my')
        except:
            return "При создание лота произошла ошибка"
    else:
        return render_template("create.html", active1='link-dark', active2='active', active3='link-dark', user=user)
