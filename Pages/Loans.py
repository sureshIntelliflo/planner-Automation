import time

import allure
from allure_commons.types import AttachmentType


class Loans:

    def __init__(self, driver):
        self.driver = driver

    def Attachscreenshot(self, Screenshotname):
        allure.attach(self.driver.get_screenshot_as_png(), name=f"{Screenshotname}",
                      attachment_type=AttachmentType.PNG)

    def NavigatetoBusiness(self):
        try:
            self.driver.find_element_by_xpath("//span[normalize-space()='Plan Inputs']").click()
            self.driver.find_element_by_xpath(
                "//span[@class='text-sm font-normal'][normalize-space()='Loans']").click()
        except:
            self.Attachscreenshot("NavigatetoBusiness")


    def AddnewLoan(self, LoanDescription):
        try:
            self.driver.find_element_by_xpath("//span[normalize-space()='Add Loan']").click()
            self.driver.find_element_by_xpath("//input[@id='loanDescription']").send_keys(LoanDescription)
        except:
            self.Attachscreenshot("AddnewLoan")


    def LoanDetails(self, loantype, OutstandingBalance, InterestRate, repaymentType):
        try:
            self.driver.find_element_by_xpath(f"//span[normalize-space()='{loantype}']").click()
            self.driver.find_element_by_xpath("//input[@id='amount_amount']").send_keys(OutstandingBalance)
            self.driver.find_element_by_xpath("//input[@id='interestRatePercentage']").send_keys(InterestRate)
            self.driver.find_element_by_xpath("//div[@name='repaymentType']//div[@class='ant-select-selector']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath(f"//div[contains(text(),'{repaymentType}')]").click()
            self.driver.find_element_by_xpath("//div[@name='stopEvent,id']//div[@class='ant-select-selector']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//div[contains(text(),'Pre-Existing')]").click()
        except:
            self.Attachscreenshot("LoanDetails")


    def addloan(self):
        try:
            self.driver.find_element_by_xpath("//button[@type='button']//span[contains(text(),'Add Loan')]").click()
            time.sleep(2)
        except:
            self.Attachscreenshot("addloan")


    def Verifyloan(self, LoanDescription):
        try:
            loan = self.driver.find_element_by_xpath(f"//span[normalize-space()='{LoanDescription}']")
            if loan.is_displayed():
                assert loan.text == LoanDescription
            else:
                self.Attachscreenshot("Verifyloan")
                assert False
        except:
            self.Attachscreenshot("Verifyloan")

