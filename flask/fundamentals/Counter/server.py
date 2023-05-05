from flask import Flask,render_template,request,redirect,session

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"

@app.route('/')
def home():
    if "page_count" in session:
        session["page_count"] += 1
    else:
        session["page_count"]=1
    if "count" not in session:
        session["count"]=0
    return render_template("index.html")

@app.route('/count', methods=['POST'])
def count():
    if "count" in session:
        session["count"] += int(request.form["count"])
    else:
        session["count"]=int(request.form["count"])
    return redirect('/')

@app.route('/count_2', methods=['POST'])
def count_2():
    if "count" in session:
        session["count"] += 2
    else:
        session["count"]=2
    return redirect('/')

@app.route('/reset', methods=['POST'])
def destroy_session():
    session.clear()
    session["count"]=0
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True,port=5001)