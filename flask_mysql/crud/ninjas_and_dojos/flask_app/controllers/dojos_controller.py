from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.dojos import Dojo

@app.route('/')
def dojos_home():
    if not 'success' in session:
        session['success']=True
    return render_template("index.html",dojos=Dojo.get_all(),delete_success=session['success'])

@app.route('/create_dojo',methods=["POST"])
def create_dojo():
    Dojo.create_dojo(request.form)
    return redirect('/')

@app.route('/delete_dojo/<int:id>')
def delete_dojo(id):
    session['success'] = Dojo.delete_dojo({'id':id})
    return redirect('/')

@app.route('/show_dojo/<int:id>')
def show_one_dojo(id):
    if session['success'] == False:
        session['success']=True
    dojo = Dojo.get_one_dojo({'id':id})
    return render_template("show_dojo.html",one_dojo=dojo,length = len(dojo.all_ninjas))

@app.route('/update_dojo/<int:id>')
def update_dojo(id):
    if session['success'] == False:
        session['success']=True
    return render_template("update_dojo.html",dojo=Dojo.get_one_dojo({'id':id}))

@app.route('/process_update_dojo/<int:id>',methods=["POST"])
def process_update_dojo(id):
    Dojo.update_dojo({'id':id,'name':request.form['name']})
    return redirect('/show_dojo/' + str(id))