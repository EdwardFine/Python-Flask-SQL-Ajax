from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.books import Book
from flask_app.models.authors import Author

@app.route('/')
def home():
    return redirect('/books')

@app.route('/books')
def books():
    return render_template('books.html',books = Book.get_all())

@app.route('/create_book',methods=["POST"])
def create_books():
    Book.create_book(request.form)
    return redirect('/books')

@app.route('/display_books_favorites/<int:book_id>')
def display_books_favorites(book_id):
    return render_template('favorite_authors.html', fav_authors = Author.get_authors_from_favorite_books({'id':book_id}),authors = Author.get_authors_not_in_book_favorite({'book_id':book_id}),book = Book.get_book_by_id({'id':book_id}))

@app.route('/process_add_book_favorite/<int:book_id>', methods=["POST"])
def add_book_favorites(book_id):
    Book.add_author_to_book_favorites({'book_id':book_id,'author_id':request.form['author_id']})
    return redirect(f'/display_books_favorites/{book_id}')