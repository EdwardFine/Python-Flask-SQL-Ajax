from flask_app import app
from flask import render_template,redirect,request,session,flash,jsonify
from flask_app.models.user import User
from flask_app.models.games import Game
from flask_app.models.requests import Request
import requests
import os

# Home Page

@app.route('/')
def home():
    if 'user_id' not in session:
        session['user_id']=0
    return render_template('home.html',user=User.get_one_user_by_id({'id':session['user_id']}))

@app.route('/home_games')
def home_games():
    r = requests.get(f"https://api.rawg.io/api/games?key={os.environ.get('RAWG_API_KEY')}")
    return jsonify(r.json())

# Single Game View

@app.route('/single_game/<int:id>')
def single_game(id):
    r = requests.get(f"https://api.rawg.io/api/games/{id}?key={os.environ.get('RAWG_API_KEY')}")
    return jsonify(r.json())

@app.route('/view_game/<int:id>')
def view_game(id):
    return render_template("game.html",id=id, user=User.get_one_user_by_id({'id':session['user_id']}),requests = Request.getAllRequestsForGameId({'game_id':id}))

@app.route('/check_game/',methods=["POST"])
def check_game():
    game_id=request.form['id']
    if not Game.checkIfGameInDB({'id':game_id}):
        Game.addGame(request.form)
    return redirect(f'/view_game/{game_id}')

#Create Requests

@app.route('/create_request_form/<int:id>')
def create_request_form(id):
    if session['user_id'] == 0:
        return redirect('/login_form')
    else:
        return render_template('create_request.html',id=id, user=User.get_one_user_by_id({'id':session['user_id']}),game = Game.getGameById({'id':id}))

@app.route("/create_request/<int:id>",methods=["POST"])
def create_request(id):
    if session['user_id'] ==0:
        return redirect('/login_form')
    elif not Request.validate_request(request.form):
        return redirect(f'/create_request_form/{id}')
    else:
        request_data = {
            'user_id':session['user_id'],
            'game_id':id,
            'title':request.form['title'],
            'description':request.form['description']
        }
        Request.createRequest(request_data)
        return redirect(f'/view_game/{id}')

# View Requests

@app.route("/view_request/<int:request_id>")
def view_request(request_id):
    return render_template("view_request.html",user=User.get_one_user_by_id({'id':session['user_id']}),request = Request.getRequestById({'request_id':request_id}))

# Delete Requests

@app.route("/delete_request/<int:request_id>")
def delete_request(request_id):
    request = Request.getRequestById({"request_id":request_id})
    if session['user_id'] != request.user.id:
        return redirect('/login_form')
    else:
        Request.deleteRequestById({'request_id':request_id})
        return redirect(f'/view_game/{request.game.id}')

# Edit Requests

@app.route("/edit_request/<int:request_id>")
def edit_request(request_id):
    request = Request.getRequestById({"request_id":request_id})
    if session['user_id'] != request.user.id:
        return redirect('/login_form')
    else:
        return render_template("edit_request.html",user=User.get_one_user_by_id({'id':session['user_id']}),game = Game.getGameById({'id':request.game.id}),request=request)

@app.route('/update_request/<int:request_id>',methods=["POST"])
def update_request(request_id):
    requests = Request.getRequestById({"request_id":request_id})
    if session['user_id'] != requests.user.id:
        return redirect('/login_form')
    else:
        request_data={
            'request_id':request_id,
            'title':request.form['title'],
            'description':request.form['description']
        }
        if not Request.validate_request(request_data):
            return redirect(f'/edit_request/{request_id}')
        else:
            Request.updateRequestById(request_data)
            return redirect(f'/view_request/{request_id}')

# Process Likes

@app.route('/add_like/<int:request_id>')
def add_like(request_id):
    if session['user_id']==0:
        return redirect('/login_form')
    User.processLike({'user_id':session['user_id'],'request_id':request_id,"likeValue":1})
    return redirect(f"/view_game/{Request.getRequestById({'request_id':request_id}).game.id}")

@app.route('/add_dislike/<int:request_id>')
def add_dislike(request_id):
    if session['user_id']==0:
        return redirect('/login_form')
    User.processLike({'user_id':session['user_id'],'request_id':request_id,"likeValue":0})
    return redirect(f"/view_game/{Request.getRequestById({'request_id':request_id}).game.id}")