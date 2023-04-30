import pytest


@pytest.mark.smoke
def test_open_login_page(open_main_page):
    main_page = open_main_page
    login_page = main_page.click_login_button()
    assert login_page.is_login_form_visible(), "Login page was not opened "


@pytest.mark.smoke
def test_open_found_product_page(open_main_page, env):
    main_page = open_main_page
    found_product_page = main_page.set_search_input(env.search_item).click_search_item_button()
    actual_text = found_product_page.get_product_description_text()
    assert actual_text == 'Опис', 'Found product page was not opened'


@pytest.mark.smoke
def test_is_negative_search_result_message_displayed(open_main_page, env):
    main_page = open_main_page
    negative_search = main_page.set_search_input(env.invalid_search_item).click_search_icon()
    assert negative_search.is_negative_search_result_message_displayed(), 'Negative search result was not displayed'


@pytest.mark.regression
def test_open_free_gifts_page(open_main_page):
    main_page = open_main_page
    free_gifts = main_page.click_actions_button().click_free_gifts_button()
    assert free_gifts.is_gifts_list_exist(), 'Free gifts page was not opened'


@pytest.mark.smoke
def test_open_brands_page(open_main_page):
    main_page = open_main_page
    brands_list = main_page.click_brands_button()
    assert brands_list.is_brands_list_exist(), 'Brands page was not opened'


@pytest.mark.regression
def test_open_get_the_look_page(open_main_page):
    main_page = open_main_page
    beauty_look = main_page.click_beauty_blog_button().click_get_the_look_button()
    assert beauty_look.is_fashionable_look_advices_button_exist(), 'Get the look page was not opened'


@pytest.mark.smoke
def test_is_female_button_clickable(open_main_page, env):
    main_page = open_main_page
    newsletter = main_page.set_newsletter_input(env.email)
    assert newsletter.is_female_button_clickable(), 'Female button is not clickable'
