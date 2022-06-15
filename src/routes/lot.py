from datetime import datetime, timedelta
from flask import session, render_template, request, redirect
from flask_login import login_required

from app import app, db, lots_schema, users_schema
from src.models.lot import Lot
from src.models.user import User
from src.models.queue import Queue


@app.route('/lot/<int:id_lot>', methods=[ 'GET', 'POST'])
@login_required
def get_lot(id_lot):
    id_user = int(session['_user_id'])
    user = db.session.query(User).get(id_user).login

    lots = db.session.query(Lot).filter(Lot.id == id_lot)
    lot = db.session.query(Lot).get(id_lot)
    timer = timedelta(hours=24)



    if request.method == 'POST':
        time_now = datetime.now()
        # time_now.strftime("%Y-%m-%d %H:%M:%S")
        if lot.time == None:
            end_queue = Queue(id_lot=id_lot, id_buyer=id_user, time=time_now+timer)
            lot.time = time_now

            try:
                db.session.add(end_queue)
                db.session.flush()
                db.session.commit()
                return redirect('lot/wishlist')
            except:
                return "При покупки произошла ошибка"

        elif lot.time < time_now:
            end_queue = Queue(id_lot=id_lot, id_buyer=id_user, time=time_now+timer)

            lot.price += int(request.form['increase'])
            lot.time = time_now

            try:
                db.session.add(end_queue)
                db.session.flush()
                db.session.commit()
                return redirect('lot/wishlist')
            except:
                return "При покупки произошла ошибка"

        else: 
            pass

    else:
        
        id_author = lots_schema.dump(lots, many=True)[0]['id_author']
        authors = db.session.query(User).filter(User.id == id_author)
        return render_template('lot.html', lots=lots, authors=authors, active1='active', active2='link-dark', active3='link-dark', user=user)