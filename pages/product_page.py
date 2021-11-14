from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_product_gallery()
        self.should_be_main()
        self.should_be_description()

    def should_be_product_gallery(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_GALLERY), "Not found product gallery images"

    def should_be_main(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_TITLE), "Not found product title"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Not found product price"
        assert self.is_element_present(*ProductPageLocators.AVAILABILITY), "Not found product availability"
        assert self.is_element_present(*ProductPageLocators.WRITE_REVIEW), "Not found button write review about product"
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "Not found button add product to basket"
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_WISHLIST), "Not found button add product to wishlist"

    def should_be_description(self):
        assert self.is_element_present(*ProductPageLocators.DESCRIPTION), "Not found DESCRIPTION product"

    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET).click()

    def check_success_addition_product_to_basket(self):
        self.browser.implicitly_wait(5)

        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGES)

        assert len(self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGES)) == 2

        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        product_title_in_basket = self.browser.find_element(*ProductPageLocators.TITLE_PRODUCT_IN_BASKET).text
        assert product_title_in_basket == product_title, "The title product on the page and product in basket do not match"

        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        info_message_price = self.browser.find_element(*ProductPageLocators.NEW_AMOUNT_BASKET).text
        assert info_message_price == product_price, "The price product on the page and product in basket do not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGES), "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGES), "Success message is presented, but should be disappeared"
