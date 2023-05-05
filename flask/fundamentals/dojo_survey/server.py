from flask import Flask,render_template,request,redirect,session

app = Flask(__name__)
app.secret_key = "DK DONKEY KONG"
required=False

@app.route('/')
def home():
    return render_template("index.html",required=session["name"].strip())

@app.route('/process',methods=["POST"])
def process():
    for key in request.form:
        session[key]=request.form[key]
    if session["name"].strip()=="":
        return redirect('/')
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__=="__main__":
    app.run(debug=True,port=5001)