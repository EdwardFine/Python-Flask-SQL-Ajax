from flask import flash
from flask_app.config.mysqlconnections import connectToMySQL

class Game:
    DB = 'fan_requests_schema'
    def __init__(self,data):
        self.id = data['id']
        self.title=data['title']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def checkIfGameInDB(cls,data):
        query="""
            SELECT * FROM games
            WHERE id=%(id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query,data)
        if len(results)==0:return False
        else:return True 
    @classmethod
    def addGame(cls,data):
        query="""
            INSERT INTO games(id,title)
            VALUES(%(id)s,%(title)s);
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    @classmethod
    def getGameById(cls,data):
        query="""
            SELECT * FROM games
            WHERE id=%(id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result[0]