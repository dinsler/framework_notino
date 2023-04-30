import pytest


@pytest.mark.smoke
def test_add_product_to_cart(open_found_product_page):
    found_product_page = open_found_product_page
    cart_page = found_product_page.click_buy_button().click_go_to_cart_button()
    actual_text = cart_page.get_cart_page_text()
    assert actual_text == 'Кошик', 'Product was not added to cart'


@pytest.mark.smoke
def test_click_continue_shopping_button(open_found_product_page):
    found_product_page = open_found_product_page
    continue_shopping = found_product_page.click_buy_button().click_continue_shopping_button()
    actual_text = continue_shopping.get_product_description_text()
    assert actual_text == 'Опис', 'Continue shopping button was not clicked'


@pytest.mark.smoke
def test_click_select_two_units_of_product(open_found_product_page):
    found_product_page = open_found_product_page
    select_option = found_product_page.click_quantity_dropdown().select_two_units_of_product()
    assert select_option.is_two_units_of_product_selected_visible(), 'Two units of product were not selected'


@pytest.mark.regression
def test_add_product_to_wishlist(open_found_product_page):
    found_product_page = open_found_product_page
    wishlist = found_product_page.click_add_to_wishlist_button().click_wishlist_button()
    assert wishlist.is_product_in_wishlist_exist(), 'Product was not added to wishlist'


@pytest.mark.regression
def test_is_too_much_products_selected_error_message_displayed(open_found_product_page):
    found_product_page = open_found_product_page
    too_much_products_error = found_product_page.click_quantity_dropdown().select_three_units_of_product().\
        click_buy_button()
    assert too_much_products_error.is_too_much_products_selected_error_message_displayed(), \
        'Error message was not displayed'


@pytest.mark.smoke
def test_click_delivery_time_expand_button(open_found_product_page):
    found_product_page = open_found_product_page
    delivery_spot = found_product_page.click_delivery_time_expand_button()
    assert delivery_spot.is_delivery_spot_visible(), 'Delivery time expand button was not clicked'


@pytest.mark.smoke
def test_shipping_info_button(open_found_product_page):
    found_product_page = open_found_product_page
    delivery_price_list = found_product_page.click_shipping_info_button()
    assert delivery_price_list.is_delivery_price_list_visible(), 'Shipping info button was not clicked'


@pytest.mark.regression
def test_send_review(open_found_product_page, env):
    found_product_page = open_found_product_page
    add_new_review = found_product_page.click_reviews_button().click_add_new_review_button().\
        click_five_star_review_button().set_reviewer_name_input(env.username).click_send_review_button()
    assert add_new_review.is_review_sent_message_displayed(), 'Review was not sent'


@pytest.mark.regression
@pytest.mark.xfail
def test_sent__review_with_invalid_reviewer_name_input(open_found_product_page, env):
    found_product_page = open_found_product_page
    add_new_review = found_product_page.click_reviews_button().click_add_new_review_button(). \
        click_five_star_review_button().set_reviewer_name_input(env.invalid_username)
    assert not add_new_review.is_send_review_button_clickable(), 'Reviewer name input should be valid'
