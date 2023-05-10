from flask_app.config.mysqlconnections import connectToMySQL

class User():
    DB = "users_schema"
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
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
    @classmethod
    def create_user(cls,data):
        query="""
        INSERT INTO users(first_name,last_name,email)
        VALUES (%(first_name)s,%(last_name)s,%(email)s);
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    @classmethod
    def get_one_user(cls,data):
        query = """
        SELECT * FROM users
        WHERE id = %(id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return cls(result[0])
    @classmethod
    def update_user(cls,data):
        query = """
        UPDATE users
        SET first_name = %(first_name)s,last_name = %(last_name)s,email=%(email)s
        WHERE id=%(id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    @classmethod
    def delete_user(cls,data):
        query="""
        DELETE FROM users
        WHERE id = %(id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result