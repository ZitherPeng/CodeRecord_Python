import pytest


# Possible values for scope are: function, class, module, package or session.
@pytest.fixture(scope='module')
def login():
    print('login...')


@pytest.fixture(autouse=True)
def operating_browser():
    print('open browser')
    yield
    print('close browser')

@pytest.fixture(scope='module')
def exit():
    print('exit...')


def test_search_function():
    print(' I\'m searching...')
    assert 0


class Test_Fixture:

    @pytest.mark.usefixtures('login')
    def test_search(self):
        print('I\'m searching...')


if __name__ == '__main__':
    pytest.main(['-s', 'test_fixture.py'])
