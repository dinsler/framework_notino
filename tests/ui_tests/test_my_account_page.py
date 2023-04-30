import pytest


@pytest.mark.smoke
def test_open_my_contact_data(open_my_account_page):
    my_account = open_my_account_page
    contact_data = my_account.click_my_contact_data_button()
    assert contact_data.is_address_data_exist(), "My contact data was not opened"


@pytest.mark.smoke
def test_open_my_purchased_products(open_my_account_page):
    my_account = open_my_account_page
    purchased_products = my_account.click_my_purchased_products_button()
    assert purchased_products.is_purchased_products_status_message_visible(), "Purchased products was not opened"


@pytest.mark.smoke
def test_click_my_orders_button(open_my_account_page):
    my_account = open_my_account_page
    my_orders = my_account.click_my_contact_data_button().click_my_orders_button()
    assert my_orders.is_orders_status_message_visible(), "My orders button was not clicked"


@pytest.mark.smoke
def test_click_my_complaints_button(open_my_account_page):
    my_account = open_my_account_page
    my_complaints = my_account.click_my_complaints_button()
    assert my_complaints.is_complaints_status_message_visible(), "My complaints button was not clicked"


@pytest.mark.regression
def test_logout(open_my_account_page):
    my_account = open_my_account_page
    logout = my_account.click_logout_button().click_confirm_logout()
    assert logout.is_my_contact_data_button_invisible(), "You was not logout"
