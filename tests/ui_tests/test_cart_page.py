import pytest


@pytest.mark.smoke
def test_remove_product_from_cart_button(open_cart_page):
    cart_page = open_cart_page
    remove_from_cart = cart_page.click_remove_product_from_cart_button()
    assert remove_from_cart.is_my_product_in_cart_invisible(), 'Product was not removed from cart'


@pytest.mark.smoke
def test_is_input_error_message_displayed(open_cart_page, env):
    cart_page = open_cart_page
    error_message = cart_page.set_discount_code_input(env.invalid_discount).\
        click_submit_discount_code_button()
    assert error_message.is_input_error_message_displayed(), 'Input error message was not displayed'


@pytest.mark.smoke
def test_select_eco_wrapping_checkbox(open_cart_page):
    cart_page = open_cart_page
    eco_wrap = cart_page.select_eco_wrapping_checkbox()
    assert eco_wrap.is_gift_wrapping_checkbox_invisible(), 'Eco wrapping checkbox was not selected'


@pytest.mark.smoke
def test_click_back_to_shop_button(open_cart_page):
    cart_page = open_cart_page
    categories_of_products = cart_page.click_back_to_shop_button()
    assert categories_of_products.is_categories_of_products_links_displayed(), \
        'Categories of products was not displayed'


@pytest.mark.regression
def test_click_order_button(open_cart_page):
    cart_page = open_cart_page
    order_steps = cart_page.select_eco_wrapping_checkbox().click_order_button()
    assert order_steps.is_order_steps_chain_displayed(), 'Order steps was not displayed'
