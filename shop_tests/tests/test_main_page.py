import time

from shop_tests.helpers.data_store import TestData as test


def test_successful_search(main_page):
    """
    1. Navigate to main page
    2. Choose any maker, any model, any car on menu "SELECT YOUR CAR TO SEARCH FOR PARTS"
    3. Click "SEARCH"
    4. Page with parts should be loaded
    """
    car_page = main_page.search_random_car()
    assert car_page.page_is_displayed()


def test_search_with_some_empty_fields(main_page):
    """
    1. Navigate to main menu
    2. Search is not allowed with empty fields
    """
    main_page.search_button_click()
    assert main_page.error_selector_tooltip.is_displayed()

    main_page.choose_random_maker()
    main_page.search_button.click()
    assert main_page.error_selector_tooltip.is_displayed()

    main_page.choose_random_model()
    main_page.search_button.click()
    assert main_page.error_selector_tooltip.is_displayed()


def test_reload_search_fields(main_page):
    """
     1. Navigate to main menu
     2. Ability to reload dropdowns on search menu
    """
    main_page.choose_random_maker()
    main_page.reload_dropdown_button_click()
    assert not main_page.maker_dropdown.is_selected()

    main_page.choose_random_model()
    main_page.reload_dropdown_button_click()
    assert not main_page.maker_dropdown.is_selected() and not main_page.model_dropdown.is_selected()

    main_page.choose_random_car()
    main_page.reload_dropdown_button_click()
    assert not main_page.maker_dropdown.is_selected() and not main_page.model_dropdown.is_selected() and not main_page.car_dropdown.is_selected()


def test_pop_up_displayed(main_page):
    """
    Popup with selectors displayed when user enter unknown car
    """
    main_page.enter_reg_number(test.not_valid_registration_number)
    main_page.click_submit_reg_number_not_valid_data()
    assert main_page.close_button_on_popup.is_displayed()
