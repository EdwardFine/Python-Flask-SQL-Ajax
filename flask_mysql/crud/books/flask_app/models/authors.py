from flask_app.config.mysqlconnections import connectToMySQL
from flask_app.models import books

class Author:
    DB = 'books_schema'
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query="SELECT * FROM authors"
        results = connectToMySQL(cls.DB).query_db(query)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors
    
    @classmethod
    def create_author(cls,data):
        query="""
        INSERT INTO authors(name)
        VALUES (%(name)s);
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    
    @classmethod
    def get_authors_not_in_book_favorite(cls,data):
        query="""
        SELECT DISTINCT authors.id, authors.name,authors.created_at,authors.updated_at FROM authors
        LEFT JOIN favorites ON authors.id = favorites.author_id
        LEFT JOIN books ON books.id = favorites.book_id
        WHERE authors.id NOT IN
        (SELECT authors.id FROM authors
        LEFT JOIN favorites ON authors.id = favorites.author_id
        LEFT JOIN books ON books.id = favorites.book_id
        WHERE books.id = %(book_id)s) ;
        """
        results = connectToMySQL(cls.DB).query_db(query,data)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors
    
    @classmethod
    def get_authors_from_favorite_books(cls,data):
        query = """
            SELECT * FROM books
            LEFT JOIN favorites on favorites.book_id = books.id
            LEFT JOIN authors on authors.id = favorites.author_id
            WHERE books.id = %(id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query,data)
        print(results)
        authors_fav = []
        for author in results:
            author_data = {
                'id':author['authors.id'],
                'name':author['name'],
                'created_at':author['authors.created_at'],
                'updated_at':author['authors.updated_at']
            }
            authors_fav.append(cls(author_data))
        return authors_fav
    
    @classmethod
    def get_author_by_id(cls,data):
        query="""
        SELECT * FROM authors
        WHERE authors.id = %(id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result[0]
    
    @classmethod
    def add_book_to_author_favorites(cls,data):
        query="""
        INSERT INTO favorites(book_id,author_id)
        VALUES(%(book_id)s,%(author_id)s);
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result