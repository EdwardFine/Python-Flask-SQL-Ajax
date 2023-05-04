from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "This is the Home Page!"

@app.route('/play')
def play():
    return render_template("play.html",num=3,py_color = "rgb(159, 197, 248)")

@app.route('/play/<int:num>')
def play_num(num):
    return render_template("play.html",num=num,py_color = "rgb(159, 197, 248)")

@app.route('/play/<int:num>/<string:color>')
def play_num_color(num,color):
    return render_template("play.html",num=num,py_color = color)

if __name__=="__main__":
    app.run(debug=True,port=5001)