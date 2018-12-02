from flask import Flask, jsonify, abort, request, url_for
import db_driver
import json
import spark_driver

app = Flask(__name__)


@app.route('/factures/')
def get():
    return jsonify({'factures': json.loads(db_driver.get_factures())})


@app.route('/most/', methods=['GET'])
def get_most_frequent_product():
    res = spark_driver.get_most()
    return jsonify({"most": res})


@app.route('/factures/', methods=['POST'])
def create_facture():
    if not request.json:
        abort(400)
    res = db_driver.add_facture(request.json)
    print("return : "+str(res))
    return jsonify({'facture': str(res)}), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
