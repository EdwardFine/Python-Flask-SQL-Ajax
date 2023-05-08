from flask import Flask,render_template,request,redirect,session
from random import randint
import math

app = Flask(__name__)
app.secret_key="Arg,gold"
log=[]

@app.route('/')
def home():
    if "gold" not in session:
        session["gold"]=0
    return render_template("index.html")

@app.route('/process_gold',methods=["POST"])
def processGold():
    print("Processing Gold")
    payouts = {"farm":randint(10,20),"cave":randint(5,10),"house":randint(2,5),"casino":randint(0,1)}
    gold_diff = session['gold']
    if request.form['location']=="reset":
        session["gold"]=0
        session['log']=""
        return redirect('/process_activities/None/reset')
    elif request.form['location']=="casino":
        if randint(1,2)==1:
            session["gold"] += randint(0,50)
        else:
            session["gold"] -= randint(0,50)
    else:
        session["gold"] += payouts[request.form['location']]
    gold_diff = session["gold"]-gold_diff
    return redirect('/process_activities/'+str(gold_diff)+'/'+request.form['location'])

@app.route('/process_activities/<gold_diff>/<location>')
def activities(gold_diff,location):
    if gold_diff != "None":
        gold_diff=int(gold_diff)
        if gold_diff <0:
            message=f"<li class='negative-gold'>Entered a casino and lost {abs(gold_diff)} golds... Ouch..</li>"
        else:
            message=f"<li class='positive-gold'>Earned {gold_diff} golds from the {location}</li>"
        message+=session['log']
        session["log"]=message
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True,port=5001)