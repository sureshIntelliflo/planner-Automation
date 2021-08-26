import time


class Expenses:
    def __init__(self, driver):
        self.driver = driver

    def NavigatetoExpenses(self):
        self.driver.find_element_by_xpath("//span[normalize-space()='Plan Inputs']").click()
        self.driver.find_element_by_xpath(
            "//span[@class='text-sm font-normal'][normalize-space()='Expenses']").click()

    def AddnewExpense(self, ExpenseCategory):
        self.driver.find_element_by_xpath("//span[normalize-space()='Add Expense']").click()
        self.driver.find_element_by_xpath("//div[@class='ant-select-selector']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(f"//div[contains(text(),'{ExpenseCategory}')]").click()

    def AddExpensesdescription(self, ExpensesDescription):
        self.driver.find_element_by_xpath("//input[@id='expenseDescription']").send_keys(ExpensesDescription)

    def AddExpensesExpenditure(self, EssentialAmount, DiscretionaryAmount):
        self.driver.find_element_by_xpath("//input[@id='expenditure_essentialAmount_amount']").send_keys(EssentialAmount)
        self.driver.find_element_by_xpath("//input[@id='expenditure_discretionaryAmount_amount']").send_keys(DiscretionaryAmount)

    def SaveExpenses(self):
        self.driver.find_element_by_xpath("//button[@type='button']//span[contains(text(),'Add Expense')]").click()
        time.sleep(2)

    def VerifyExpenses(self, ExpensesDescription):
        expenses = self.driver.find_element_by_xpath(f"//span[normalize-space()='{ExpensesDescription}']")
        if expenses.is_displayed():
            assert expenses.text == ExpensesDescription
        else:
            assert False