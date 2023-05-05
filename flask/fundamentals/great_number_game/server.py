from flask import Flask,render_template,request,redirect,session
import random

app = Flask(__name__)
app.secret_key = "dk rap"
leaderboard=[]


@app.route('/')
def home():
    if "count" not in session:
        session['count']=0
    if 'answer' not in session:
        session['answer']=random.randint(1,100)
    if 'result' not in session:
        session['result'] = 'none'
    return render_template("index.html",result=session["result"])

@app.route('/guess',methods=["POST"])
def guess():
    session["count"]+=1
    session["guess"] = request.form['guess']
    if session["guess"] == "":
        session["guess"]=0
    if int(session['guess']) < session['answer']:
        session['result'] = 'low'
    elif int(session['guess']) > session['answer']:
        session['result'] = 'high'
    else:
        session['result'] = 'correct'
    print(session)
    return redirect('/endgame')

@app.route('/endgame')
def checkend():
    if session['result'] == 'correct':
        return redirect('/')
    elif session['count']>=5:
        session['result'] = 'lost'
        return redirect('/')
    else:
        return redirect('/')

@app.route('/resetgame')
def resetGame():
    session.clear()
    return redirect('/')

@app.route('/leaderboard_process',methods=["POST"])
def processLeaderboard():
    session['name'] = request.form['name']
    for item in leaderboard:
        if item['name'] == session['name']:
            if item['score'] > session['count']:
                item['score'] = session['count']
                print(leaderboard)
                return redirect('/leaderboard')
            else:
                print(leaderboard)
                return redirect('/leaderboard')
    leaderboard.append({'name':session['name'],'score':session['count']})
    session.clear()
    return redirect('/leaderboard')

@app.route('/leaderboard')
def displayLeaderboard():
    print(leaderboard)
    return render_template('leaderboard.html',leaderboard=leaderboard)


if __name__=="__main__":
    app.run(debug=True,port=5001)