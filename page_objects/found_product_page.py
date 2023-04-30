from selenium.webdriver.common.by import By

from page_objects.cart_page import CartPage
from utilities.decorators import allure_step
from utilities.web_ui.base_page import BasePage


@allure_step
class FoundProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __product_description = (By.XPATH, '//*[@id="tabDescription"]')
    __buy_button = (By.XPATH, '//button[@id="pd-buy-button"]')
    __go_to_cart_button = (By.XPATH, '//a[@data-cypress="goToShoppingCart"]')
    __continue_shopping_button = (By.XPATH, '//button[@id="upsellingContinueWithShopping"]')
    __quantity_dropdown = (By.XPATH, '//div[@class="sc-jmpzUR hUYIcj"]')
    __select_two_units_of_product = (By.XPATH, '//div[text()=2]/parent::div')
    __two_units_of_product_selected = (By.XPATH, '//div[@role="combobox" and @aria-label="2"]')
    __add_to_wishlist_button = (By.XPATH, '//a[@class="sc-b729bm-1 eUuHfR"]')
    __wishlist_button = (By.XPATH, '//a[@href="/wishlist/"]')
    __product_in_wishlist = (By.XPATH, '//div[@class="sc-ezOQGI kvUqtV"]')
    __select_three_units_of_product = (By.XPATH, '//div[text()=3]/parent::div')
    __too_much_products_selected_error_message = (By.XPATH, '//div[@class="sc-1io4v49-9 iEcErq"]')
    __delivery_time_expand_button = (By.XPATH, '//*[@id="pdDeliveryTime"]//button')
    __delivery_spot = (By.XPATH, '//div[@role="list"]//following::div[@role="listitem"]/following-'
                                 'sibling::div/following-sibling::div')
    __shipping_info_button = (By.XPATH, '//div[@class="shipping-info"]/a[@href="/dostavka-ta-oplata/"]')
    __delivery_price_list = (By.XPATH, '//div[@class="delivery-pricelist"]')
    __reviews_button = (By.XPATH, '//button[@id="tabReviews"]')
    __add_new_review_button = (By.XPATH, '//button[@data-cypress="reviews-addNewReview"]')
    __five_star_review_button = (By.XPATH, '//div[@class="sc-hBxehG DALue"]//following-sibling::button/following'
                                           '-sibling::button/following-sibling::button/following-sibling::button')
    __reviewer_name_input = (By.XPATH, '//*[@id="input_reviewsName"]')
    __send_review_button = (By.XPATH, '//button[@data-cypress="reviewsModal-submitButton"]')
    __review_sent_message = (By.XPATH, '//div[@aria-live="polite"]')

    def get_product_description_text(self):
        return self._get_text(self.__product_description)

    def click_buy_button(self):
        self._click_with_js_execute(self.__buy_button)
        return self

    def click_go_to_cart_button(self):
        self._click(self.__go_to_cart_button)
        return CartPage(self.driver)

    def click_continue_shopping_button(self):
        self._click(self.__continue_shopping_button)
        return self

    def click_quantity_dropdown(self):
        self._click_selected(self.__quantity_dropdown)
        return self

    def select_two_units_of_product(self):
        self._click_with_js_execute(self.__select_two_units_of_product)
        return self

    def is_two_units_of_product_selected_visible(self):
        return self._is_visible(self.__two_units_of_product_selected)

    def click_add_to_wishlist_button(self):
        self._click_with_js_execute(self.__add_to_wishlist_button)
        return self

    def click_wishlist_button(self):
        self._click_selected(self.__wishlist_button)
        return self

    def is_product_in_wishlist_exist(self):
        return self._is_located(self.__product_in_wishlist)

    def select_three_units_of_product(self):
        self._click_with_js_execute(self.__select_three_units_of_product)
        return self

    def is_too_much_products_selected_error_message_displayed(self):
        return self._is_visible(self.__too_much_products_selected_error_message)

    def click_delivery_time_expand_button(self):
        self._click_with_js_execute(self.__delivery_time_expand_button)
        return self

    def is_delivery_spot_visible(self):
        return self._is_visible(self.__delivery_spot)

    def click_shipping_info_button(self):
        self._click_with_js_execute(self.__shipping_info_button)
        return self

    def is_delivery_price_list_visible(self):
        return self._is_visible(self.__delivery_price_list)

    def click_reviews_button(self):
        self._click_with_js_execute(self.__reviews_button)
        return self

    def click_add_new_review_button(self):
        self._click_with_js_execute(self.__add_new_review_button)
        return self

    def click_five_star_review_button(self):
        self._click_with_js_execute(self.__five_star_review_button)
        return self

    def set_reviewer_name_input(self, username: str):
        self._send_keys(locator=self.__reviewer_name_input, value=username)
        return self

    def set_invalid_reviewer_name_input(self, invalid_username: str):
        self._send_keys(locator=self.__reviewer_name_input, value=invalid_username)
        return self

    def click_send_review_button(self):
        self._click_with_js_execute(self.__send_review_button)
        return self

    def is_send_review_button_clickable(self):
        return self._is_clickable(self.__send_review_button)

    def is_review_sent_message_displayed(self):
        return self._is_visible(self.__review_sent_message)
