from flask import Blueprint, request, jsonify, g
from monitor.db import get_monitor

api = Blueprint('monitor',__name__, url_prefix='/monitor')

@api.route('/status', methods=['GET'])
def get_status():
    monitor = get_monitor()
    data = monitor.get_services_status()

    return data, 200

@api.route('/status/service', methods=['GET'])
def get_status_of_a_service( ):
    # recibir el json de la petición
    data = request.get_json()
    monitor=get_monitor()

    # validar que todos los campos tienen valores
    if data is None:
        return jsonify({'message': 'JSON not found'}), 400

    if not data.items():
        return jsonify({'message': 'JSON not found'}), 400

    for key, value in data.items():
            if not value:
                return jsonify({'message': 'value for {} is empty'.format(key)}), 400 

    monitor = get_monitor()
    service = data['service']
    result = monitor.get_service_status(service)
    return result, 200

@api.route('/status/types', methods=['GET'])
def get_status_types():
    monitor = get_monitor()
    result = monitor.get_status_types()
    return result, 200

@api.route('/services', methods=['GET'])
def get_services():
    monitor = get_monitor()
    data = monitor.get_services_names()
    result = {}
    result['services'] = data
    return result, 200

@api.route('/downtime/record', methods=['GET'])
def get_downtimes_of_a_service():
    # recibir el json de la petición
    data = request.get_json()
    monitor = get_monitor()

    # validar que todos los campos tienen valores
    if data is None:
        return jsonify({'message': 'JSON not found'}), 400

    if not data.items():
        return jsonify({'message': 'JSON not found'}), 400

    for key, value in data.items():
            if not value:
                return jsonify({'message': 'value for {} is empty'.format(key)}), 400 

    monitor = get_monitor()
    service = data['service']
    result = monitor.get_downtime_record(service)
    return result, 200

@api.route('/downtime', methods=['GET'])
def get_downtime():
    # recibir el json de la petición
    data = request.get_json()
    monitor = get_monitor()

    # validar que todos los campos tienen valores
    if data is None:
        return jsonify({'message': 'JSON not found'}), 400

    if not data.items():
        return jsonify({'message': 'JSON not found'}), 400

    for key, value in data.items():
            if not value:
                return jsonify({'message': 'value for {} is empty'.format(key)}), 400 

    monitor = get_monitor()
    id = data['id']
    result = monitor.get_downtime(id)
    return result, 200

@api.route('/downtime', methods=['DELETE'])
def delete_downtime():
    # recibir el json de la petición
    data = request.get_json()
    monitor = get_monitor()

    # validar que todos los campos tienen valores
    if data is None:
        return jsonify({'message': 'JSON not found'}), 400

    if not data.items():
        return jsonify({'message': 'JSON not found'}), 400

    for key, value in data.items():
            if not value:
                return jsonify({'message': 'value for {} is empty'.format(key)}), 400 

    monitor = get_monitor()
    id = data['id']
    try:
        result = monitor.delete_downtime(id)
        return jsonify({'message': 'Downtime was deleted '}), 200
    except ValueError:
        return jsonify({'message': 'the id {} does not exist'.format(id)}), 404
