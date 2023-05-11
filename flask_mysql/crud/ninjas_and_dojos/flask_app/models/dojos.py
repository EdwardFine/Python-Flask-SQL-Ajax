from flask_app.config.mysqlconnections import connectToMySQL
from flask_app.models.ninjas import Ninja

class Dojo:
    DB = "dojos_and_ninjas_schema"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.all_ninjas = []
    @classmethod
    def create_dojo(cls,data):
        query="""
        INSERT INTO dojos(name)
        VALUES (%(name)s);
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    @classmethod
    def get_all(cls):
        query="SELECT * FROM dojos"
        results = connectToMySQL(cls.DB).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    @classmethod
    def get_one_dojo(cls,data):
        query = """
        SELECT * FROM dojos
        LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id
        WHERE dojos.id = %(id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        one_dojo = cls(result[0])
        for row in result:
            ninjas_data = {    
            'id':row['ninjas.id'],
            'first_name':row['first_name'],
            'last_name':row['last_name'],
            'age':row['age'],
            'created_at':row['ninjas.created_at'],
            'updated_at':row['ninjas.updated_at']
            }
            one_dojo.all_ninjas.append(Ninja(ninjas_data))
        return one_dojo
    @classmethod
    def update_dojo(cls,data):
        query = """
        UPDATE dojos
        SET name = %(name)s
        WHERE id=%(id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    @classmethod
    def delete_dojo(cls,data):
        query="""
        DELETE FROM dojos
        WHERE id = %(id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result