import pytest
import json

import sys
sys.path.append('monitor')
import monitor
from monitor.db import get_monitor
from monitor.db import init_monitor

# Tearup de la aplicación, se usará en cada test
@pytest.fixture(scope='session')
def app():
    app = monitor.create_app({'TESTING': True})

    with app.app_context():
        init_monitor()
    yield app

@pytest.fixture(scope='session')
def client(app):
    return app.test_client()

def test_get_status(client):
    response = client.get('/monitor/status')
    assert '200 OK' == response.status

def test_get_status_of_a_service(client):
    # Comprobar que al hacer la petición devuelve el código correcto
    response = client.get('/monitor/status/service',
                data= json.dumps({"service": "GitHub Actions"}),
                content_type='application/json')

    assert '200 OK' == response.status

    # Comprobar que cuando falta algún elemento del JSON devuelve el código correcto
    response = client.get('/monitor/status/service', 
                data=json.dumps({"service": ""}), 
                content_type='application/json')

    assert '400 BAD REQUEST' == response.status

    # Comprobar que cuando no se recibe nada se devuelve el código correcto
    response = client.get('/monitor/status/service', 
                data="", 
                content_type='application/json')

    assert '400 BAD REQUEST' == response.status

    # Comprobar que cuando se recibe un JSON vacío se devuelve el código correcto
    response = client.get('/monitor/status/service', 
                data=json.dumps({}), 
                content_type='application/json')

    assert '400 BAD REQUEST' == response.status

def test_get_status_types(client):
    response = client.get('/monitor/status/types')
    assert '200 OK' == response.status

def test_get_services(client):
    response = client.get('/monitor/services')
    assert '200 OK' == response.status

def test_get_downtimes_of_a_service(client):
    # Comprobar que al hacer la petición devuelve el código correcto
    response = client.get('/monitor/downtime/record',
                data= json.dumps({"service": "GitHub Actions"}),
                content_type='application/json')

    assert '200 OK' == response.status

    # Comprobar que cuando falta algún elemento del JSON devuelve el código correcto
    response = client.get('/monitor/downtime/record', 
                data=json.dumps({"service": ""}), 
                content_type='application/json')

    assert '400 BAD REQUEST' == response.status

    # Comprobar que cuando no se recibe nada se devuelve el código correcto
    response = client.get('/monitor/downtime/record', 
                data="", 
                content_type='application/json')

    assert '400 BAD REQUEST' == response.status

    # Comprobar que cuando se recibe un JSON vacío se devuelve el código correcto
    response = client.get('/monitor/downtime/record', 
                data=json.dumps({}), 
                content_type='application/json')

    assert '400 BAD REQUEST' == response.status

def test_get_downtime(client):
    # Comprobar que al hacer la petición devuelve el código correcto
    response = client.get('/monitor/downtime',
                data= json.dumps({"id": 1}),
                content_type='application/json')

    assert '200 OK' == response.status

    # Comprobar que cuando falta algún elemento del JSON devuelve el código correcto
    response = client.get('/monitor/downtime', 
                data=json.dumps({"id": ""}), 
                content_type='application/json')

    assert '400 BAD REQUEST' == response.status

    # Comprobar que cuando no se recibe nada se devuelve el código correcto
    response = client.get('/monitor/downtime', 
                data="", 
                content_type='application/json')

    assert '400 BAD REQUEST' == response.status

    # Comprobar que cuando se recibe un JSON vacío se devuelve el código correcto
    response = client.get('/monitor/downtime', 
                data=json.dumps({}), 
                content_type='application/json')

    assert '400 BAD REQUEST' == response.status

def test_delete_downtime(client):
    # Comprobar que al hacer la petición devuelve el código correcto
    response = client.delete('/monitor/downtime',
                data= json.dumps({"id": 1}),
                content_type='application/json')

    assert '404 NOT FOUND' == response.status

    # Comprobar que cuando falta algún elemento del JSON devuelve el código correcto
    response = client.delete('/monitor/downtime', 
                data=json.dumps({"id": ""}), 
                content_type='application/json')

    assert '400 BAD REQUEST' == response.status

    # Comprobar que cuando no se recibe nada se devuelve el código correcto
    response = client.delete('/monitor/downtime', 
                data="", 
                content_type='application/json')

    assert '400 BAD REQUEST' == response.status

    # Comprobar que cuando se recibe un JSON vacío se devuelve el código correcto
    response = client.delete('/monitor/downtime', 
                data=json.dumps({}), 
                content_type='application/json')

    assert '400 BAD REQUEST' == response.status
