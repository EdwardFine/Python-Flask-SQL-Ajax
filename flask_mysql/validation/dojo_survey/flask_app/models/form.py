from flask import flash
from flask_app.config.mysqlconnections import connectToMySQL

class Form():
    DB = "dojo_survey_schema"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @staticmethod
    def validate_form(form):
        is_valid = True
        if len(form['name'])<1:
            flash('Name is required.')
            is_valid = False
        if 'location' not in form:
            flash('Location is required')
            is_valid = False
        if 'language' not in form:
            flash('Language is required')
            is_valid = False
        return is_valid

    @classmethod
    def create_survey(cls,data):
        query="""
        INSERT INTO dojos(name,location,language,comment)
        VALUES (%(name)s,%(location)s,%(language)s,%(comment)s);
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    
    @classmethod
    def get_one_survey_from_form(cls,data):
        query = """
        SELECT * FROM dojos
        WHERE name=%(name)s AND location=%(location)s AND language = %(language)s AND comment = %(comment)s;
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return cls(result[0])
    @classmethod
    def get_one_survey_from_id(cls,data):
        query = """
        SELECT * FROM dojos
        WHERE id = %(id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return cls(result[0])
    @classmethod
    def get_all(cls):
        query="SELECT * FROM dojos"
        results = connectToMySQL(cls.DB).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos