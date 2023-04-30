from selenium.webdriver.common.by import By
from page_objects.my_account_page import MyAccountPage
from utilities.decorators import allure_step
from utilities.web_ui.base_page import BasePage


@allure_step
class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __login_form = (By.XPATH, '//*[@id="login"]')
    __email_input = (By.XPATH, '//input[@name="Email"]')
    __password_input = (By.XPATH, '//input[@name="Password"]')
    __log_in_button = (By.XPATH, '//button[@value="login"]')
    __forgot_password_button = (By.XPATH, '//a[@class="reset-pwd"]')
    __validation_error_message = (By.XPATH, '//span[@class="message error-message field-validation-error"]')
    __reset_password_form = (By.XPATH, '//*[@id="pwd-forgot-step-1"]')
    __register_link = (By.XPATH, '//a[@class="register-link"]')
    __register_form = (By.XPATH, '//*[@id="register"]')
    __log_in_with_register_form_button = (By.XPATH, '//a[@class="register-link" and @href="/account/login"]')

    def is_login_form_visible(self):
        return self._is_visible(self.__login_form)

    def set_email(self, email: str):
        self._send_keys(locator=self.__email_input, value=email)
        return self

    def set_password(self, password: str):
        self._send_keys(locator=self.__password_input, value=password)
        return self

    def click_log_in_button(self):
        self._click(self.__log_in_button)

    def login(self, email, password):
        self.set_email(email).set_password(password).click_log_in_button()
        return MyAccountPage(self.driver)

    def set_invalid_email(self, invalid_email: str):
        self._send_keys(locator=self.__email_input, value=invalid_email)
        return self

    def set_invalid_password(self, invalid_password: str):
        self._send_keys(locator=self.__password_input, value=invalid_password)
        return self

    def click_login_button_with_invalid_user_data(self, invalid_email: str, invalid_password: str):
        self.set_invalid_password(invalid_email).set_invalid_password(invalid_password).click_log_in_button()
        return self

    def is_validation_error_message_visible(self):
        return self._is_visible(self.__validation_error_message)

    def click_forgot_password_button(self):
        self._click(self.__forgot_password_button)
        return self

    def is_reset_password_form_exist(self):
        return self._is_located(self.__reset_password_form)

    def click_register_link(self):
        self._click(self.__register_link)
        return self

    def is_register_form_visible(self):
        return self._is_visible(self.__register_form)

    def click_log_in_with_register_form_button(self):
        self._click_with_js_execute(self.__log_in_with_register_form_button)
        return self
