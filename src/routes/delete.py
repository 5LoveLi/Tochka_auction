from flask import session, render_template, request, redirect
from flask_login import login_required

from app import app, db, lots_schema
from src.models.lot import Lot
from src.models.queue import Queue


@app.route('/delete/<int:id_lot>', methods=['GET'])
@login_required
def delete_my_queue(id_lot):
    lot = db.session.query(Lot).filter(Lot.id == id_lot).one()

    try:
        db.session.delete(lot)
        db.session.commit()
        return redirect('/lot/my')
    except:
        return "При удаление лота произошла ошибка"

    
    