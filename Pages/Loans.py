import time


class Loans:

    def __init__(self, driver):
        self.driver = driver


    def NavigatetoBusiness(self):
        self.driver.find_element_by_xpath("//span[normalize-space()='Plan Inputs']").click()
        self.driver.find_element_by_xpath(
            "//span[@class='text-sm font-normal'][normalize-space()='Loans']").click()

    def AddnewLoan(self, LoanDescription):
        self.driver.find_element_by_xpath("//span[normalize-space()='Add Loan']").click()
        self.driver.find_element_by_xpath("//input[@id='loanDescription']").send_keys(LoanDescription)

    def LoanDetails(self, loantype, OutstandingBalance, InterestRate, repaymentType):
        self.driver.find_element_by_xpath(f"//span[normalize-space()='{loantype}']").click()
        self.driver.find_element_by_xpath("//input[@id='amount_amount']").send_keys(OutstandingBalance)
        self.driver.find_element_by_xpath("//input[@id='interestRatePercentage']").send_keys(InterestRate)
        self.driver.find_element_by_xpath("//div[@name='repaymentType']//div[@class='ant-select-selector']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(f"//div[contains(text(),'{repaymentType}')]").click()
        self.driver.find_element_by_xpath("//div[@name='stopEvent,id']//div[@class='ant-select-selector']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[contains(text(),'Pre-Existing')]").click()

    def addloan(self):
        self.driver.find_element_by_xpath("//button[@type='button']//span[contains(text(),'Add Loan')]").click()
        time.sleep(2)

    def Verifyloan(self, LoanDescription):
        loan = self.driver.find_element_by_xpath(f"//span[normalize-space()='{LoanDescription}']")
        if loan.is_displayed():
            assert loan.text == LoanDescription
        else:
            assert False
