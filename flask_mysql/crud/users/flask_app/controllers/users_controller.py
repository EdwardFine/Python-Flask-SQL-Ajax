from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.users import User

@app.route('/')
def home():
    return render_template("index.html",users=User.get_all())

@app.route('/create_user')
def create_user():
    return render_template("create_user.html",mode="Create")

@app.route('/show_one/<int:id>')
def show_one(id):
    return render_template('one_user.html',user=User.get_one_user({'id':id}))

@app.route('/process_create',methods=["POST"])
def process_create():
    User.create_user(request.form)
    return redirect('/')

@app.route('/update_user/<int:id>')
def update_user(id):
    return render_template("create_user.html",mode="Update",user=User.get_one_user({'id':id}))

@app.route('/process_update/<int:id>',methods=["POST"])
def process_update(id):
    user_data = {
        'id':id,
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email']
    }
    User.update_user(user_data)
    return redirect('/')

@app.route('/delete_user/<int:id>')
def delete_user(id):
    User.delete_user({'id':id})
    return redirect('/')