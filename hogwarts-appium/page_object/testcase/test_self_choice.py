import pytest

from page_object.page.MainPage import MainPage


class TestSelfChoice(object):
    def test_price(self):
        main = MainPage()
        assert main.click_self_choice()