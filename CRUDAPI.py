#  AFZAL KHAN
# Email -      afzalkhan01765835454@gamil.com
from flask import  Flask , jsonify , request

app = Flask (__name__)

books = [
    {"id":1 , "title":"Book1" , "author":"author1"},
    {"id":2 , "title":"Book2" , "author":"author2"},
    {"id":3 , "title":"Book3" , "author":"author3"}
    ]

@app.route('/books',methods = ['GET'])

def get_books():
    return books

@app.route('/books/<int:book_id>', methods=['GET'])

# get a specific  book by book id

def get_book(book_id):

    for book in books:
        if book['id'] == book_id:

            return book

    return ('Error : Book not found')

#create new book
@app.route('/books',methods=['POST'])

def create_new_book():

    new_book = {'id':len(books)+1,'title':request.json['title'],'author':request.json['author']}
    books.append(new_book)

    return books

#update a book

@app.route('/books/<int:book_id>',methods = ['PUT'])

def update_book(book_id):

    for book in books:
        if book['id'] == book_id:
            book["title"] = request.json["title"]
            book["author"] = request.json["author"]
            return  books

    return("Error :This book is not found")

#delete a book

#@app.route('/books/<int:book_id>',methods=['DELETE'])
'''
def Delete_a_book(book_id):
    for book in books:
        if book['id'] == book_id:

           # books = [book for book in books if book['id'] != book_id]

            return  "the book delete successfully"

    return "This book not found"'''


@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_a_book(book_id):
    global books  # Declare 'books' as global to modify it
    for book in books:
        if book['id'] == book_id:
            books = [b for b in books if b['id'] != book_id]  # Create a new list excluding the book
            return jsonify({"message": "The book was deleted successfully"}), 200
    return jsonify({"error": "This book was not found"}), 404




if __name__ =="__main__":

    app.run(debug=True)



