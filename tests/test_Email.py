import pytest

import sys
sys.path.append('../notifier')
from Email import Email

@pytest.fixture(scope='session')
def email():
    email = Email()
    return email

def test_add(email):
    email.add('irene@email.com')
    assert str(email) == str(['irene@email.com'])
    assert len(email) == 1
    with pytest.raises(ValueError, match='Email no válido'):
        email.add('irene.com')

def test_remove(email):
    email.remove('irene@email.com')
    assert str(email) == str([])
    assert len(email) == 0
    with pytest.raises(ValueError, match='El email no existe'):
        email.remove('irene@email.com')

