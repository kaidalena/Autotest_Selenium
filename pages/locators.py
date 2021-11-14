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


class ProductPageLocators:
    PRODUCT_GALLERY = (By.CSS_SELECTOR, "#product_gallery")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    AVAILABILITY = (By.CSS_SELECTOR, ".product_main .availability")
    WRITE_REVIEW = (By.CSS_SELECTOR, '.product_main #write_review')
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '.product_main button.btn-add-to-basket')
    BUTTON_ADD_TO_WISHLIST = (By.CSS_SELECTOR, '.product_main button.btn-wishlist')
    DESCRIPTION = (By.CSS_SELECTOR, '#product_description')

    BLOCK_MESSAGES = (By.CSS_SELECTOR, '#messages')
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, '#messages .alert.alert-safe.alert-noicon.alert-success')
    TITLE_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '#messages .alert.alert-safe.alert-noicon.alert-success:nth-child(1) .alertinner strong')
    INFO_MESSAGES = (By.CSS_SELECTOR, '#messages .alert.alert-safe.alert-noicon.alert-info')
    NEW_AMOUNT_BASKET = (By.CSS_SELECTOR, '#messages .alert.alert-safe.alert-noicon.alert-info .alertinner strong')
