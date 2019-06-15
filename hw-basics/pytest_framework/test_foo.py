import pytest


# pytest 生命周期

def setup_module():
    print('整个模块.py开始')


def teardown_module():
    print('整个模块.py结束')


def setup_function():
    print('不在类中的函数前')


def teardown_function():
    print('不在类中的函数后')


def test_w_one():
    print('不在类中的函数1')


def test_w_two():
    print('不在类中的函数2function')


class TestClass:
    def setup_class(self):
        print('类前面')

    def teardown_class(self):
        print('类之后')

    def setup_method(self):
        print('方法前')

    def teardown_method(self):
        print('方法后')

    def test_one(self):
        x = "this"
        assert "th" in x


    def test_two(self):
        x = 'hello'
        pytest.assume(0)
        pytest.assume(x in 'hell1o1')
        pytest.assume(0)


    def test_three(self):
        a = "hello"
        b = "hello world"
        assert a in b


if __name__ == '__main__':
    pytest.main(["-s", "test_foo.py"])
    # -s -v -q

