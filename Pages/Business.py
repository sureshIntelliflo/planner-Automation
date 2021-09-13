import time

import allure
from allure_commons.types import AttachmentType


class Business:

    def __init__(self, driver):
        self.driver = driver

    def Attachscreenshot(self, Screenshotname):
        allure.attach(self.driver.get_screenshot_as_png(), name=f"{Screenshotname}", attachment_type=AttachmentType.PNG)

    def NavigatetoBusiness(self):
        try:

            self.driver.find_element_by_xpath("//span[normalize-space()='Plan Inputs']").click()
            self.driver.find_element_by_xpath(
                "//span[@class='text-sm font-normal'][normalize-space()='Businesses']").click()
        except:
            self.Attachscreenshot("NavigatetoBusiness")


    def AddNewBusiness(self, BusinessDescription):
        try:
            self.driver.find_element_by_xpath("//span[normalize-space()='Add Business']").click()
            self.driver.find_element_by_xpath("//input[@id='businessDescription']").send_keys(BusinessDescription)
        except:
            self.Attachscreenshot("AddNewBusiness")

    def BusinessDetail(self, BusinessType, BusinessValue, AnnualIncreasepercentage, BaseCostforCGT, ValuationBasis):
        try:
            self.driver.find_element_by_xpath(f"//span[normalize-space()='{BusinessType}']").click()
            self.driver.find_element_by_xpath("//input[@id='value_amount']").send_keys(BusinessValue)
            self.driver.find_element_by_xpath("//input[@id='increasePostStartPercentage']").send_keys(
                AnnualIncreasepercentage)
            self.driver.find_element_by_xpath("//input[@id='baseCostForCgt_amount']").send_keys(BaseCostforCGT)
            self.driver.find_element_by_xpath("//input[@id='hasBusinessAssetDisposalRelief']").click()
            self.driver.find_element_by_xpath(f"(//input[@value='{ValuationBasis}']//following::span)[2]").click()
        except:
            self.Attachscreenshot("BusinessDetail")


    def BusinessSaleEvent(self, SaleEvent):
        try:
            self.driver.find_element_by_xpath("//button[@id='saleEnabled']").click()
            self.driver.find_element_by_xpath("//div[@class='ant-select-selector']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath(f"//div[contains(text(),'{SaleEvent}')]").click()
        except:
            self.Attachscreenshot("BusinessSaleEvent")


    def BusinessDividends(self, DividendFrequency, DividendAmount, IncreasePerstart, PeriodSetby):
        try:
            self.driver.find_element_by_xpath("//button[@id='dividendsEnabled']").click()
            self.driver.find_element_by_xpath("//span[normalize-space()='Add Business Dividend']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath(f"//span[normalize-space()='{DividendFrequency}']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath(
                "//span[normalize-space()='Dividend Amount']//following::input[@id='value_amount']").send_keys(
                DividendAmount)
            self.driver.find_element_by_xpath("//input[@id='increasePreStartPercentage']").send_keys(IncreasePerstart)
            self.driver.find_element_by_xpath(f"//span[normalize-space()='{PeriodSetby}']").click()
            time.sleep(1)

            self.driver.find_element_by_xpath("//span[normalize-space()='Add Dividend']").click()
        except:
            self.Attachscreenshot("BusinessDividends")


    def DeathOptions(self):
        try:
            self.driver.find_element_by_xpath("//input[@id='qualifiesForBusinessRelief']").click()
        except:
            self.Attachscreenshot("DeathOptions")


    def AddBusiness(self):
        try:
            self.driver.find_element_by_xpath("//button[@type='button']//span[contains(text(),'Add Business')]").click()
        except:
            self.Attachscreenshot("AddBusiness")


    def VerifyBusiness(self, BusinessDescription):
        try:
            business = self.driver.find_element_by_xpath(f"//span[normalize-space()='{BusinessDescription}']")
            if business.is_displayed():
                assert business.text == BusinessDescription
            else:
                self.Attachscreenshot("VerifyBusiness")
                assert False
        except:
            self.Attachscreenshot("VerifyBusiness")

