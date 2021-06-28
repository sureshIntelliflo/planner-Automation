from selenium.webdriver.common import by
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Properties:

    def __init__(self, driver):
        self.driver = driver

    PopertiesOption = "//a//span[text()='Properties']"

    def Navigate_to_properties_page(self):
        WebDriverWait(self.driver, 15).until(
            expected_conditions.presence_of_element_located(by.xpath, Properties.PopertiesOption)).click()
