from flask import session, render_template
from flask_login import login_required

from app import app, db
from src.models.lot import Lot
from src.models.user import User

@app.route('/lot/other', methods=['GET']) 
@login_required
def get_lots():
    id_user = int(session['_user_id'])
    user = db.session.query(User).get(id_user).login
    lots = db.session.query(Lot).filter(Lot.id_author != id_user)
    return render_template('gallery.html', lots=lots, active1='active', active2='link-dark', active3='link-dark', user=user)


@app.route('/lot/other/<int:id_seller>', methods=['GET']) 
@login_required
def get_lots_seller(id_seller):
    id_user = int(session['_user_id'])
    user = db.session.query(User).get(id_user).login
    lots = db.session.query(Lot).filter(Lot.id_author == id_seller)
    return render_template('gallery.html', lots=lots, active1='active', active2='link-dark', active3='link-dark', user=user)
    