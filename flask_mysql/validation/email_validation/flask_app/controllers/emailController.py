from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.email import Email

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/process_email', methods = ["POST"])
def process_email():
    if not Email.validate_email(request.form):
        return redirect('/')
    else:
        Email.create_email(request.form)
        session['email'] = request.form['email']
        return redirect('/all_emails')

@app.route('/all_emails')
def display_emails():
    return render_template("all_emails.html",emails = Email.get_all(), new_email = session['email'])

@app.route('/delete_email/<int:id>')
def delete_email(id):
    Email.delete_email({'id':id})
    session['email']= None
    return redirect('/all_emails')