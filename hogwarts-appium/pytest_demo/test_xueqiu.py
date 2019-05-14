from appium import webdriver
from appium.webdriver.webdriver import MobileWebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait



class DriverFactory(object):
    """ Generate the caps and set up AppiumDriver. """

    def create_driver(self, platform) -> WebDriver:
        if 'Android' == platform:
            return webdriver.Remote('http://localhost:4723/wd/hub',
                                    self.android_caps())

    def android_caps(self):
        caps = {
            'platformName': 'Android',
            'autoGrantPermissions': 'true',
            'noReset': 'true'
        }
        caps['deviceName'] = 'vivo x9'
        caps['platformVersion'] = '7.1'
        caps['automationName'] = 'UiAutomator2'
        caps['appPackage'] = 'com.xueqiu.android'
        caps['appActivity'] = '.view.WelcomeActivityAlias'
        caps['unicodeKeyboard'] = 'true'
        caps['resetKeyboard'] = 'true'
        return caps


class ElementUtil(object):
    """ Package element's common function. """

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, timeout, locator) -> MobileWebElement:
        return WebDriverWait(self.driver, timeout).until(
            lambda x: x.find_element(*locator))

    def click(self, byType, locate, timeout=10):
        element = self.find_element(timeout, (byType, locate))
        element.click()
        return self

    def typing(self, byType, locate, value, timeout=10):
        element = self.find_element(timeout, (byType, locate))
        element.click()  # Let the element in focus.
        element.clear()
        element.send_keys(value)
        return self

    # 内部类




class BasePage(ElementUtil):
    """
    Parent class for all pages.
    Extended from ElementUtil, also package page's common function.
    """
    pass


class MainClass(object):
    def choose_stock(self):
        driver = DriverFactory().create_driver('Android')

        BasePage(driver) \
            .click('id', 'skip_ad') \
            .click('id', 'tv_search') \
            .typing('id', 'search_input_text'
                    , 'alibaba') \
            .click('id', 'follow_btn')

        driver.quit()

    if __name__ == '__main__':
        pass

