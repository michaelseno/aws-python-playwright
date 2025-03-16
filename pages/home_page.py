from playwright.sync_api import Page
from pages.base_page import BasePage

class HomePage:
    def __init__(self, page: Page):
        self.__page = BasePage(page)
        self.__page_url = "http://aws-personal-portfolio-bucket.s3-website-us-east-1.amazonaws.com"
        self.__header_locator = "text=Welcome to My Cloud Portfolio"
        self.__about_locator = "#about"
        self.__skills_locator = "#skills"
        self.__projects_locator = "#projects"
        self.__contact_locator = "#contact"

    def open_homepage(self):
        self.__page.open_url(url=self.__page_url)

    def validate_homepage(self):
        self.__page.validate_locator(self.__header_locator)
        self.__page.validate_locator(self.__about_locator)
        self.__page.validate_locator(self.__skills_locator)
        self.__page.validate_locator(self.__projects_locator)
        self.__page.validate_locator(self.__contact_locator)


