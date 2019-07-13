import selenium
from selenium import webdriver


class TestDemo(object):
    @classmethod
    def setup_class(cls):
        cls.driver=webdriver.Chrome(executable_path=r'/Users/zither/project/ideaProject/oray.webui.pgybox/webDriver/chromedriver')
        cls.driver.get(r'https://www.luckycoding.com')

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_addStock(self):
        self.driver.find_element()




        pass

    def test_basic(self):
        pass