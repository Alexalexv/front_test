from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout=timeout).until(EC.visibility_of_element_located(locator))

