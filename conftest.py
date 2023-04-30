from contextlib import suppress
import allure
import pytest
import json

from constans import ROOT_DIR
from page_objects.main_page import MainPage

from utilities.configuration import Configuration
from utilities.driver_factory import driver_factory


@pytest.fixture(scope='session', autouse=True)
def env():
    with open(f'{ROOT_DIR}/configurations/config.json', 'r') as file:
        res = file.read()
        config = json.loads(res)
        return Configuration(**config)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def create_browser(env, request):
    driver = driver_factory(int(env.browser_id))
    driver.maximize_window()
    driver.get(env.app_url)
    yield driver
    # if request.node.rep_call.failed:
    #     with suppress(Exception):
    #         allure.attach(driver.get_screenshot_as_png(),
    #                       name=request.function.__name__,
    #                       attachment_type=allure.attachment_type.PNG)
    driver.quit()


def pytest_addoption(parser):
    parser.addoption('--browser_id', action='store', default=1, help='Set browser id')
    parser.addoption('--env', action='store', help='Env')


@pytest.fixture()
def open_main_page(create_browser):
    return MainPage(create_browser)


@pytest.fixture()
def open_login_page(open_main_page):
    return open_main_page.click_login_button()


@pytest.fixture()
def open_my_account_page(open_login_page, env):
    return open_login_page.login(env.email, env.password)


@pytest.fixture()
def open_found_product_page(open_main_page, env):
    return open_main_page.found_product(env.search_item)


@pytest.fixture()
def open_cart_page(open_found_product_page):
    return open_found_product_page.click_buy_button().click_go_to_cart_button()


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "smoke: for smoke tests"
    )
    config.addinivalue_line(
        "markers", "regression: for regression tests"
    )
