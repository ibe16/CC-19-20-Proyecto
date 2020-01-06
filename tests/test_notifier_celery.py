import pytest
from unittest.mock import Mock

import sys
sys.path.append('notifier')
from notifier_celery import app, send_emails

# @pytest.fixture(scope='session')
# def send_emails():
#     return Mock()

def setup_module():
    app.conf.update(CELERY_ALWAYS_EAGER=True)

def test_send_email():
    result = send_emails('1', ['irenebejar@correo.ugr.es'])
    assert result is None
    