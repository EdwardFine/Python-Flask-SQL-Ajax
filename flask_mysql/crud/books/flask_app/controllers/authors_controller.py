from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.authors import Author
from flask_app.models.books import Book

@app.route('/authors')
def authors():
    return render_template('authors.html',authors = Author.get_all())

@app.route('/create_author',methods=["POST"])
def create_author():
    Author.create_author(request.form)
    return redirect('/authors')

@app.route('/display_authors_favorites/<int:author_id>')
def display_authors_favorites(author_id):
    return render_template('favorite_books.html', fav_books = Book.get_books_from_favorite_author({'id':author_id}),books = Book.get_books_not_in_author_favorite({'author_id':author_id}),author = Author.get_author_by_id({'id':author_id}))

@app.route('/process_add_author_favorite/<int:author_id>', methods=["POST"])
def add_author_favorites(author_id):
    Author.add_book_to_author_favorites({'author_id':author_id,'book_id':request.form['book_id']})
    return redirect(f'/display_authors_favorites/{author_id}')