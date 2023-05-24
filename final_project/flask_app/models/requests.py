from flask import flash
from flask_app.config.mysqlconnections import connectToMySQL
from flask_app.models import user,games

class Request:
    DB = 'fan_requests_schema'
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.game_id = data['game_id']
        self.title=data['title']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = ""
        self.game = ""
    
    @staticmethod
    def validate_request(data):
        is_valid = True
        if len(data['title'])<1:
            flash("Title wasn't filled out.")
            is_valid=False
        elif len(data['title']) > 45:
            flash("Maximum length of title is 45 characters.")
            is_valid = False
        if len(data['description']) < 1:
            flash("Request is necessary")
            is_valid = False
        return is_valid
    
    @classmethod
    def createRequest(cls,data):
        query="""
            INSERT INTO requests(user_id,game_id,title,description)
            VALUES(%(user_id)s,%(game_id)s,%(title)s,%(description)s);
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    
    @classmethod
    def getAllRequestsForGameId(cls,data):
        query="""
            SELECT * FROM requests
            JOIN users ON users.id = requests.user_id
            WHERE game_id=%(game_id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query,data)
        requests = []
        for request in results:
            one_request = cls(request)
            user_data={
                'id':request['user_id'],
                'username':request['username'],
                'email':request['email'],
                'created_at':request['users.created_at'],
                'updated_at':request['users.updated_at']
            }
            one_request.user = user.User(user_data)
            requests.append(one_request)
        return requests
    
    @classmethod
    def getRequestById(cls,data):
        query="""
            SELECT * FROM requests
            JOIN users ON users.id = requests.user_id
            JOIN games ON games.id = requests.game_id
            WHERE requests.id=%(request_id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query,data)
        for request in results:
            one_request = cls(request)
            user_data={
                'id':request['user_id'],
                'username':request['username'],
                'email':request['email'],
                'created_at':request['users.created_at'],
                'updated_at':request['users.updated_at']
            }
            game_data={
                'id':request['game_id'],
                'title':request['games.title'],
                'description':request['description'],
                'created_at':request['games.created_at'],
                'updated_at':request['games.updated_at']
            }
            one_request.user = user.User(user_data)
            one_request.game = games.Game(game_data)
        return one_request
    
    @classmethod
    def deleteRequestById(cls,data):
        query="""
            DELETE FROM requests
            WHERE id=%(request_id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results
    
    @classmethod
    def updateRequestById(cls,data):
        query="""
            UPDATE requests
            SET title=%(title)s,description=%(description)s
            WHERE id = %(request_id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results