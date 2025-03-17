from utilities.logger import Logs
import pytest


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.page = browser.new_page()
        self.log = Logs()

    def open_url(self, url):
        try:
            self.log.info(f"opening URL: {url}")
            self.page.goto(url)
        except Exception as e:
            self.page.screenshot(path="screenshots/failure.png")
            self.log.error(f"`page.goto()` encountered an Exception: {e}")
            pytest.fail(e)

    def validate_locator(self, locator, timeout=3000):
        try:
            self.log.info(f"Waiting for element locator {locator} to be visible within {timeout}ms ")
            self.page.wait_for_selector(selector=locator, timeout=timeout)
        except Exception as e:
            self.page.screenshot(path=f"screenshots/element_{locator}_not_found.png")
            self.log.error(f"`validate_locator()` encountered an Exception: {e}")
            pytest.fail(e)
