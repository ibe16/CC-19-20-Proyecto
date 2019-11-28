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
    app = notifier.create_app({"TESTING": True})

    with app.app_context():
        init_db()
    yield app

@pytest.fixture(scope='session')
def client(app):
    return app.test_client()

def test_hello(client):
    response = client.get('/hello')
    assert b'Hello, World!' == response.data

def test_subscribe(client):
    response = client.post("/notifier/subscribe", 
                data=json.dumps({ "id_line":"1","email":"irene@email.com"}), 
                content_type='application/json')
    assert b'{"message":"Email was subscribed succesfully"}\n' == response.data

    response = client.post("/notifier/subscribe", 
                data=json.dumps({ "id_line":"","email":"irene@email.com"}), 
                content_type='application/json')
    assert b'empty' in response.data

    response = client.post("/notifier/subscribe", 
                data="")
    assert b'JSON not found' in response.data

    response = client.post("/notifier/subscribe", 
                data=json.dumps({}), 
                content_type='application/json')
    assert b'JSON not found' in response.data

def test_email(client):
    response = client.get('/notifier/email')
    print(response.data)
    assert b"{'1': ['irene@email.com']}" == response.data

def test_unsubcsribe(client):
    response = client.delete("/notifier/unsubscribe", 
                data=json.dumps({ "id_line":"1","email":"irene@email.com"}), 
                content_type='application/json')
    assert b'{"message":"Email was deleted "}\n' == response.data

    response = client.delete("/notifier/unsubscribe", 
                data=json.dumps({ "id_line":"","email":"irene@email.com"}), 
                content_type='application/json')
    assert b'empty' in response.data    

    response = client.delete("/notifier/unsubscribe", 
                data="")
    assert b'JSON not found' in response.data

    response = client.delete("/notifier/unsubscribe", 
                data=json.dumps({}), 
                content_type='application/json')
    assert b'JSON not found' in response.data    

