from flask import Flask, jsonify
from flask_cors import CORS
from sqlite import creat_db, write_json


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

# sanity check route
@app.route('/send_transacoes', methods=['GET'])
def send():
    return jsonify(data.json)


if __name__ == '__main__':
    app.run()
