from flask import Blueprint, request, jsonify, g
from notifier.db import get_db

api = Blueprint('notifier',__name__, url_prefix='/notifier')

@api.route('/prueba', methods=['GET'])
def prueba():
    return jsonify({'message': 'El blueprint funca'})

@api.route('/email', methods=['POST'])
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

@api.route('/email', methods=['PUT'])
def update():
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
    old_email = data['old_email']
    new_email = data['new_email']

    db.unsubscribe(id_line, old_email)
    db.subscribe(id_line, new_email)

    return jsonify({'message': 'Email was updated succesfully'})

# Devuelve un json con las suscripciones en las que se encuentra un email
@api.route('/email', methods=['GET'])
def email():
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

    email = data['email']

    try:
        lines=db.subscriptions(email)
        print("lo que devuelve db.subscriptions")
        print(lines)
        return jsonify(id_lines=lines)
    except ValueError:
        return jsonify({'message': 'not subscriptions for email {}'.format(email)})
    

@api.route('/email', methods=['DELETE'])
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