import os
import pytest 


@pytest.fixture()
def root():
    return os.path.dirname(os.path.abspath(__file__))
