from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def basic_board():
    return render_template("index.html",x=8,y=8,color1="red",color2="black")

@app.route('/<int:y>')
def boardY(y):
    return render_template("index.html",x=8,y=y,color1="red",color2="black")

@app.route('/<int:y>/<int:x>')
def boardYX(y,x):
    return render_template("index.html",x=x,y=y,color1="red",color2="black")

@app.route('/<int:y>/<int:x>/<string:color1>')
def boardYXC1(y,x,color1):
    return render_template("index.html",x=x,y=y,color1=color1,color2="black")

@app.route('/<int:y>/<int:x>/<string:color1>/<string:color2>')
def boardYXC1C2(y,x,color1,color2):
    return render_template("index.html",x=x,y=y,color1=color1,color2=color2)

if __name__=="__main__":
    app.run(debug=True,port=5001)