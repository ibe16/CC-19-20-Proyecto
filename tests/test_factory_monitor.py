import pytest

import sys
sys.path.append('monitor')
from monitor import create_app

# comprueba que se crea bien la aplicacións
def test_config():
    assert not create_app().testing
    assert create_app({"TESTING":True}).testing