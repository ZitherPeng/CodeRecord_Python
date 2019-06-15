import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner


class TestBar(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('set up')

    def setUp(self):
        print('set up method')

    def test_foo(self):
        assert isinstance('s', str)
        assert 'hello' in 'hello world'
        print('test_foo')

    def test_bar(self):
        assert isinstance('s', int)
        print('test_bar')

    @classmethod
    def tearDownClass(cls) -> None:
        print('trerDown')


if __name__ == '__main__':
    report_path = os.path.join(os.path.dirname(__file__), 'report')
    report_name = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime()) + '_result.html'

    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestBar))

    with open(report_path + '/' + report_name, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title='test report', description='测试用例')
        runner.run(suite)