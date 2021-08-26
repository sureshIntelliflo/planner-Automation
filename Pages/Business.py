import time


class Business:

    def __init__(self, driver):
        self.driver = driver

    def NavigatetoBusiness(self):
        self.driver.find_element_by_xpath("//span[normalize-space()='Plan Inputs']").click()
        self.driver.find_element_by_xpath(
            "//span[@class='text-sm font-normal'][normalize-space()='Businesses']").click()
    def AddNewBusiness(self, BusinessDescription):
        self.driver.find_element_by_xpath("//span[normalize-space()='Add Business']").click()
        self.driver.find_element_by_xpath("//input[@id='businessDescription']").send_keys(BusinessDescription)

    def BusinessDetail(self, BusinessType, BusinessValue, AnnualIncreasepercentage, BaseCostforCGT, ValuationBasis):
        self.driver.find_element_by_xpath(f"//span[normalize-space()='{BusinessType}']").click()
        self.driver.find_element_by_xpath("//input[@id='value_amount']").send_keys(BusinessValue)
        self.driver.find_element_by_xpath("//input[@id='increasePostStartPercentage']").send_keys(AnnualIncreasepercentage)
        self.driver.find_element_by_xpath("//input[@id='baseCostForCgt_amount']").send_keys(BaseCostforCGT)
        self.driver.find_element_by_xpath("//input[@id='hasBusinessAssetDisposalRelief']").click()
        self.driver.find_element_by_xpath(f"(//input[@value='{ValuationBasis}']//following::span)[2]").click()

    def BusinessSaleEvent(self, SaleEvent):
        self.driver.find_element_by_xpath("//button[@id='saleEnabled']").click()
        self.driver.find_element_by_xpath("//div[@class='ant-select-selector']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(f"//div[contains(text(),'{SaleEvent}')]").click()

    def BusinessDividends(self, DividendFrequency, DividendAmount, IncreasePerstart, PeriodSetby):
        self.driver.find_element_by_xpath("//button[@id='dividendsEnabled']").click()
        self.driver.find_element_by_xpath("//span[normalize-space()='Add Business Dividend']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(f"//span[normalize-space()='{DividendFrequency}']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//span[normalize-space()='Dividend Amount']//following::input[@id='value_amount']").send_keys(DividendAmount)
        self.driver.find_element_by_xpath("//input[@id='increasePreStartPercentage']").send_keys(IncreasePerstart)
        self.driver.find_element_by_xpath(f"//span[normalize-space()='{PeriodSetby}']").click()
        time.sleep(1)

        self.driver.find_element_by_xpath("//span[normalize-space()='Add Dividend']").click()

    def DeathOptions(self):

        self.driver.find_element_by_xpath("//input[@id='qualifiesForBusinessRelief']").click()

    def AddBusiness(self):
        self.driver.find_element_by_xpath("//button[@type='button']//span[contains(text(),'Add Business')]").click()

    def VerifyBusiness(self, BusinessDescription):
        business = self.driver.find_element_by_xpath(f"//span[normalize-space()='{BusinessDescription}']")
        if business.is_displayed():
            assert business.text == BusinessDescription

