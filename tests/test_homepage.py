import pytest
from utilities.test_config import browser
from pages.home_page import HomePage


class TestHomePage:

    def test_open_homepage(self, browser):
        homepage = HomePage(browser)
        homepage.open_homepage()
        homepage.validate_homepage()
