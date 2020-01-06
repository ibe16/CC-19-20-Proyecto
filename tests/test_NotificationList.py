import pytest
import pymongo
from pymongo import MongoClient

import os
import sys
sys.path.append('notifier')
import NotificationList

@pytest.fixture(scope='session')
def notification_list():
    n = NotificationList.NotificationList()
    return n

@pytest.fixture(scope='session')
def mongo_client():
    client = MongoClient(os.environ['MONGO_URI'])
    db = client.notifier
    collection = db.notification_list
    return collection

def setup_module():
    client = MongoClient(os.environ['MONGO_URI'])
    db = client.notifier
    collection = db.notification_list
    
    test = { "_id" : "1", "email" : ["test@email.com"] }
    collection.insert_one(test)

def teardown_module(mongo_client):
    client = MongoClient(os.environ['MONGO_URI'])
    db = client.notifier
    collection = db.notification_list
    collection.delete_many({ })

def test_read_email(notification_list):
    response = notification_list.read_email('test@email.com')
    
    for r in response:
        assert r.id_line == "1"
        assert r.email == ["test@email.com"]

    response = notification_list.read_email('noexiste@email.com')
    assert response == [ ]

def test_read_line(notification_list):
    response = notification_list.read_line('1')
    assert response == ["test@email.com"]

    response = notification_list.read_line('no_existe')
    assert response == [ ]

def test_create(notification_list, mongo_client):
    with pytest.raises(NameError, match='El email ya existe'):
        notification_list.create('1','test@email.com')

    notification_list.create('1','otraprueba@email.com')
    assertion = mongo_client.find_one({"_id" : "1"})
    assert 'otraprueba@email.com' in assertion['email']

def test_delete(notification_list, mongo_client):
    notification_list.delete('1','otraprueba@email.com')
    assertion = mongo_client.find_one({"_id" : "1"})
    assert 'otraprueba@email.com' not in assertion['email']

def test_update(notification_list, mongo_client):
    with pytest.raises(ValueError, match='No se pudo actualizar'):
        notification_list.update('1','nuevotest@email.com', 'test@email.com')

    notification_list.update('1','test@email.com', 'nuevotest@email.com')
    assertion = mongo_client.find_one({"_id" : "1"})
    assert 'nuevotest@email.com' in assertion['email']


    