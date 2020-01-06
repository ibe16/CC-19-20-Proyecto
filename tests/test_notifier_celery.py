import pytest
from unittest.mock import Mock, patch

import sys
sys.path.append('notifier')
from notifier_celery import app, send_emails

def setup_module():
    app.conf.update(CELERY_ALWAYS_EAGER=True)

def test_send_email():
    with patch("smtplib.SMTP") as mock_smtp:
        result = send_emails('1', ['irenebejar@correo.ugr.es'])
        instance = mock_smtp.return_value
        assert instance.sendmail.called == True 
    