from flask import Flask, jsonify, request
from flask_cors import CORS
from sqlite import creat_db, insert_db, delete_db, update_db
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


# f = open('books.json')
  
# data = json.load(f)

data = []

@app.route('/send_transacoes', methods=['GET', 'POST'])
def all_books():

    banco = creat_db()
    response_object = {}
    if request.method == 'POST':
        post_data = request.get_json()
        print(post_data)
        data.append({
            'id': uuid.uuid4().hex,
            'timestamp': post_data.get('timestamp'),
            'descricao': post_data.get('descricao'),
            'valor': post_data.get('valor'),
            'categoria': post_data.get('categoria')
        })
        insert_db(banco, data[-1]['id'], data[-1]['time_stamp'], data[-1]['descricao'], data[-1]['valor'], data[-1]['categoria'])
        banco.cursor.close()

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
def single_book(id):
    response_object = {'status': 'success'}

    #connect with db
    banco = creat_db()

    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(id)
        delete_db(id)
        data.append({
            'id': uuid.uuid4().hex,
            'time_stamp': post_data.get('time_stamp'),
            'descricao': post_data.get('descricao'),
            'valor': post_data.get('valor'),
            'categoria': post_data.get('categoria')
        })
        insert_db(banco, data[-1]['id'], data[-1]['time_stamp'], data[-1]['descricao'], data[-1]['valor'], data[-1]['categoria'])
        response_object['message'] = 'Transação atualizada!'
    if request.method == 'DELETE':
        remove_book(id)
        delete_db(banco, id)
        response_object['message'] = 'Transação removida!'

    banco.cursor.close()

    return jsonify(response_object)
    



if __name__ == '__main__':
    app.run()
