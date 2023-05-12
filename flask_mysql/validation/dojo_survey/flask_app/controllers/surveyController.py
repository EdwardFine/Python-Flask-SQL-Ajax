from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.form import Form

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/process',methods=["POST"])
def process():
    print(request.form)
    if not Form.validate_form(request.form):
        return redirect('/')
    else:
        Form.create_survey(request.form)
        survey = Form.get_one_survey_from_form(request.form)
        print(survey)
        return redirect('/result/' + str(survey.id))

@app.route('/result/<int:id>')
def result(id):
    return render_template('result.html',survey=Form.get_one_survey_from_id({'id':id}))