from flask import Flask, jsonify, request

app = Flask(__name__)

books = {
    1: {"title": "Distributed Systems", "author": "Tanenbaum", "price": 50.0},
    2: {"title": "Clean Code", "author": "Robert C. Martin", "price": 45.0}
}


@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = books.get(book_id)
    if book:
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    if not data or 'title' not in data or 'author' not in data or 'price' not in data:
        return jsonify({"error": "Invalid data"}), 400

    new_id = max(books.keys()) + 1 if books else 1
    books[new_id] = {
        "title": data['title'],
        "author": data['author'],
        "price": float(data['price'])
    }
    return jsonify({"message": "Book added", "id": new_id}), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    if book_id not in books:
        return jsonify({"error": "Book not found"}), 404

    books[book_id].update({
        "title": data.get("title", books[book_id]["title"]),
        "author": data.get("author", books[book_id]["author"]),
        "price": float(data.get("price", books[book_id]["price"]))
    })
    return jsonify({"message": "Book updated", "id": book_id})

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    if book_id in books:
        del books[book_id]
        return jsonify({"message": "Book deleted"})
    return jsonify({"error": "Book not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
