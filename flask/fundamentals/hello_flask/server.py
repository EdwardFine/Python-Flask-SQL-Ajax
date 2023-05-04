from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/hello/<string:str>/<int:num>')
def hello(str,num):
    return render_template("hello.html",str = str, num=num)


if __name__=="__main__":
    app.run(debug=True,port=5001)