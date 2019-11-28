from flask import Blueprint, request, jsonify, g
from notifier.db import get_db

api = Blueprint('notifier',__name__, url_prefix='/notifier')

@api.route('/prueba', methods=['GET'])
def prueba():
    return jsonify({'message': 'El blueprint funca'})

@api.route('/subscribe', methods=['POST'])
def subscribe():
    # recibir el json de la petición
    data = request.get_json()
    db=get_db()

    # validar que todos los campos tienen valores
    if data is None:
        return jsonify({'message': 'JSON not found'})

    if not data.items():
        return jsonify({'message': 'JSON not found'})

    for key, value in data.items():
            if not value:
                return jsonify({'message': 'value for {} is empty'.format(key)})

    id_line = data['id_line']
    email = data['email']
    
    db.subscribe(id_line, email)
    print (db)
    return jsonify({'message': 'Email was subscribed succesfully'})

@api.route('/email', methods=['GET'])
def email():
    db = get_db()
    print(db)
    return str(db)

@api.route('/unsubscribe', methods=['DELETE'])
def unsubscribe():
    # recibir el json de la petición
    data = request.get_json()
    db=get_db()

    # validar que todos los campos tienen valores
    if data is None:
        return jsonify({'message': 'JSON not found'})
        
    if not data.items():
        return jsonify({'message': 'JSON not found'})

    for key, value in data.items():
            if not value:
                return jsonify({'message': 'value for {} is empty'.format(key)})

    id_line = data['id_line']
    email = data['email']
    
    db.unsubscribe(id_line, email)
    print (db)
    return jsonify({'message': 'Email was deleted '})