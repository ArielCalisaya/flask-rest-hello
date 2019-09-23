"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db
from family_datastructure import *
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/allMembers', methods=['GET'])
def family():
    if request.method == 'GET':
        filt = get_all_members()
        return jsonify(filt), 200


    else:
        return ERROR, 404


@app.route('/postMembers', methods=['POST'])
def addMember():
    if request.method == 'POST':
        addM = add_member()
        return jsonify(addM), 202



@app.route('/editMember', methods=['PUT'])
def edit():
    if request.method == 'PUT':
        edit = update_member()
        return jsonify(edit), 203
    else:
        return ERROR, 404

@app.route('/delMember', methods=['DELETE'])
def delete():
        if request.method == 'DELETE':
            supr = delete_member()
            return jsonnify(supr), 204


# this only runs if `$ python src/main.py` is exercuted
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT)
