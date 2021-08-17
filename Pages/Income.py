import time


class Income:
    def __init__(self, driver):
        self.driver = driver

    def verifyuserhomepage(self):
        element = self.driver.find_element_by_xpath("//span[text()='Active Scenario']")
        if element.is_displayed():
            print("User is on home page")

    def NavigatetoIncome(self):
        self.driver.find_element_by_xpath("//span[normalize-space()='Plan Inputs']").click()
        self.driver.find_element_by_xpath(
            "//span[@class='text-sm font-normal'][normalize-space()='Income']").click()

    def AddNewIncome(self):
        AddnewIncome = self.driver.find_element_by_xpath("//span[contains(text(),'Add Income')]")
        if AddnewIncome.is_displayed():
            AddnewIncome.click()
        else:
            print("Add Income options is not displaying")

    def AddIncomeDescription(self, IncomeDescription):
        NewIncome = self.driver.find_element_by_xpath("//input[@id='incomeDescription']")
        if NewIncome.is_displayed():
            NewIncome.send_keys(IncomeDescription)
        else:
            print("income description box is not displaying")

    def AddIncomeType(self, IncomeType):
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='incomeType']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(f"//div[contains(text(),'{IncomeType}')]").click()



    def Current_Future_income(self, CurrentFutureIncome):
        time.sleep(1)
        currentfuture = self.driver.find_element_by_xpath("//span[@class='ant-input-group']//label[1]")
        if currentfuture.text == CurrentFutureIncome:
            currentfuture.click()
        else:
            print("unable to locate element income type")

    def AddIncomeAmount(self, IncomeAmount):
        time.sleep(1)
        amount = self.driver.find_element_by_xpath("//input[@id='amount_amount']")
        amount.send_keys(IncomeAmount)

    def Addincome(self, IncomeDescription):
        self.driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-link ant-btn-block']//span[contains(text(),'Add')]").click()
        incomenarrative = self.driver.find_element_by_xpath(f"//span[normalize-space()='{IncomeDescription}']")
        if incomenarrative.is_displayed():
            assert incomenarrative.text == IncomeDescription

    def IncomeExclude(self, IncomeDescription):

        income = self.driver.find_element_by_xpath(f"//span[normalize-space()='{IncomeDescription}']")
        if income.is_displayed():
            income.click()
            excludefromscenario = self.driver.find_element_by_xpath("//button[normalize-space()='Exclude from Scenario']")
            if excludefromscenario.is_displayed():
                excludefromscenario.click()
                textalert = self.driver.find_element_by_xpath("//span[@class='text-red-800']")
                assert textalert.text == "This income is excluded from the current scenario"
                self.driver.find_element_by_xpath("//button[@type='button']//span[contains(text(),'Save Income')]").click()
                if self.driver.find_element_by_xpath(f"//span[@class='ant-tag ant-tag-red']//preceding::span[text()= '{IncomeDescription}']").is_displayed():
                    print("Income is excluded from scenario")
                else:
                    print("income is not excluded from scenario")
        else:
            print("unable to locate the added income")
