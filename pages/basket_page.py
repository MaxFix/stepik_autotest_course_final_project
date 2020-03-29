from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BasketPage(BasePage):

    def should_be_busket(self):
        self.should_be_basket_head_title()
        self.should_be_basket_caption()

    def should_be_basket_head_title(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_TILE_EN), "Basket page title not found."

    def should_be_basket_caption(self):
        assert self.is_element_present(*BasketPageLocators.PAGE_ACTION_TITLE_EN), "Basket page caption not found."

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty."

    def should_be_basket_is_empty_message(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_IS_EMPTY_MSG), "'Your basket is empty' message not found."
