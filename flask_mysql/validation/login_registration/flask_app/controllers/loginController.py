from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def home():
    if 'last_request' not in session:
        session['last_request'] = ""
    if 'id' not in session:
        session['user_id']=0
    print(session['user_id'])
    return render_template('index.html',last_request = session['last_request'])

@app.route('/register_user', methods=["POST"])
def register_user():
    if not User.validate_user_register(request.form):
        session['last_request'] = 'register'
        return redirect('/')
    else:
        hash_password = bcrypt.generate_password_hash(request.form['password'])
        user_data = {
            'first_name':request.form['first_name'],
            'last_name':request.form['last_name'],
            'email':request.form['email'],
            'password':hash_password,
        }
        User.create_user(user_data)
        session['last_request'] = ''
        user_in_db = User.get_one_user_by_email(request.form)
        session['user_id'] = user_in_db.id
        session['last_request'] = ''
        return redirect(f'/dashboard/{user_in_db.id}')

@app.route('/login',methods=["POST"])
def login():
    if not User.validate_user_login(request.form):
        flash('Email/Password not Valid')
        session['last_request'] = 'login'
        return redirect('/')
    user_in_db = User.get_one_user_by_email(request.form)
    if not user_in_db:
        flash('Email/Password not Valid')
        session['last_request'] = 'login'
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Email/Password not Valid')
        session['last_request'] = 'login'
        return redirect('/')
    session['user_id']=user_in_db.id
    session['last_request'] = ''
    return redirect(f'/dashboard/{user_in_db.id}')

@app.route('/dashboard/<int:id>')
def dashboard(id):
    if id == session['user_id']:
        return render_template("dashboard.html",user =User.get_one_user_by_id({'id':session['user_id']}) )
    else:
        return redirect('/')

@app.route('/signout')
def signout():
    session.clear()
    return redirect('/')