from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    AUTH_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    AUTH_LOGIN = (By.CSS_SELECTOR, "#id_login-username")
    AUTH_PASS = (By.CSS_SELECTOR, "#id_login-password")
    REG_LOGIN = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_REP_PASS = (By.CSS_SELECTOR, "#id_registration-password2")
