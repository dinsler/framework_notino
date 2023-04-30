from utilities.decorators import allure_step
from utilities.web_ui.base_page import BasePage
from selenium.webdriver.common.by import By


@allure_step
class MyAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __logout_button = (By.XPATH, '//a[@href="#"]')
    __confirm_logout_button = (By.XPATH, '//button[@loading="1"]')
    __my_contact_data_button = (By.XPATH, '//a[@class="sc-JHWBx hDbydo" and @href="/mynotino/customer-profile"]')
    __address_data_form = (By.XPATH, '//div[@class="sc-fmixVB gFNBiH"]')
    __my_orders_button = (By.XPATH, '//a[@href="/mynotino/my-orders"]')
    __orders_status_message = (By.XPATH, '//div/h2[text()="Поки що у вас немає жодного замовлення"]')
    __my_purchased_products_button = (By.XPATH, '//a[@href="/mynotino/purchased-products"]')
    __purchased_products_status_message = (By.XPATH, '//h2[text()="У вас поки що немає придбаних продуктів"]')
    __my_complaints_button = (By.XPATH, '//a[@href="/mynotino/my-complaints"]')
    __complaints_status_message = (By.XPATH, '//h2[text()="Досі ви не подали жодної рекламації"]')

    def is_logout_button_exist(self):
        return self._is_located(self.__logout_button)

    def click_my_contact_data_button(self):
        self._click(self.__my_contact_data_button)
        return self

    def is_address_data_exist(self):
        return self._is_located(self.__address_data_form)

    def click_my_orders_button(self):
        self._click(self.__my_orders_button)
        return self

    def is_orders_status_message_visible(self):
        return self._is_visible(self.__orders_status_message)

    def click_my_purchased_products_button(self):
        self._click(self.__my_purchased_products_button)
        return self

    def is_purchased_products_status_message_visible(self):
        return self._is_visible(self.__purchased_products_status_message)

    def click_my_complaints_button(self):
        self._click(self.__my_complaints_button)
        return self

    def is_complaints_status_message_visible(self):
        return self._is_visible(self.__complaints_status_message)

    def click_logout_button(self):
        self._click(self.__logout_button)
        return self

    def click_confirm_logout(self):
        self._click(self.__confirm_logout_button)
        return self

    def is_my_contact_data_button_invisible(self):
        return self._is_invisible(self.__my_contact_data_button)
