import time
import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage


# @pytest.mark.skip
class TestGuestAddToBasketFromProductPage:

    @pytest.mark.need_review
    @pytest.mark.parametrize('link', [
        # 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019',
        # 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear',
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    def test_guest_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser=browser, url=link)
        page.open()
        page.should_be_product_page()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.check_success_addition_product_to_basket()
        # time.sleep(20)

    @pytest.mark.xfail
    @pytest.mark.parametrize('link', [
        'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019',
    ])
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, link):
        page = ProductPage(browser=browser, url=link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_not_be_success_message()

    @pytest.mark.parametrize('link', [
        'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019',
    ])
    def test_guest_cant_see_success_message(self, browser, link):
        page = ProductPage(browser=browser, url=link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail
    @pytest.mark.parametrize('link', [
        'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019',
    ])
    def test_message_disappeared_after_adding_product_to_basket(self, browser, link):
        page = ProductPage(browser=browser, url=link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_disappeared_success_message()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.xfail
    def test_guest_can_not_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_invalid_login_page()
        login_page = LoginPage(browser=browser, url=browser.current_url)
        login_page.should_be_login_page()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser=browser, url=browser.current_url)
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link_main_page = "http://selenium1py.pythonanywhere.com"
        main_page = MainPage(browser=browser, url=link_main_page)
        main_page.open()
        main_page.go_to_basket()
        basket_page = BasketPage(browser=browser, url=browser.current_url)
        basket_page.should_be_no_products()
        basket_page.should_be_no_items_text()

    @pytest.mark.need_review
    @pytest.mark.parametrize('link', [
        'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019',
    ])
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser, link):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_no_products()
        basket_page.should_be_no_items_text()


# @pytest.mark.skip
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser=browser)
        login_page.open()

        email = str(time.time()) + "@fakemail.org"
        login_page.register_new_user(email, "d8sus86w621265xgd5w8")
        login_page.should_be_authorized_user()

    @pytest.mark.parametrize('link', [
        'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019',
    ])
    def test_user_cant_see_success_message(self, browser, link):
        page = ProductPage(browser=browser, url=link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    @pytest.mark.parametrize('link', [
        'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'])
    def test_user_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser=browser, url=link)
        page.open()
        # time.sleep(3)
        # page.should_be_product_page()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.check_success_addition_product_to_basket()
