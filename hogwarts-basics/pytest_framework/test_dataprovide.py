import pytest

foo = [('3+5', 8), ('2+6', 9)]


@pytest.mark.parametrize('expression,expected', foo)
def test_eval(expression, expected):
    assert eval(expression) == expected


bar = ['lukcy', 'coding']


@pytest.fixture()
def name(request):
    # 这是接收传入的参数，接收一个参数
    print('param is ' + request.param)
    return request.param


# indeirect=True 是把login_r当作函数去执行
@pytest.mark.parametrize('name', bar, indirect=True)
def test_print_name(name):
    print(name)


# parametrizi and fixture
class Test_dataprovide_1:
    baz = [{'name': 'zither', 'passwd': '123'},
           {'name': 'lucky', 'passwd': '123'},
           {'name': 'monica', 'passwd': ''}]

    @pytest.fixture()
    def login_data(self, request):
        print('user is ' + request.param['name'],
              'passwd is ' + request.param['passwd'])
        return False if request.param['passwd'] == '' else True

    @pytest.mark.parametrize('login_data', baz, indirect=True)
    def test_login(self, login_data):
        assert login_data, '密码为空'


class Test_dataprovide_2:
    foo = [{'name': 'zither', 'passwd': '123'},
           {'name': 'lucky', 'passwd': '123'},
           {'name': 'monica', 'passwd': ''}]

    bar = [{"q": "中国平安", "count": 3, "page": 1},
           {"q": "阿里巴巴", "count": 2, "page": 2},
           {"q": "pdd", "count": 3, "page": 1}]

    @pytest.fixture()
    def login_data(self, request):
        print('user is ' + request.param['name'],
              'passwd ' + request.param['passwd'])
        return False if request.param['passwd'] == '' else True

    @pytest.fixture()
    def search_data(self, request):
        print('search key is ' + request.param['q'])
        return request.param

    # 从下往上执行
    # 两个数据进行组合测试有3*3个测试用例执行（test_user_data1的个数*test_user_data2的个数）
    @pytest.mark.parametrize('search_data', bar, indirect=True)
    @pytest.mark.parametrize('login_data', foo, indirect=True)
    def test_login(self, login_data, search_data):
        print(search_data)
        assert login_data, '密码为空'
