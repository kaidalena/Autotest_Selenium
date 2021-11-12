import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ch_options
from selenium.webdriver.firefox.options import Options as fr_options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='ru')


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")

    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = ch_options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = fr_options()
        profile = webdriver.FirefoxProfile()
        profile.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(options=options, firefox_profile=profile)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    time.sleep(5)
    print("\nquit browser..")
    browser.quit()
