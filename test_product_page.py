import time
import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage


@pytest.mark.skip
@pytest.mark.parametrize('link', [
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019',
    'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear',
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.should_be_product_page()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.check_success_addition_product_to_basket()
    # time.sleep(20)


@pytest.mark.skip
@pytest.mark.xfail
@pytest.mark.parametrize('link', [
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019',
])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


@pytest.mark.skip
@pytest.mark.parametrize('link', [
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019',
])
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
@pytest.mark.xfail
@pytest.mark.parametrize('link', [
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019',
])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_disappeared_success_message()


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.skip
@pytest.mark.xfail
def test_guest_can_not_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_invalid_login_page()
    login_page = LoginPage(browser=browser, url=browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser=browser, url=browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link_main_page = "http://selenium1py.pythonanywhere.com"
    main_page = MainPage(browser=browser, url=link_main_page)
    main_page.open()
    main_page.go_to_basket()
    basket_page = BasketPage(browser=browser, url=browser.current_url)
    basket_page.should_be_no_products()
    basket_page.should_be_no_items_text()


@pytest.mark.parametrize('link', [
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019',
])
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_no_products()
    basket_page.should_be_no_items_text()
