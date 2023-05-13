from flask import flash
from flask_app.config.mysqlconnections import connectToMySQL
import re


EMAIL_REGEX = re.compile('^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    DB = 'users_schema'
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query="SELECT * FROM users"
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
    
    @staticmethod
    def validate_user_register(user):
        is_valid = True
        if len(user['first_name']) <1:
            flash('First name is needed, field was empty.')
            is_valid = False
        if len(user['last_name']) <1:
            flash('Last name is needed, field was empty.')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash('Email not Valid')
            is_valid = False
        else:
            for u in User.get_all():
                if user['email'] == u.email:
                    flash('Account Already Made With Given Email')
                    is_valid=False
                    break
        if len(user['password']) < 1:
            flash("Password is needed, field was empty")
            is_valid = False
        else:
            has_cap = False
            has_num=False
            for letter in user['password']:
                if letter.isupper():
                    has_cap=True
                elif letter.isdigit():
                    has_num = True
                if has_cap and has_num:break
            if not has_cap or not has_num:
                flash('Password needs at least one uppercase and one number')
                is_valid=False
        if user['password'] != user['confirm_password']:
            flash('Passwords do not match')
            is_valid = False
        return is_valid

    @staticmethod
    def validate_user_login(data):
        is_valid = True
        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
        if len(data['password']) < 1:
            is_valid = False
        return is_valid
    @classmethod
    def create_user(cls,data):
        query="""
        INSERT INTO users(first_name,last_name,email,password)
        VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    @classmethod
    def get_one_user_by_email(cls,data):
        query="""
        SELECT * FROM users
        WHERE email=%(email)s;
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        try:
            return cls(result[0])
        except IndexError:
            return result
    @classmethod
    def get_one_user_by_id(cls,data):
        query="""
        SELECT * FROM users
        WHERE id=%(id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        try:
            return cls(result[0])
        except IndexError:
            return result