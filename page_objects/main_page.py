from selenium.webdriver.common.by import By

from page_objects.found_product_page import FoundProductPage
from page_objects.login_page import LoginPage
from utilities.decorators import allure_step
from utilities.web_ui.base_page import BasePage


@allure_step
class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __login_button = (By.XPATH, '//*[@title="Мій акаунт"]/parent::a[@href="/mynotino/"]')
    __search_input = (By.XPATH, '//input[@type="search"]')
    __search_item_button = (By.XPATH, '//*[@href="https://www.notino.ua/kringle-candle/'
                                      'vineyard-cabernet-aromatichna-svichka/"]')
    __search_icon = (By.XPATH, '//a[@data-testid="search-icon"]')
    __cart_button = (By.XPATH, '//a[@href="/cart/"]')
    __negative_search_result_message = (By.XPATH, '//p[@class="styled__SearchNoResultsText-sc-14y14oz-4 CsDMr"]')
    __actions_button = (By.XPATH, '//a[@href="/aktsiyi/" and @aria-haspopup="true"]')
    __free_gifts_button = (By.XPATH, '//a[@href="/aktualni-akciji/" and @class="styled__Category-sc-lh232m-0 buJOdN"]')
    __gifts_list = (By.XPATH, '//*[@id="col-content"]')
    __brands_button = (By.XPATH, '//a[@href="/kosmetychni-brendy/"]')
    __brands_list = (By.XPATH, '//div[@class="crossroad-brands"]')
    __beauty_blog_button = (By.XPATH, '//a[@href="/beautyblog/"]')
    __get_the_look_button = (By.XPATH, '//a[@href="/beautyblog/get-the-look/"]')
    __fashionable_look_advices_button = (By.XPATH, '//nav/a[@href="/beautyblog/get-the-look/modnij/"]')
    __newsletter_input = (By.XPATH, '//input[@name="EmailNews"]')
    __female_button = (By.XPATH, '//*[@id="womanButton"]')

    def click_login_button(self):
        self._click(self.__login_button)
        return LoginPage(self.driver)

    def set_search_input(self, search_item: str):
        self._send_keys(locator=self.__search_input, value=search_item)
        return self

    def click_search_icon(self):
        self._click_with_js_execute(self.__search_icon)
        return self

    def is_negative_search_result_message_displayed(self):
        return self._is_visible(self.__negative_search_result_message)

    def click_search_item_button(self):
        self._click_with_js_execute(self.__search_item_button)
        return FoundProductPage(self.driver)

    def found_product(self, search_item: str):
        self.set_search_input(search_item).click_search_item_button()
        return FoundProductPage(self.driver)

    def click_actions_button(self):
        self._click_with_js_execute(self.__actions_button)
        return self

    def click_free_gifts_button(self):
        self._click(self.__free_gifts_button)
        return self

    def is_gifts_list_exist(self):
        return self._is_located(self.__gifts_list)

    def click_brands_button(self):
        self._click_with_js_execute(self.__brands_button)
        return self

    def is_brands_list_exist(self):
        return self._is_located(self.__brands_list)

    def click_beauty_blog_button(self):
        self._click_with_js_execute(self.__beauty_blog_button)
        return self

    def click_get_the_look_button(self):
        self._click(self.__get_the_look_button)
        return self

    def is_fashionable_look_advices_button_exist(self):
        return self._is_located(self.__fashionable_look_advices_button)

    def set_newsletter_input(self, email: str):
        self._send_keys(locator=self.__newsletter_input, value=email)
        return self

    def is_female_button_clickable(self):
        return self._is_clickable(self.__female_button)
