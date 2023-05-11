from flask_app.config.mysqlconnections import connectToMySQL

class Ninja:
    DB = "dojos_and_ninjas_schema"
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = ""
    
    @classmethod
    def create_ninja(cls,data):
        query="""
        INSERT INTO ninjas(first_name,last_name,age, dojo_id)
        VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    @classmethod
    def get_all(cls):
        query="SELECT * FROM ninjas"
        results = connectToMySQL(cls.DB).query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas
    @classmethod
    def get_one_ninja(cls,data):
        query="""
        SELECT * FROM ninjas
        JOIN dojos ON dojos.id = ninjas.dojo_id
        WHERE ninjas.id = %(id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        one_ninja = cls(result[0])
        one_ninja.dojo_id=result[0]['dojos.id']
        return one_ninja
    @classmethod
    def update_ninja(cls,data):
        query = """
        UPDATE ninjas
        SET first_name = %(first_name)s,last_name = %(last_name)s,age=%(age)s,dojo_id = %(dojo_id)s
        WHERE id=%(id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    @classmethod
    def delete_ninja(cls,data):
        query="""
        DELETE FROM ninjas
        WHERE id = %(id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result