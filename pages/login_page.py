from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def __init__(self, *args, **kwargs,):
        kwargs['url'] = kwargs.get('url', 'http://selenium1py.pythonanywhere.com/ru/accounts/login/')
        super().__init__(*args, **kwargs)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, f"Current url should be contain 'login' in url, but found {self.browser.current_url}"
        assert self.browser.current_url == self.url, f"Current url should be login url ({self.url}), but found {self.browser.current_url}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.AUTH_FORM), "Not found login form"
        assert self.is_element_present(*LoginPageLocators.AUTH_LOGIN), "Not found field for login in login form"
        assert self.is_element_present(*LoginPageLocators.AUTH_PASS), "Not found field for password in login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Not found registration form"
        assert self.is_element_present(*LoginPageLocators.REG_LOGIN), "Not found field for login in registration form"
        assert self.is_element_present(*LoginPageLocators.REG_PASS), "Not found field for password in registration form"
        assert self.is_element_present(*LoginPageLocators.REG_REP_PASS), "Not found field for repeat password in registration form"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REG_LOGIN).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_REP_PASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BTN).click()
