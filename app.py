from datetime import datetime, timedelta
from flask import Flask, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True
db = SQLAlchemy(app)

app.config.from_pyfile('config.py')

login_manager = LoginManager(app)

#####MODELS#######

from src.models.user import User
from src.models.lot import Lot
from src.models.queue import Queue


#####SCHEMA########

from src.schema.user import UserSchema
from src.schema.lot import LotSchema
from src.schema.queue import QueueSchema


users_schema = UserSchema(many=True)
lots_schema = LotSchema(many=True)
queues_schema = QueueSchema(many=True)


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)


if __name__ == "__main__":
    app.run()