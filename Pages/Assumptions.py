import time

from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Assumptions:

    def __init__(self, driver):
        self.driver = driver

    def NavigatetoAssumptions(self):
        self.driver.find_element_by_xpath("//span[normalize-space()='Plan Inputs']").click()
        self.driver.find_element_by_xpath(
            "//span[@class='text-sm font-normal'][normalize-space()='Assumptions']").click()

    def NavigatetoAssumptionsDetails(self):
        WebDriverWait(self.driver, 2).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH,
                 "//span[normalize-space()='Return Overrides']"))).click()

    def UpdateTaxTaxResidency(self, NewTaxResidency):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH,
                 "//div[@class='ant-select-selector']"))).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(f"//div[contains(text(),'{NewTaxResidency}')]").click()

    def Update_Property_Assumptions(self, NewPropertyInflation):
        time.sleep(2)
        inflactionlock_unlock = self.driver.find_element_by_xpath(
            "//label[@for='inflation_property_rate']//button[@type='button']//span")
        if inflactionlock_unlock.text == "Locked":
            inflactionlock_unlock.click()
            time.sleep(1)
            propertyinflation = self.driver.find_element_by_xpath("//input[@id='inflation_property_rate']")
            propertyinflation.send_keys(Keys.CONTROL)
            propertyinflation.send_keys(Keys.DOWN + "a")
            propertyinflation.send_keys(NewPropertyInflation)

    def UpdateOverrideReturns(self, FirstYearofOverride, GrossReturn, RepeatFrequency):
        OverrideReturns = self.driver.find_element_by_xpath("//button[@id='overrideReturnEnabled']")
        if OverrideReturns.get_attribute("aria-checked") == "false":
            OverrideReturns.click()
            self.driver.find_element_by_xpath("//span[normalize-space()='Add Override Specific Years']").click()
            self.driver.find_element_by_xpath("//input[@id='startYear']").send_keys(FirstYearofOverride)
            self.driver.find_element_by_xpath("//input[@id='grossReturn']").send_keys(GrossReturn)
            self.driver.find_element_by_xpath("//div[@name='frequency']//div[@class='ant-select-selector']").click()
            self.driver.find_element_by_xpath(f"//div[contains(text(),'{RepeatFrequency}')]").click()
            self.driver.find_element_by_xpath("//button//span[normalize-space()='Add Override Return']").click()

        else:
            self.driver.find_element_by_xpath("//span[normalize-space()='Add Override Specific Years']").click()
            self.driver.find_element_by_xpath("//input[@id='startYear']").send_keys(FirstYearofOverride)
            self.driver.find_element_by_xpath("//input[@id='grossReturn']").send_keys(GrossReturn)
            self.driver.find_element_by_xpath("//div[@name='frequency']//div[@class='ant-select-selector']").click()
            self.driver.find_element_by_xpath(f"//div[contains(text(),'{RepeatFrequency}')]").click()
            self.driver.find_element_by_xpath("//button//span[normalize-space()='Add Override Return']").click()

    def SaveAssumptions(self):
        self.driver.find_element_by_xpath("//button[@type='button']//span[contains(text(),'Save Assumptions')]").click()

    def VerifyPropertyAssumption(self, NewPropertyInflation):
        NarrativeProperty = WebDriverWait(self.driver, 2).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH,
                 "//span[normalize-space()='Your changes have been saved']")))

        if NarrativeProperty.is_displayed():
            assert True
        else:
            assert False
