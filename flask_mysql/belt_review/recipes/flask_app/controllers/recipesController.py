from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.recipes import Recipe
from flask_app.models.user import User

@app.route('/dashboard')
def dashboard():
    if session['user_id'] != 0:
        return render_template("dashboard.html",user =User.get_one_user_by_id({'id':session['user_id']}),recipes = Recipe.get_all_recipes_and_users() )
    else:
        return redirect('/')

@app.route('/create_recipe')
def create_recipe():
    if session['user_id'] != 0:
        return render_template('create_recipe.html')
    return redirect('/')

@app.route('/process_create_recipe',methods=["POST"])
def process_create_recipe():
    if session['user_id'] !=0:
        if not Recipe.validate_recipe(request.form):
            return redirect('/create_recipe')
        recipe_data = {
            'user_id' : session['user_id'],
            'name':request.form['name'],
            'description':request.form['description'],
            'instruction':request.form['instruction'],
            'date_made':request.form['date_made'],
        }
        if request.form['under_30'] == "True":
            recipe_data['under_30'] = True
        else:
            recipe_data['under_30'] = False
        Recipe.create_recipe(recipe_data)
        return redirect('/dashboard')
    return redirect('/')

@app.route('/view_recipe/<int:recipe_id>')
def view_recipe(recipe_id):
    if session['user_id'] != 0:
        return render_template('view_recipe.html',recipe = Recipe.get_recipe_by_id({'id':recipe_id}))
    return redirect('/')

@app.route('/delete_recipe/<int:recipe_id>')
def delete_recipe(recipe_id):
    user = Recipe.get_recipe_by_id({'id':recipe_id})
    if session['user_id'] == user['user'].id:
        Recipe.delete_recipe_by_id({'id':recipe_id})
        return redirect('/dashboard')
    return redirect('/')

@app.route('/update_recipe/<int:recipe_id>')
def update_recipe(recipe_id):
    user = Recipe.get_recipe_by_id({'id':recipe_id})
    if session['user_id'] == user['user'].id:
        return render_template("edit_recipe.html",recipe = user)

@app.route('/process_update_recipe/<int:recipe_id>',methods=["POST"])
def process_update_recipe(recipe_id):
    user = Recipe.get_recipe_by_id({'id':recipe_id})
    if session['user_id'] == user['user'].id:
        if not Recipe.validate_recipe(request.form):
            return redirect(f'/update_recipe/{recipe_id}')
        recipe_data = {
            'id':recipe_id,
            'name':request.form['name'],
            'description':request.form['description'],
            'instruction':request.form['instruction'],
            'date_made':request.form['date_made'],
        }
        if request.form['under_30'] == "True":
            recipe_data['under_30'] = True
        else:
            recipe_data['under_30'] = False
        Recipe.update_recipe(recipe_data)
        return redirect('/dashboard')
    return redirect('/')