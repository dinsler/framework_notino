import pytest


@pytest.mark.smoke
def test_login(open_login_page, env):
    login_page = open_login_page
    my_account_page = login_page.login(env.email, env.password)
    assert my_account_page.is_logout_button_exist(), 'You not logged in'


@pytest.mark.smoke
def test_is_validation_error_message_visible(open_login_page, env):
    login_page = open_login_page
    invalid_user_data = login_page.click_login_button_with_invalid_user_data(env.invalid_email, env.invalid_password)
    assert invalid_user_data.is_validation_error_message_visible(), 'Error message is not visible'


@pytest.mark.smoke
def test_open_forgot_password_page(open_login_page):
    login_page = open_login_page
    forgot_password = login_page.click_forgot_password_button()
    assert forgot_password.is_reset_password_form_exist(), 'Forgot password page was not opened'


@pytest.mark.smoke
def test_open_register_form(open_login_page):
    login_page = open_login_page
    register = login_page.click_register_link()
    assert register.is_register_form_visible(), 'Register form was not opened'


@pytest.mark.smoke
def test_log_in_with_register_form_button(open_login_page, env):
    login_page = open_login_page
    login_from_register = login_page.click_register_link().click_log_in_with_register_form_button().\
        login(env.email, env.password)
    assert login_from_register.is_logout_button_exist(), 'Login with register form button was not clicked'
