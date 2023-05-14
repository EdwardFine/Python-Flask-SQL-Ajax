from flask_app.config.mysqlconnections import connectToMySQL
from flask_app.models import authors

class Book:
    DB = 'books_schema'
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query="SELECT * FROM books"
        results = connectToMySQL(cls.DB).query_db(query)
        books = []
        for book in results:
            books.append(cls(book))
        return books
    
    @classmethod
    def get_books_from_favorite_author(cls,data):
        query = """
            SELECT * FROM books
            LEFT JOIN favorites on favorites.book_id = books.id
            LEFT JOIN authors on authors.id = favorites.author_id
            WHERE authors.id = %(id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query,data)
        print(results)
        books_fav = []
        for book in results:
            book_data = {
                'id':book['id'],
                'title':book['title'],
                'num_of_pages':book['num_of_pages'],
                'created_at':book['authors.created_at'],
                'updated_at':book['authors.updated_at']
            }
            books_fav.append(cls(book_data))
        return books_fav
    
    @classmethod
    def create_book(cls,data):
        query="""
        INSERT INTO books(title,num_of_pages)
        VALUES (%(title)s,%(num_of_pages)s);
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    
    @classmethod
    def get_book_by_id(cls,data):
        query="""
        SELECT * FROM books
        WHERE books.id = %(id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result[0]
    
    @classmethod
    def add_author_to_book_favorites(cls,data):
        query="""
        INSERT INTO favorites(book_id,author_id)
        VALUES(%(book_id)s,%(author_id)s);
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    
    @classmethod
    def get_books_not_in_author_favorite(cls,data):
        query="""
        SELECT DISTINCT books.id,books.title,books.num_of_pages,books.created_at,books.updated_at FROM books
        LEFT JOIN favorites ON books.id = favorites.book_id
        LEFT JOIN authors ON authors.id = favorites.author_id
        WHERE books.id NOT IN
        (SELECT books.id FROM books
        LEFT JOIN favorites ON books.id = favorites.book_id
        LEFT JOIN authors ON authors.id = favorites.author_id
        WHERE authors.id = %(author_id)s) ;
        """
        results = connectToMySQL(cls.DB).query_db(query,data)
        books = []
        for book in results:
            books.append(cls(book))
        return books