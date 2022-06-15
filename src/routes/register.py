from flask import request, redirect, render_template
from werkzeug.security import  generate_password_hash

from app import app, db, users_schema
from src.models.user import User



@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        login = request.form['login']
        user_login = db.session.query(User).filter(User.login == login)
        result =  users_schema.dump(user_login, many=True)
        if result == []:
            hash = generate_password_hash(request.form['password'])
            new_user = User(login=login, name=name,  password=hash)
            try:
                db.session.add(new_user)
                db.session.commit()
                return redirect('/login')
            except:
                return "При регистрации произошла ошибка"
        else: 
            return render_template('register.html', mistake = 'такой логин уже есть!')
    else:
        return render_template('register.html')
