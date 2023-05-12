from flask import flash
from flask_app.config.mysqlconnections import connectToMySQL
import re

EMAIL_REGEX = re.compile('^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    DB = "email_validation_schema"
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_all(cls):
        query="SELECT * FROM emails"
        results = connectToMySQL(cls.DB).query_db(query)
        emails = []
        for email in results:
            emails.append(cls(email))
        return emails
    @staticmethod
    def validate_email(email):
        is_valid = True
        if not EMAIL_REGEX.match(email['email']):
            flash('Email not Valid')
            is_valid = False
        else:
            for e in Email.get_all():
                if email['email'] == e.email:
                    flash('Email already in data')
                    is_valid=False
                    break
        return is_valid
    @classmethod
    def create_email(cls,data):
        query="""
        INSERT INTO emails(email)
        VALUES (%(email)s);
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    @classmethod
    def delete_email(cls,data):
        query = """
        DELETE FROM emails
        WHERE id = %(id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result