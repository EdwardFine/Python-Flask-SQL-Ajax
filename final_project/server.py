from flask_app import app
from flask_app.controllers import loginController,requestController

if __name__=="__main__":
    app.run(debug=True,port=5000)