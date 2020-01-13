import pytest
from unittest.mock import Mock, patch

import sys
sys.path.append('monitor')
sys.path.append('notifier')
from monitor_celery import app, check_services

def setup_module():
    app.conf.update(CELERY_ALWAYS_EAGER=True)

def test_check_services():
        check_services()