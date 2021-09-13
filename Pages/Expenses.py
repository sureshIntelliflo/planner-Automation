import time

import allure
from allure_commons.types import AttachmentType


class Expenses:
    def __init__(self, driver):
        self.driver = driver

    def Attachscreenshot(self, Screenshotname):
        allure.attach(self.driver.get_screenshot_as_png(), name=f"{Screenshotname}",
                      attachment_type=AttachmentType.PNG)

    def NavigatetoExpenses(self):
        try:
            self.driver.find_element_by_xpath("//span[normalize-space()='Plan Inputs']").click()
            self.driver.find_element_by_xpath(
                "//span[@class='text-sm font-normal'][normalize-space()='Expenses']").click()
        except:
            self.Attachscreenshot("DeleteClient")


    def AddnewExpense(self, ExpenseCategory):
        try:
            self.driver.find_element_by_xpath("//span[normalize-space()='Add Expense']").click()
            self.driver.find_element_by_xpath("//div[@class='ant-select-selector']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath(f"//div[contains(text(),'{ExpenseCategory}')]").click()
        except:
            self.Attachscreenshot("AddnewExpense")


    def AddExpensesdescription(self, ExpensesDescription):
        try:
            self.driver.find_element_by_xpath("//input[@id='expenseDescription']").send_keys(ExpensesDescription)
        except:
            self.Attachscreenshot("AddnewExpense")


    def AddExpensesExpenditure(self, EssentialAmount, DiscretionaryAmount):
        try:
            self.driver.find_element_by_xpath("//input[@id='expenditure_essentialAmount_amount']").send_keys(EssentialAmount)
            self.driver.find_element_by_xpath("//input[@id='expenditure_discretionaryAmount_amount']").send_keys(DiscretionaryAmount)
        except:
            self.Attachscreenshot("AddExpensesExpenditure")


    def SaveExpenses(self):
        try:
            self.driver.find_element_by_xpath("//button[@type='button']//span[contains(text(),'Add Expense')]").click()
            time.sleep(2)
        except:
            self.Attachscreenshot("SaveExpenses")


    def VerifyExpenses(self, ExpensesDescription):
        try:
            expenses = self.driver.find_element_by_xpath(f"//span[normalize-space()='{ExpensesDescription}']")
            if expenses.is_displayed():
                assert expenses.text == ExpensesDescription
            else:
                self.Attachscreenshot("VerifyExpenses")
                assert False
        except:
            self.Attachscreenshot("VerifyExpenses")
