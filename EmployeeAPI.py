

from flask import Flask, request
app = Flask(__name__)

books =[{"id":1 ,"title":"Book1","author":"author1"},
        {"id":2 ,"title":"Book2","author":"author2"},
        {"id":3,"title":"Book3","author":"author3"},
        ]

@app.route("/books",methods = ["GET"])

def get_books():
    return  books

@app.route("/books/<int:book_id>",methods = ["GET"])

def get_book(book_id):

    for book in books:
        if book['id'] == book_id:
            return book

    return  "This book not Found"

@app.route("/books/<int:book_id>",methods = ["POST"])
#Create new book
def create_new_book():
    #new_book = {'id': len(books) + 1, 'title': request.json['title'], 'author': request.json['author']}
    new_book = {"id":len(books)+1 , "title":request.json["title"],"author":request.json['author']}
    books.append(new_book)
    return books

#update book list by update the book

@app.route("/books/<int:book_id>",methods =["PUT"])
def update_book(book_id):
    for book in books:
        if book['id'] == book_id:
            book["title"] = request.json["title"]
            book["author"] = request.json["author"]
            return books

    return "Error:This book is not found"

#Delete book
@app.route("/books/<int:book_id>",methods = ["DELETE"])

def delete_book(book_id):
    global  books.



    for book in books:
        if book['id'] == book_id:
            books = [b for b in books if b['id'] != book_id]
            return  "The book is deleted successfully"
@app.route("/uploadbook",methods =["POST"])

def upload_book():
    import os
    upload_file = request.files["file"]
    destination = os.path("uploads/",upload_file.filename)

    upload_file.save(destination)
    return {"Data:file uploaded successfully"}


if __name__ =="__main__":
    app.run(debug=True)





