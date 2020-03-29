from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    TOP_BASKET_LINK = (By.XPATH, '//div[contains(@class,"basket-mini")]/span[contains(@class,"btn-group")]/a')


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_TWO = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_SUBMIT = (By.XPATH, '//button[@name="registration_submit" and @value="Register"]')


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_TITLE = (By.XPATH, '//div[contains(@class,"product_main")]/h1')
    PRODUCT_PRICE = (By.XPATH, '//div[contains(@class,"product_main")]/p[@class="price_color"]')
    PRODUCT_INSTOCK = (By.XPATH, '//div[contains(@class,"product_main")]/p/i[@class="icon-ok"]')
    PRODUCT_SUCCESSFULLY_ADDED_TO_BASKET = (
        By.XPATH, '//div[contains(@class,"alert-success")]/div[contains(@class,"alertinner")]/strong')
    BASKET_TOTAL_MESSAGE = (
        By.XPATH, '//div[contains(@class,"alert-info")]/div[contains(@class,"alertinner")]/p/strong')
    TOP_BASKET_LINK = (By.XPATH, '//a[@class="btn btn-default"]')


class BasketPageLocators(object):
    BASKET_TILE_EN = (By.XPATH, '//head/title[contains(text(),"Basket")]')
    PAGE_ACTION_TITLE_EN =(By.XPATH, '//div[contains(@class,"page-header") and contains(@class,"action")]/h1['
                                     'contains(text(),"Basket")]')
    BASKET_ITEMS = (By.XPATH, '//div[@class="basket-items"]/div[@class="row"]')
    BASKET_IS_EMPTY_MSG = (By.XPATH, '//div[@id="content_inner"]/p[contains(text(),"Your basket is empty.")]')
