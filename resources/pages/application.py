from resources.pages.base_page import BasePage
from resources.pages.home_page import HomePage


class Application:

    def __init__(self, app_data):
        self.base_page = BasePage(app_data)
        self.home_page = HomePage(app_data)