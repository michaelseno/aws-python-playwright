from playwright.sync_api import Page
from utilities.logger import Logs


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.log = Logs()

    def open_url(self, url):
        try:
            self.log.info(f"opening URL: {url}")
            self.page.goto(url)
        except Exception as e:
            self.log.error(f"`page.goto()` encountered an Exception: {e}")

    def validate_locator(self, locator, timeout=3000):
        try:
            self.log.info(f"Waiting for element locator {locator} to be visible within {timeout}ms ")
            self.page.wait_for_selector(selector=locator, timeout=timeout)
        except Exception as e:
            self.log.error(f"`validate_locator()` encountered an Exception: {e}")
