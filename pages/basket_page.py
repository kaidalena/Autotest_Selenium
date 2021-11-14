from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_no_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)

    def should_be_no_items_text(self):
        assert self.is_element_present(*BasketPageLocators.NO_ITEMS_TEXT)
