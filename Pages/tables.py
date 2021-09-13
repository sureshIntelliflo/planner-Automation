import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains


class Tables:

    def __init__(self, driver):
        self.driver = driver

    def Attachscreenshot(self, Screenshotname):
        allure.attach(self.driver.get_screenshot_as_png(), name=f"{Screenshotname}",
                      attachment_type=AttachmentType.PNG)

    def NavigatetoTables(self):
        try:
            self.driver.find_element_by_xpath("//div[@class='flex flex-col relative']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//a[3]//div[1]//div[1]//*[local-name()='svg']").click()
            time.sleep(5)
            self.driver.find_element_by_xpath(
                "//tr[@data-row-key='REGULAR']//button[@aria-label='Collapse row']").click()
        except:
            self.Attachscreenshot("NavigatetoTables")


    def NavigatewithinTables(self):
        try:
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
            elif assetSummary.is_displayed():
                assetSummary.click()
                liquidassets = self.driver.find_element_by_xpath(
                    "//span[normalize-space()='Liquid Assets Plus Accessible Pensions']")
                if liquidassets.is_displayed():
                    print("liquid assets plus accessible pensions table is displaying")
                else:
                    print("liquid assets plus accessible pensions table is NOT displaying")
        except:
            self.Attachscreenshot("NavigatewithinTables")

