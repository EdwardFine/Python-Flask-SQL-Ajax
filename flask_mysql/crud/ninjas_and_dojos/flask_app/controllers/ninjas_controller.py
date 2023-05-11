from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.ninjas import Ninja
from flask_app.models.dojos import Dojo

@app.route('/add_ninja/<int:dojo_id>')
def add_ninja(dojo_id):
    return render_template("add_ninja.html",dojos=Dojo.get_all(),mode="Create")

@app.route('/process_add_ninja/<int:dojo_id>',methods=["POST"])
def process_add_ninja(dojo_id):
    ninja_data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'age':request.form['age'],
        'dojo_id':dojo_id
    }
    Ninja.create_ninja(ninja_data)
    return redirect('/show_dojo/' + str(dojo_id))

@app.route('/update_ninja/<int:ninja_id>')
def update_ninja(ninja_id):
    return render_template('add_ninja.html',ninja=Ninja.get_one_ninja({'id':ninja_id}),mode="Update",dojos = Dojo.get_all())

@app.route('/process_update_ninja/<int:ninja_id>',methods=["POST"])
def process_update_ninja(ninja_id):
    ninja_data = {
        'id':ninja_id,
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'age':request.form['age'],
        'dojo_id':request.form['dojo_id'],
    }
    Ninja.update_ninja(ninja_data)
    return redirect('/show_dojo/' + str(request.form['dojo_id']))

@app.route('/show_ninja/<int:ninja_id>')
def show_ninja(ninja_id):
    return render_template('show_ninja.html',ninja=Ninja.get_one_ninja({'id':ninja_id}))

@app.route('/delete_ninja/<int:ninja_id>')
def delete_ninja(ninja_id):
    ninja = Ninja.get_one_ninja({'id':ninja_id})
    dojo_id = ninja.dojo_id
    Ninja.delete_ninja({'id':ninja_id})
    del ninja
    return redirect('/show_dojo/' + str(dojo_id))