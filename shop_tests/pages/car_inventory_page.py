from selenium.webdriver.common.by import By

from shop_tests.pages.base_page import BasePage


class CarInventoryPage(BasePage):
    CAR_INFO_LOCATOR = (By.ID, '//div/h1')
    MODEL_SLIDER_LOCATOR = (By.XPATH, "//div[@class='search_mod_n catalog-search_mod_n']")

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def car_info(self):
        return self.element(CarInventoryPage.CAR_INFO_LOCATOR)

    @property
    def top_categories_slider(self):
        return self.element(CarInventoryPage.MODEL_SLIDER_LOCATOR)

    def page_is_displayed(self):
        return self.top_categories_slider.is_displayed()


