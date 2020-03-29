from .base_page import BasePage
from  .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_basket_top(self):
        link = self.browser.find_element(*MainPageLocators.TOP_BASKET_LINK)
        link.click()
