from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoSuchElementException


class ProductPage(BasePage):

    def should_be_btn(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        assert True

    def should_be_product_title(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_TITLE), "Product title is not found."

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not found."

    def click_btn_add_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        btn.click()

    def should_be_product_instock(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_INSTOCK), "Product instock availability is not found."

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), "Add to basket button is not found."

    def should_be_product_added_to_basket_message(self):
        try:
            title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE)
            what_added = self.browser.find_element(*ProductPageLocators.PRODUCT_SUCCESSFULLY_ADDED_TO_BASKET)
        except (NoSuchElementException):
            assert False, "No message product successfully added to the basket."
        assert title.text == what_added.text, "Message 'product was added' not contains product title."

    def should_be_basket_total_message(self):
        try:
            price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
            basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE)
        except (NoSuchElementException):
            assert False, "No message with basket total."
        assert price.text == basket_total.text, "Price of product and basket total mismatch."

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_SUCCESSFULLY_ADDED_TO_BASKET), \
            "Success message is presented, but should not be"

    def should_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_SUCCESSFULLY_ADDED_TO_BASKET), \
            "A success message was presented, but it should have disappeared"

    def add_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        link.click()

    def go_to_basket_top(self):
        link = self.browser.find_element(*ProductPageLocators.TOP_BASKET_LINK)
        link.click()

    def should_be_product(self):
        self.should_be_product_title()
        self.should_be_product_price()
        self.should_be_product_instock()
        self.should_be_add_to_basket_button()
