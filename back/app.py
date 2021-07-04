from flask import Flask, jsonify, request
from flask_cors import CORS
from sqlite import creat_db, write_json
import json
import uuid
from uuid import UUID
from uuid import uuid4


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

#connect with db and get json
banco = creat_db()
write_json(banco)

# f = open('books.json')
  
# data = json.load(f)

data = []

@app.route('/send_transacoes', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        data.append({
            'id': uuid.uuid4().hex,
            'time_stamp': post_data.get('time_stamp'),
            'descricao': post_data.get('descricao'),
            'valor': post_data.get('valor'),
            'categoria': post_data.get('categoria')
        })
        response_object['message'] = 'Data added!'
    else:
        response_object['data'] = data
    return jsonify(response_object)


# @app.route('/send_transacoes/<transaction_id>', methods=['PUT'])
# def single_book(book_id):
#     response_object = {'status': 'success'}
#     if request.method == 'PUT':
#         post_data = request.get_json()
#         remove_book(book_id)
#         data.append({
#             'id': uuid.uuid4().hex,
#             'title': post_data.get('title'),
#             'author': post_data.get('author'),
#             'read': post_data.get('read')
#         })
#         response_object['message'] = 'Book updated!'
#     return jsonify(response_object)


def remove_book(book_id):
    for book in data:
        if book['id'] == book_id:
            data.remove(book)
            return True
    return False


@app.route('/send_transacoes/<transaction_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        data.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)
    



if __name__ == '__main__':
    app.run()
