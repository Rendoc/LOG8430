from flask import Flask, jsonify, abort, request
import db_driver

app = Flask(__name__)

factures = [
    {
        'id': 0,
        'title': 'IGA',
        'articles': [
            {
                'id': 0,
                'name': 'pain',
                'prix': 5.99
            },
            {
                'id': 1,
                'name': 'mtn dew',
                'prix': 7.99
            },
            {
                'id': 2,
                'name': 'lait',
                'prix': 2.99
            }
        ]
    },
    {
        'id': 1,
        'title': 'Jean-Coutu',
        'articles': [
            {
                'id': 0,
                'name': 'tylenol',
                'prix': 12.99
            }
        ]
    }
]


@app.route('/')
def index():
    facture = {
        'id': 1,
        'title': 'Jean-Coutu',
        'articles': [
            {
                'id': 0,
                'name': 'tylenol',
                'prix': 12.99
            }
        ]
    }
    db_driver.add_facture(facture)
    return "Hello, World!"


@app.route('/get/')
def get():
    return db_driver.get_factures()


@app.route('/factures/')
def get_factures():
    return jsonify({'factures': factures})


@app.route('/factures/<int:facture_id>', methods=['GET'])
def get_facture(facture_id):
    facture = [
        facture for facture in factures if facture['id'] == facture_id]
    if len(factures) == 0:
        abort(404)
    return jsonify({'factures': facture[0]})


@app.route('/factures/', methods=['POST'])
def create_facture():
    if not request.json or not 'title' in request.json:
        abort(400)
    facture = {
        'id': factures[-1]['id'] + 1,
        'title': request.json['title'],
        'articles': request.json.get('articles')
    }
    factures.append(facture)
    return jsonify({'facture': facture}), 201


if __name__ == '__main__':
    db_driver.main()
    app.run(debug=True)
