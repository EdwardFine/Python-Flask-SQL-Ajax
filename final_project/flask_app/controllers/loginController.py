from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/register_form')
def register_form():
    return render_template('register.html')

@app.route('/login_form')
def login_form():
    return render_template('login.html')

@app.route('/register_user', methods=["POST"])
def register_user():
    if not User.validate_user_register(request.form):
        session['last_request'] = 'register'
        return redirect('/register_form')
    else:
        hash_password = bcrypt.generate_password_hash(request.form['password'])
        user_data = {
            'username':request.form['username'],
            'email':request.form['email'],
            'password':hash_password,
        }
        User.create_user(user_data)
        user_in_db = User.get_one_user_by_email(request.form)
        session['user_id'] = user_in_db.id
        return redirect('/')

@app.route('/login',methods=["POST"])
def login():
    if not User.validate_user_login(request.form):
        flash('Email/Password not Valid')
        return redirect('/login_form')
    user_in_db = User.get_one_user_by_email(request.form)
    if not user_in_db:
        flash('Email/Password not Valid')
        return redirect('/login_form')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Email/Password not Valid')
        return redirect('/login_form')
    session['user_id']=user_in_db.id
    session['last_request'] = ''
    return redirect('/')


@app.route('/signout')
def signout():
    session.clear()
    return redirect('/')