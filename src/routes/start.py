from flask import session, render_template

from app import app

@app.route('/', methods=['GET']) 
def start():
    return render_template('start.html')
