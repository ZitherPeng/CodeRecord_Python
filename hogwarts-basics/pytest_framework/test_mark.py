import pytest
import sys


class TestMark():
    # .
    def test_normal(self):
        print(sys.platform)

    @pytest.mark.skip
    def test_skip(self):
        print('skip')

    # S
    @pytest.mark.skipif(sys.platform == 'win32', reason='not run on win32')
    def test_skipif(self):
        print('I\'m not windows. I\'m ' + sys.platform)

    # X
    @pytest.mark.xfail
    def test_xfail(self):
        raise Exception('WRONG')

@pytest.mark.andoid
def test_only_android():
    print('only on android')

@pytest.mark.ios
def test_only_ios():
    print('only on ios')

@pytest.mark.macos
def test_only_macos():
    print('only on macos')

# pytest -m 'ios' test_mark.py
# pytest -m 'not ios' test_mark.py

