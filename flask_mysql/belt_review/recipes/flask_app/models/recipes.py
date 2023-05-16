from flask import flash
from flask_app.config.mysqlconnections import connectToMySQL
from flask_app.models import user

class Recipe:
    DB = "recipe_schema"
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.under_30 = bool(data['under_30'])
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all_recipes_and_users(cls):
        query="""
        SELECT * FROM recipes
        LEFT JOIN users on users.id = recipes.user_id;
        """
        result = connectToMySQL(cls.DB).query_db(query)
        recipes = []
        for recipe in result:
            recipe_data = {
                'id':recipe['id'],
                'user_id':recipe['user_id'],
                'name':recipe['name'],
                'description':recipe['description'],
                'instruction':recipe['instruction'],
                'under_30':recipe['under_30'],
                'date_made':recipe['date_made'],
                'created_at':recipe['created_at'],
                'updated_at':recipe['updated_at'],
            }
            user_data={
                'id':recipe['users.id'],
                'first_name':recipe['first_name'],
                'last_name':recipe['last_name'],
                'email':recipe['email'],
                'created_at':recipe['users.created_at'],
                'updated_at':recipe['users.updated_at']
            }
            recipe_user = {'recipe':cls(recipe_data),'user':user.User(user_data)}
            recipes.append(recipe_user)
        return recipes
    
    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data['name'])<3:
            flash("Recipe Name Should be at Least 3 Letters.")
            is_valid = False
        if len(data['description'])<1:
            flash("Description is Needed.")
            is_valid = False
        if len(data['instruction']) <1:
            flash("Instructions Are Needed")
            is_valid = False
        if len(data['date_made']) < 10:
            flash("Date Made is Needed.")
            is_valid = False
        if 'under_30' not in data:
            flash("Under 30 Must be Selected.")
            is_valid = False
        return is_valid
    
    @classmethod
    def create_recipe(cls,data):
        query="""
        INSERT INTO recipes(name,user_id,description,instruction,date_made,under_30)
        VALUES (%(name)s,%(user_id)s,%(description)s,%(instruction)s,%(date_made)s,%(under_30)s);
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    
    @classmethod
    def get_recipe_by_id(cls,data):
        query="""
        SELECT * FROM recipes
        LEFT JOIN users on users.id = recipes.user_id
        WHERE recipes.id = %(id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        for recipe in result:
            recipe_data = {
                'id':recipe['id'],
                'user_id':recipe['user_id'],
                'name':recipe['name'],
                'description':recipe['description'],
                'instruction':recipe['instruction'],
                'under_30':recipe['under_30'],
                'date_made':recipe['date_made'],
                'created_at':recipe['created_at'],
                'updated_at':recipe['updated_at'],
            }
            user_data={
                'id':recipe['users.id'],
                'first_name':recipe['first_name'],
                'last_name':recipe['last_name'],
                'email':recipe['email'],
                'created_at':recipe['users.created_at'],
                'updated_at':recipe['users.updated_at']
            }
            recipe_user = {'recipe':cls(recipe_data),'user':user.User(user_data)}
        return recipe_user
    @classmethod
    def delete_recipe_by_id(cls,data):
        query="""
        DELETE FROM recipes
        WHERE recipes.id = %(id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    
    @classmethod
    def update_recipe(cls,data):
        query="""
        UPDATE recipes SET 
        name=%(name)s,description=%(description)s,
        instruction=%(instruction)s,date_made = %(date_made)s,
        under_30 = %(under_30)s
        WHERE recipes.id = %(id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result