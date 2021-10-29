import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Tables:

    def __init__(self, driver):
        self.driver = driver

    def Attachscreenshot(self, Screenshotname):
        allure.attach(self.driver.get_screenshot_as_png(), name=f"{Screenshotname}",
                      attachment_type=AttachmentType.PNG)

    def NavigatetoTables(self):

        # self.driver.find_element_by_xpath("//span[@class='text-sm font-semibold'][normalize-space()='Plan Outputs']").click()

        WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH,
                 "//a[@class='NavigationSidebarItem_navlink__2ChYw NavigationSidebarItem_header__3cFRA']//span[text()='Plan Inputs']"))).click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, "//span[@class='block leading-tight text-xs']"))).click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, "//span[normalize-space()='Liquid Assets']"))).click()

        self.driver.find_element_by_xpath("//span[normalize-space()='Events']").click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, "//button[@title='Next graph']"))).click()

    def NavigatewithinTables(self):

        CashflowTable = self.driver.find_element_by_xpath("//div[@id='rc-tabs-1-tab-cashflow-summary']")
        assetSummary = self.driver.find_element_by_xpath("//div[@id='rc-tabs-4-tab-asset-summary']")

        if CashflowTable.is_displayed():
            CashflowTable.click()
            cashflowtable = self.driver.find_element_by_xpath(
                "//span[@title='Cashflow Summary']//following::table//tbody")
            if cashflowtable.is_displayed():
                self.driver.find_element_by_xpath("//span[normalize-space()='Regular']").click()
            else:
                print("Failed due to some error")
                self.Attachscreenshot("NavigatewithinTables")
        elif assetSummary.is_displayed():
            assetSummary.click()
            liquidassets = self.driver.find_element_by_xpath(
                "//span[normalize-space()='Liquid Assets Plus Accessible Pensions']")
            if liquidassets.is_displayed():
                print("liquid assets plus accessible pensions table is displaying")
            else:
                print("liquid assets plus accessible pensions table is NOT displaying")
                self.Attachscreenshot("NavigatewithinTables")
