import time

import allure
from allure_commons.types import AttachmentType


class Exports:

    def __init__(self, driver):
        self.driver = driver

    def Attachscreenshot(self, Screenshotname):
        allure.attach(self.driver.get_screenshot_as_png(), name=f"{Screenshotname}",
                      attachment_type=AttachmentType.PNG)

    def NavigatetoExports(self):
        try:
            self.driver.find_element_by_xpath("//span[@class='text-sm font-semibold'][normalize-space()='Plan Outputs']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//a[4]//div[1]//div[1]//*[local-name()='svg']").click()
            time.sleep(2)
        except:
            self.Attachscreenshot("NavigatetoExports")


    def Exportdownload(self):
        try:
            self.driver.find_element_by_xpath("//span[normalize-space()='Download Report']").click()
            time.sleep(10)
        except:
            self.Attachscreenshot("Exportdownload")


    def SelectComparisonReport(self):
        try:
            self.driver.find_element_by_xpath("//span[normalize-space()='Comparison Report']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//div[@name='compareScenarioId']//div[@class='ant-select-selector']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//div[@class='ant-select-item-option-content'][normalize-space()='Baseline Scenario']").click()
        except:
            self.Attachscreenshot("SelectComparisonReport")
