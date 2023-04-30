from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(self.driver, 13, 5)

    def _is_located(self, locator):
        return self.__wait.until(EC.presence_of_element_located(locator))

    def _is_clickable(self, locator):
        return self.__wait.until(EC.element_to_be_clickable(locator))

    def _send_keys(self, locator, value, is_clear=True):
        element = self._is_located(locator)
        if is_clear:
            element.clear()
        element.send_keys(value)

    def _click_selected(self, locator):
        self._is_located(locator).click()

    def _click(self, locator):
        self._is_clickable(locator).click()

    def _is_visible(self, locator):
        return self.__wait.until(EC.visibility_of_element_located(locator))

    def _is_invisible(self, locator):
        return self.__wait.until(EC.invisibility_of_element_located(locator))

    def _click_with_js_execute(self, locator):
        return self.driver.execute_script('arguments[0].click()', self._is_located(locator))

    def _get_text(self, locator):
        element = self._is_located(locator)
        return element.text
