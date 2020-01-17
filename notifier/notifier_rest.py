from flask import Blueprint, request, jsonify, g
from notifier.db import get_notifier

# 400 Bad Request
# 403 Forbidden
# 200 OK

# Ruta por la que se va a acceder al Blueprint
api = Blueprint('notifier',__name__, url_prefix='/notifier')

# Prueba para comprobar la conexión
@api.route('/prueba', methods=['GET'])
def prueba():
    return jsonify({'message': 'El blueprint funca'})


@api.route('/email', methods=['POST'])
def subscribe():
    """Susbscribe un emaol a una lista
    Recibe un json con la lista y el email"""
    # recibir el json de la petición
    data = request.get_json()
    notifier=get_notifier()

    # validar que todos los campos tienen valores
    if data is None:
        return jsonify({'message': 'JSON not found'}), 400

    if not data.items():
        return jsonify({'message': 'JSON not found'}), 400

    for key, value in data.items():
        if not value:
            return jsonify({'message': 'value for {} is empty'.format(key)}), 400

    id_line = data['id_line']
    email = data['email']
    
    try :
        notifier.subscribe(id_line, email)
        print (notifier)
        return jsonify({'message': 'Email was subscribed succesfully'}), 200
    except NameError:
        return jsonify({'message': 'Email has already been subscribed'}), 403


@api.route('/email', methods=['PUT'])
def update():
    """Actualiza un email de una lista
    Recibe el email antiguo, el nuevo y la lista en la que se encuentra"""
    # recibir el json de la petición
    data = request.get_json()
    notifier=get_notifier()

    # validar que todos los campos tienen valores
    if data is None:
        return jsonify({'message': 'JSON not found'}), 400

    if not data.items():
        return jsonify({'message': 'JSON not found'}), 400

    for key, value in data.items():
            if not value:
                return jsonify({'message': 'value for {} is empty'.format(key)}), 400

    id_line = data['id_line']
    old_email = data['old_email']
    new_email = data['new_email']

    try:
        notifier.update(id_line, old_email, new_email)
        return jsonify({'message': 'Email was updated succesfully'}), 200
    except ValueError:
        return jsonify({'message': 'old_email argument does not exist or new_email already exists'}), 403


# Devuelve un json con las suscripciones en las que se encuentra un email
@api.route('/email', methods=['GET'])
def email():
    """Devuelve un mensaje con las lista en las que se encuentra un email suscripto"""
    # recibir el json de la petición
    data = request.get_json()
    notifier=get_notifier()

    # validar que todos los campos tienen valores
    if data is None:
        return jsonify({'message': 'JSON not found'}), 400

    if not data.items():
        return jsonify({'message': 'JSON not found'}), 400

    for key, value in data.items():
            if not value:
                return jsonify({'message': 'value for {} is empty'.format(key)}), 400

    email = data['email']

    try:
        lines=notifier.subscriptions(email)
        return jsonify(lines), 200
    except ValueError:
        return jsonify({'message': 'not subscriptions for email {}'.format(email)}), 404
    

@api.route('/email', methods=['DELETE'])
def unsubscribe():
    """Elimina un email de una lista
    Recibe un json con el email y la lista en la que se encuentra"""
    # recibir el json de la petición
    data = request.get_json()
    notifier=get_notifier()

    # validar que todos los campos tienen valores
    if data is None:
        return jsonify({'message': 'JSON not found'}), 400
        
    if not data.items():
        return jsonify({'message': 'JSON not found'}), 400

    for key, value in data.items():
            if not value:
                return jsonify({'message': 'value for {} is empty'.format(key)}), 400

    id_line = data['id_line']
    email = data['email']
    
    notifier.unsubscribe(id_line, email)
    return jsonify({'message': 'Email was deleted '}), 200