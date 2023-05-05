from flask import Flask,render_template,request,redirect,session

app = Flask(__name__)

@app.route('/')
def home():
    return "This is the Home Page!"

@app.route('/hello/<name>')
def name(name):
    return f"Hello, {name}"

if __name__=="__main__":
    app.run(debug=True,port=5001)