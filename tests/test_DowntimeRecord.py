import pytest
from datetime import datetime

import os
import sys
sys.path.append('monitor')
import DowntimeRecord

@pytest.fixture(scope='session')
def downtime_record():
    d = DowntimeRecord.DowntimeRecord()
    return d

def test_start_downtime_and_end_downtime(downtime_record):
    id_s = downtime_record.start_downtime('GitHub Actions', datetime.now())
    assert id_s is not None

    id_e = downtime_record.end_downtime(id_s, datetime.now())
    assert id_e == id_s

def test_get_downtime_record(downtime_record):
    result = downtime_record.get_downtime_record('No existe')
    assert result == {}
    result = downtime_record.get_downtime_record('GitHub Actions')
    assert result == {'GitHub Actions' : [1]}

def test_get_downtime(downtime_record):
    result = downtime_record.get_downtime(45)
    assert result == {}
    result = downtime_record.get_downtime(1)
    assert result

def test_delete_downtime(downtime_record):
    with pytest.raises(ValueError, match="El id no existe"):
        downtime_record.delete_downtime(45)

    downtime_record.delete_downtime(1)
    result = downtime_record.get_downtime(1)
    assert result == {}