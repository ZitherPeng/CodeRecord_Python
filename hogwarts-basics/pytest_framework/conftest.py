# conf pytest

import pytest

@pytest.fixture()
def login():
    print('I\'m login...')

@pytest.fixture()
def operating_browser():
    print('open browser')
    yield
    print('close browser')
