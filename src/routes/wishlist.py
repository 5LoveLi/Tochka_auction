from flask import session, render_template
from flask_login import login_required

from app import app, db, queues_schema
from src.models.queue import Queue
from src.models.lot import Lot
from src.models.user import User


@app.route('/lot/wishlist', methods =['GET'])
@login_required
def want_buy():
    id_user = int(session['_user_id'])
    user = db.session.query(User).get(id_user).login
    id_lots = db.session.query(Queue.id_lot).filter(Queue.id_buyer == id_user)
    lots = db.session.query(Lot).filter(Lot.id == id_lots)

    return render_template('wishlist.html', lots=lots, active1='link-dark', active2='link-dark', active3='active', user=user)