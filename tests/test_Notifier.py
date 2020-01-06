import pytest
from unittest.mock import Mock, patch

import sys
sys.path.append('notifier')
import Notifier
import NotificationList_model


@pytest.fixture(scope='session')
def db():
    return Mock()

@pytest.fixture(scope='session')
def notifier(db):
    notifier = Notifier.Notifier(db)
    return notifier

def test_subscribe(notifier, db):
    notifier.subscribe('test@email.com', '1')
    db.create.assert_called_with('test@email.com', '1')
    
    db.create.side_effect = NameError
    with pytest.raises(NameError, match='El email existe ya'):
        notifier.subscribe('test@email.com', '1')

def test_unsubscribe(notifier, db):
    notifier.unsubscribe('test@email.com', '1')
    db.delete.assert_called_with('test@email.com', '1')

def test_subscriptions(notifier, db):
    db.read_email.return_value = [ ]
    with pytest.raises(ValueError, match='El email no tiene subscripciones'):
        notifier.subscriptions('test@email.com')
    db.read_email.assert_called_with('test@email.com')

    db.read_email.return_value = [NotificationList_model.NotificationList_model(email=['test@email.com'], id_line='1')]
    result = notifier.subscriptions('test@email.com')
    assertion = {'id_lines' : ['1']}
    assert result == assertion

def test_update(notifier, db):
    notifier.update('1', 'viejo@email.com', 'nuevo@email.com')
    db.update.assert_called_with('1', 'viejo@email.com', 'nuevo@email.com')

    db.update.side_effect = ValueError
    with pytest.raises(ValueError, match='Argumentos inválidos'):
        notifier.update('1', 'viejo@email.com', 'nuevo@email.com')

def test_notification(notifier, db):
    result1 = ['test1@email.com', 'test2@email.com']
    result2 = [ ]
    
    db.read_line.return_value = result2
    notifier.notification('1')
    db.read_line.assert_called_with('1')
    
