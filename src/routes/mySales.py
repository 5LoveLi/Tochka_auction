from flask import session, render_template, request, redirect
from flask_login import login_required

from app import app, db
from src.models.lot import Lot
from src.models.user import User


@app.route('/lot/my', methods=[ 'GET'])
@login_required
def get_my_lots():
    id_user = int(session['_user_id'])
    user = db.session.query(User).get(id_user).login
    lots = db.session.query(Lot).filter(Lot.id_author == id_user)
    return render_template('mySales.html', lots=lots, active1='link-dark', active2='active', active3='link-dark', user=user)