import time
from random import randint

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from shop_tests.pages.base_page import BasePage
from shop_tests.helpers.data_store import URL
import shop_tests.pages.car_inventory_page as car_page


class MainPage(BasePage):

    MAKER_DROPDOWN_LOCATOR = (By.ID, 'form_maker_id')
    MODEL_DROPDOWN_LOCATOR = (By.ID, 'form_model_id')
    MODEL_OPTIONS_LOCATOR = (By.XPATH, '//select[@id="form_model_id"]/optgroup')
    CAR_DROPDOWN_LOCATOR = (By.ID, 'form_car_id')
    CAR_OPTIONS_LOCATOR = (By.XPATH, '//select[@id="form_car_id"]/optgroup')
    SUBMIT_SEARCH_BUTTON_LOCATOR = (By.XPATH, "//div/div[@class='block-select-car__button']/a")
    COOKIES_ACCEPT_LOCATOR = (By.ID, '1')
    SELECTOR_ERROR_LOCATOR = (By.XPATH, "//div[@class='popup-error-select validation-tooltip']")
    RELOAD_DROPDOWNS_BUTTON = (By.XPATH, "//a[@id='reset_selector_form']")
    REGISTRATION_NUMBER_INPUT_LOCATOR = (By.ID, "kba1")
    SUBMIT_REGISTRATION_BUTTON_LOCATOR = (By.XPATH, "//a[@class='submit search_button kba_submit']")
    CLOSE_BUTTON_ON_POP_UP_LOCATOR = (By.XPATH, "//a[@class='back']")

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def maker_dropdown(self):
        return self.element(MainPage.MAKER_DROPDOWN_LOCATOR)

    @property
    def model_dropdown(self):
        return self.element(MainPage.MODEL_DROPDOWN_LOCATOR)

    @property
    def car_dropdown(self):
        return self.element(MainPage.CAR_DROPDOWN_LOCATOR)

    @property
    def search_button(self):
        return self.element(MainPage.SUBMIT_SEARCH_BUTTON_LOCATOR)

    @property
    def reload_dropdown_button(self):
        return self.element(MainPage.RELOAD_DROPDOWNS_BUTTON)

    @property
    def error_selector_tooltip(self):
        return self.element(MainPage.SELECTOR_ERROR_LOCATOR)

    @property
    def registration_number_input(self):
        return self.element(MainPage.REGISTRATION_NUMBER_INPUT_LOCATOR)

    @property
    def submit_reg_number_button(self):
        return self.element(MainPage.SUBMIT_REGISTRATION_BUTTON_LOCATOR)

    @property
    def close_button_on_popup(self):
        return self.element(MainPage.CLOSE_BUTTON_ON_POP_UP_LOCATOR)

    def accept_cookies(self):
        accept_cookies = self.element(MainPage.COOKIES_ACCEPT_LOCATOR)
        accept_cookies.click()
        return self

    def navigate(self):
        self.driver.get(URL.BASE_PAGE)
        self.accept_cookies()

    def choose_random_selector(self, element):
        selector = Select(element)
        length = len(selector.options)
        selector_index = randint(1, length - 1)
        selector.select_by_index(selector_index)
        return self

    def choose_random_maker(self):
        self.choose_random_selector(self.maker_dropdown)
        return self

    def choose_random_model(self):
        self.choose_random_maker()
        self.element(MainPage.MODEL_OPTIONS_LOCATOR)
        self.choose_random_selector(self.model_dropdown)
        return self

    def choose_random_car(self):
        self.choose_random_model()
        self.element(self.CAR_OPTIONS_LOCATOR)
        self.choose_random_selector(self.car_dropdown)
        return self

    def search_button_click(self):
        self.search_button.click()

    def reload_dropdown_button_click(self):
        self.reload_dropdown_button.click()

    def search_random_car(self):
        self.choose_random_car()
        self.search_button_click()
        return car_page.CarInventoryPage(self.driver)

    def enter_reg_number(self, number):
        self.registration_number_input.send_keys(number)
        return self

    def click_submit_reg_number_not_valid_data(self):
        self.submit_reg_number_button.click()
        return self


