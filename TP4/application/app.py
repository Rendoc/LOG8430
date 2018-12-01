from flask import Flask, jsonify, abort, request
import db_driver
import json

app = Flask(__name__)


@app.route('/factures/')
def get():
    return jsonify({'factures': db_driver.get_factures()})


@app.route('/factures/<int:facture_id>', methods=['GET'])
def get_facture(facture_id):
    factures = db_driver.get_facture(facture_id)
    if len(factures) == 0:
        abort(404)
    return jsonify({'facture': json.loads(factures)})


@app.route('/factures/', methods=['POST'])
def create_facture():
    if not request.json or not 'title' in request.json:
        abort(400)
    factures = json.loads(db_driver.get_factures())
    facture = {
        'id': len(factures),
        'title': request.json['title'],
        'articles': request.json['articles']
    }
    db_driver.add_facture(facture)
    return jsonify({'facture': facture}), 201


if __name__ == '__main__':
    # db_driver.main()
    app.run(debug=True)
