from flask_app.config.mysqlconnections import connectToMySQL
from flask import flash

class Friend:
    DB = "friendships_schema"
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.friends = []
    
    @classmethod
    def get_all_users(cls):
        query="SELECT * FROM users;"
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
    
    @classmethod
    def create_user(cls,data):
        query="""
        INSERT INTO users(first_name,last_name)
        VALUES (%(first_name)s,%(last_name)s);
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    
    @classmethod
    def get_user_by_id(cls,data):
        query="""
        SELECT * FROM users
        WHERE users.id = %(id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return cls(result[0])
    
    @classmethod
    def get_friends_of_id(cls,data):
        query="""
        SELECT * FROM users
        LEFT JOIN friendships ON users.id = friendships.user_id
        LEFT JOIN users AS friends ON friendships.friend_id = friends.id
        WHERE users.id = %(id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        friends = []
        for case in result:
            friend_data = {
                'id':case['friends.id'],
                'first_name':case['friends.first_name'],
                'last_name':case['friends.last_name'],
                'created_at':case['friends.created_at'],
                'updated_at':case['friends.updated_at']
            }
            friends.append(cls(friend_data))
        return friends
    
    @staticmethod
    def check_friendship(user,friend):
        is_valid = True
        if user.id == friend.id:
            flash("User cannot be friends with themself.")
            is_valid = False
        users_friends = Friend.get_friends_of_id({'id':user.id})
        for case in users_friends:
            if friend.id == case.id:
                flash("Users are already Friends")
                is_valid = False
                break
        return is_valid
    
    @classmethod
    def get_all_friends(cls):
        query="""
        SELECT * FROM users
        LEFT JOIN friendships ON users.id = friendships.user_id
        JOIN users AS friends ON friendships.friend_id = friends.id
        ORDER BY users.id;
        """
        result = connectToMySQL(cls.DB).query_db(query)
        friends = []
        for case in result:
            user_data = {
                'id':case['id'],
                'first_name':case['first_name'],
                'last_name':case['last_name'],
                'created_at':case['created_at'],
                'updated_at':case['updated_at']
            }
            friend_data = {
                'id':case['friends.id'],
                'first_name':case['friends.first_name'],
                'last_name':case['friends.last_name'],
                'created_at':case['friends.created_at'],
                'updated_at':case['friends.updated_at']
            }
            relationship = {'user':cls(user_data),'friend':cls(friend_data)}
            friends.append(relationship)
        return friends
    
    @classmethod
    def create_relationship(cls,user,friend):
        query=f"INSERT INTO friendships(user_id,friend_id)VALUES({user.id},{friend.id})"
        result = connectToMySQL(cls.DB).query_db(query)
        return result