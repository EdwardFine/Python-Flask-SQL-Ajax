from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.friends import Friend

@app.route('/')
def home():
    return redirect('/friendships')

@app.route('/friendships')
def friendships():
    return render_template('index.html',users = Friend.get_all_users(),friends = Friend.get_all_friends())

@app.route('/create_user', methods=["POST"])
def create_user():
    Friend.create_user(request.form)
    return redirect('/friendships')

@app.route('/create_friendship',methods=["POST"])
def create_friendship():
    user = Friend.get_user_by_id({'id':request.form['user']})
    friend = Friend.get_user_by_id({'id':request.form['friend']})
    if not Friend.check_friendship(user,friend):
        return redirect('/friendships')
    Friend.create_relationship(user,friend)
    return redirect('/friendships')