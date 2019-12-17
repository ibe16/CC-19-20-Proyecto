import pytest

import sys
sys.path.append('notifier')
import NotificationList

@pytest.fixture(scope='session')
def notification_list():
    list = NotificationList.NotificationList()
    list.subscribe(1, 'irene@email.com')
    list.subscribe(1, 'bejar@gmail.com')
    list.subscribe(2, 'irene@email.com')
    return list

def test_subscribe(notification_list):
    notification_list.subscribe(3, 'test@email.com')
    assert str(notification_list) == str({1: ['irene@email.com', 'bejar@gmail.com'], 2: ['irene@email.com'], 3: ['test@email.com']})
    notification_list.subscribe(2, 'test@email.com')
    assert str(notification_list) == str({1: ['irene@email.com', 'bejar@gmail.com'], 2: ['irene@email.com', 'test@email.com'], 3: ['test@email.com']})
    assert len(notification_list) == 3
    with pytest.raises(ValueError, match='Email no válido'):
        notification_list.subscribe(4, 'test.email')

def test_unsubscribe(notification_list):
    notification_list.unsubscribe(3, 'test@email.com')
    assert str(notification_list) == str({1: ['irene@email.com', 'bejar@gmail.com'], 2: ['irene@email.com', 'test@email.com']})
    assert len(notification_list) == 2
    with pytest.raises(ValueError, match='El email no existe'):
        notification_list.unsubscribe(1, 'test.email')
    with pytest.raises(KeyError, match='La línea no existe'):
        notification_list.unsubscribe(4, 'test@email.com')

def test_subscriptions(notification_list):
    list = notification_list.subscriptions('irene@email.com')
    assert list == [1, 2]
    with pytest.raises(ValueError, match='El email no tiene subscripciones'):
        notification_list.subscriptions('test@correo.com')