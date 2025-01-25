from flask import Blueprint, request, jsonify
from .models import User
from .extensions import database


blueprint = Blueprint('api', __name__, url_prefix='/api')

@blueprint.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    if not data or not all(item in data for item in ("name", "birth_date")):
        return jsonify({"error": "Input not accepted"}), 400
    
    try:
        user = User(
            name=data['name'],
            birth_date=data['birth_date']
        )

        database.session.add(user)
        database.session.commit()

        return jsonify(user.to_dict()), 201
    except Exception as e:
        return jsonify({"Error ": str(e)}), 500


    

