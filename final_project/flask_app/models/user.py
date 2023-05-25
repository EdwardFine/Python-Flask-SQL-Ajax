from flask import flash
from flask_app.config.mysqlconnections import connectToMySQL
import re


EMAIL_REGEX = re.compile('^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    DB = 'fan_requests_schema'
    def __init__(self,data):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        if 'password' in data:
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
        if len(user['username']) <1:
            flash('Username is needed, field was empty.')
            is_valid = False
        elif len(user['username']) >16:
            flash('Username must be less than 16 characters.')
            is_valid=False
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
        INSERT INTO users(username,email,password)
        VALUES (%(username)s,%(email)s,%(password)s);
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
    
    @classmethod
    def checkLiked(self,data):
        query="""
        SELECT isLiked FROM request_likes
        WHERE user_id=%(user_id)s AND request_id = %(request_id)s;
        """
        result = connectToMySQL(User.DB).query_db(query,data)
        return result
    
    @classmethod
    def processLike(cls,data):
        result = User.checkLiked(data)
        if len(result)==0:
            query="""
            INSERT INTO request_likes(user_id,request_id,isLiked)
            VALUES (%(user_id)s,%(request_id)s,%(likeValue)s);
            """
            result = connectToMySQL(cls.DB).query_db(query,data)
            return result
        elif result[0]['isLiked'] !=data['likeValue']:
            query="""
            UPDATE request_likes SET isLiked = %(likeValue)s
            WHERE user_id = %(user_id)s AND request_id = %(request_id)s;
            """
            result = connectToMySQL(cls.DB).query_db(query,data)
            return result
        elif result[0]['isLiked']==data['likeValue']:
            query="""
            DELETE FROM request_likes
            WHERE user_id = %(user_id)s AND request_id = %(request_id)s;
            """
            result = connectToMySQL(cls.DB).query_db(query,data)
            return result
        else:
            return False

    @classmethod
    def updateLike(cls,data):
        query="""
        UPDATE request_likes SET isLiked = %(likeValue)s
        WHERE user_id = %(user_id)s AND request_id = %(request_id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    
    @classmethod
    def removeLike(cls,data):
        query="""
        DELETE FROM request_likes
        WHERE user_id = %(user_id)s AND request_id = %(request_id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result