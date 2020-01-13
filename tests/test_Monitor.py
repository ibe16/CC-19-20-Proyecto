import pytest
from unittest.mock import Mock, patch

import sys
sys.path.append('monitor')
import Monitor

@pytest.fixture(scope='session')
def db():
    return Mock()

@pytest.fixture(scope='session')
def monitor(db):
    monitor = Monitor.Monitor(db)
    return monitor

def test_get_services_status(monitor):
    result = monitor.get_services_status()
    assert result is not None

def test_get_services_names(monitor):
    result = monitor.get_services_names()
    assert result == ["Git Operations","API Requests","Webhooks","Visit www.githubstatus.com for more information","Issues, PRs, Projects","GitHub Actions","GitHub Packages", "GitHub Pages","Other"]

def test_get_status_types(monitor):
    result = monitor.get_status_types()
    assert result == {"status_types": ['operational', 'degraded_performance', 'partial_outage', 'major_outage']}

def test_get_service_status(monitor):
    data = monitor.get_service_status('GitHub Actions')
    result = data['status']
    assert result in ['operational', 'degraded_performance', 'partial_outage', 'major_outage']

def test_start_downtime(monitor, db):
    monitor.start_downtime('Github Actions')
    db.start_downtime.assert_called_once()

def test_end_downtime(monitor, db):
    monitor.end_downtime(1)
    db.end_downtime.assert_called_once()

    db.end_downtime.side_effect = ValueError
    with pytest.raises(ValueError, match="El id no existe"):
        monitor.end_downtime(45)

def test_delete_downtime(monitor, db):
    monitor.delete_downtime(1)
    db.delete_downtime.assert_called_once()

    db.delete_downtime.side_effect = ValueError
    with pytest.raises(ValueError, match="El id no existe"):
        monitor.delete_downtime(45)

def test_get_downtime_record(monitor, db):
    monitor.get_downtime_record('GitHub Actions')
    db.get_downtime_record.assert_called_with('GitHub Actions')

def test_get_downtime(monitor, db):
    monitor.get_downtime(1)
    db.get_downtime.assert_called_with(1)
