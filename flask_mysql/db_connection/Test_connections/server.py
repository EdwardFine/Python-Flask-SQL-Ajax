from flask import Flask,render_template,request,redirect,session
from friend import Friend

app = Flask(__name__)

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    return render_template("index.html", friends=Friend.get_all())

@app.route('/add_friend', methods=["POST"])
def add_friend():
    Friend.create_friend(request.form)
    return redirect('/')

@app.route('/show_friend/<int:id>')
def show_one(id):
    return render_template("show_friend.html",friend=Friend.get_one_friend({"id":id}))

@app.route('/update_friend/<int:id>')
def update_one(id):
    return render_template("update_friend.html",friend = Friend.get_one_friend({'id':id}))

@app.route('/edit_friend/<int:id>',methods=["POST"])
def edit_friend(id):
    friend_data={
        'id':id,
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'occupation':request.form['occupation']
    }
    Friend.update(friend_data)
    return redirect(f'/show_friend/{id}')

@app.route('/delete_friend/<int:id>')
def delete_friend(id):
    Friend.delete_friend({'id':id})
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True,port=5001)