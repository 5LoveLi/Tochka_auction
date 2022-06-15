from flask import  redirect
from flask_login import login_required, logout_user

from app import app


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/login')