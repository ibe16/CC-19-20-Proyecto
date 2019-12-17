import pytest
import json

import sys
sys.path.append('notifier')
import notifier
from notifier.db import get_db
from notifier.db import init_db


# Tearup de la aplicación, se usará en cada test
@pytest.fixture(scope='session')
def app():
    app = notifier.create_app({'TESTING': True})

    with app.app_context():
        init_db()
    yield app

@pytest.fixture(scope='session')
def client(app):
    return app.test_client()

# Comprobar que todas las peticiones funcionan
def test_hello(client):
    response = client.get('/hello')
    assert b'Hello, World!' == response.data

# Testea POST: /notifier/email
def test_subscribe(client):
    # Comprobar que al hacer la petición devuelve el mensaje correcto
    response = client.post("/notifier/email", 
                data=json.dumps({ "id_line":"1","email":"irene@email.com"}), 
                content_type='application/json')
    assert b'"message": "Email was subscribed succesfully"' in response.data

    # Comprobar que cuando falta algún elemento del JSON devuelve el mensaje correcto
    response = client.post("/notifier/email", 
                data=json.dumps({ "id_line":"","email":"irene@email.com"}), 
                content_type='application/json')
    assert b'empty' in response.data

    # Comprobar que cuando no se recibe nada se devuelve el mensaje correcto
    response = client.post("/notifier/email", 
                data="")
    assert b'JSON not found' in response.data

    # Comprobar que cuando se recibe un JSON vacío se devuelve el mensaje correcto
    response = client.post("/notifier/email", 
                data=json.dumps({}), 
                content_type='application/json')
    assert b'JSON not found' in response.data

# Testea GET: /notifier/email
def test_email(client):
    # Comprobar que al hacer la petición devuelve el mensaje correcto
    response = client.get('/notifier/email',
                data=json.dumps({ "email":"irene@email.com"}),
                content_type='application/json')
    print(response.data)
    assert b'{\n  "id_lines": [\n    "1"\n  ]\n}\n' in response.data

    # Comprobar que cuando falta algún elemento del JSON devuelve el mensaje correcto
    response = client.get('/notifier/email',
                data=json.dumps({ "email":""}),
                content_type='application/json')
    print(response.data)
    assert b'empty' in response.data

    # Comprobar que cuando no se recibe nada se devuelve el mensaje correcto
    response = client.get('/notifier/email',
                data="")
    print(response.data)
    assert b'JSON not found' in response.data

    # Comprobar que cuando se recibe un JSON vacío se devuelve el mensaje correcto
    response = client.get('/notifier/email',
                data=json.dumps({}),
                content_type='application/json')
    print(response.data)
    assert b'JSON not found' in response.data

# Testea DELETE: /notifier/email
def test_unsubcsribe(client):
    # Comprobar que al hacer la petición devuelve el mensaje correcto
    response = client.delete("/notifier/email", 
                data=json.dumps({ "id_line":"1","email":"irene@email.com"}), 
                content_type='application/json')
    assert b'"message": "Email was deleted "' in response.data

    # Comprobar que cuando falta algún elemento del JSON devuelve el mensaje correcto
    response = client.delete("/notifier/email", 
                data=json.dumps({ "id_line":"","email":"irene@email.com"}), 
                content_type='application/json')
    assert b'empty' in response.data    

    # Comprobar que cuando no se recibe nada se devuelve el mensaje correcto
    response = client.delete("/notifier/email", 
                data="")
    assert b'JSON not found' in response.data

    # Comprobar que cuando se recibe un JSON vacío se devuelve el mensaje correcto
    response = client.delete("/notifier/email", 
                data=json.dumps({}), 
                content_type='application/json')
    assert b'JSON not found' in response.data    

# Testea PUT: /notifier/email
def test_update(client):
    # Metemos un email
    response = client.post("/notifier/email", 
                data=json.dumps({ "id_line":"1","email":"irene@email.com"}), 
                content_type='application/json')

    # Comprobar que al hacer la petición devuelve el mensaje correcto
    response = client.put("/notifier/email", 
                data=json.dumps({ "id_line":"1", "old_email":"irene@email.com", "new_email":"test@correo.com"}), 
                content_type='application/json')
    assert b'"message": "Email was updated succesfully"' in response.data

    # Comprobar que cuando falta algún elemento del JSON devuelve el mensaje correcto
    response = client.put("/notifier/email", 
                data=json.dumps({ "id_line":"","old_email":"irene@email.com", "new_email":""}), 
                content_type='application/json')
    assert b'empty' in response.data    

    # Comprobar que cuando no se recibe nada se devuelve el mensaje correcto
    response = client.put("/notifier/email", 
                data="")
    assert b'JSON not found' in response.data

    # Comprobar que cuando se recibe un JSON vacío se devuelve el mensaje correcto
    response = client.put("/notifier/email", 
                data=json.dumps({}), 
                content_type='application/json')
    assert b'JSON not found' in response.data   

