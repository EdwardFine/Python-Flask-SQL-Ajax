from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route("/say/<string:name>")
def hiName(name):
    return f"Hi {name.capitalize()}!"

@app.route("/repeat/<int:times>/<string:phrase>")
def repeat(times, phrase):
    return f"{phrase * times} " 

@app.errorhandler(404)
def not_found(e):
    return "Sorry! No response. Try again."

if __name__=="__main__":
    app.run(debug=True,port=5001)