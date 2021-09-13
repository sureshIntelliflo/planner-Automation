import time

import allure
from allure_commons.types import AttachmentType


class Income:
    def __init__(self, driver):
        self.driver = driver

    def Attachscreenshot(self, Screenshotname):
        allure.attach(self.driver.get_screenshot_as_png(), name=f"{Screenshotname}",
                      attachment_type=AttachmentType.PNG)

    def verifyuserhomepage(self):
        try:
            element = self.driver.find_element_by_xpath("//span[text()='Active Scenario']")
            if element.is_displayed():
                print("User is on home page")
            else:
                self.Attachscreenshot("verifyuserhomepage")
                assert False
        except:
            self.Attachscreenshot("verifyuserhomepage")


    def NavigatetoIncome(self):
        try:
            self.driver.find_element_by_xpath("//span[normalize-space()='Plan Inputs']").click()
            self.driver.find_element_by_xpath(
                "//span[@class='text-sm font-normal'][normalize-space()='Income']").click()
        except:
            self.Attachscreenshot("NavigatetoIncome")


    def AddNewIncome(self):
        try:
            AddnewIncome = self.driver.find_element_by_xpath("//span[contains(text(),'Add Income')]")
            if AddnewIncome.is_displayed():
                AddnewIncome.click()
            else:
                print("Add Income options is not displaying")
                self.Attachscreenshot("AddNewIncome")
                assert False
        except:
            self.Attachscreenshot("AddNewIncome")


    def AddIncomeDescription(self, IncomeDescription):
        try:
            NewIncome = self.driver.find_element_by_xpath("//input[@id='incomeDescription']")
            if NewIncome.is_displayed():
                NewIncome.send_keys(IncomeDescription)
            else:
                print("income description box is not displaying")
                self.Attachscreenshot("AddIncomeDescription")
                assert False
        except:
            self.Attachscreenshot("AddIncomeDescription")


    def AddIncomeType(self, IncomeType):
        try:
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@id='incomeType']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath(f"//div[contains(text(),'{IncomeType}')]").click()
        except:
            self.Attachscreenshot("AddIncomeType")


    def Current_Future_income(self, CurrentFutureIncome):
        try:
            time.sleep(1)
            currentfuture = self.driver.find_element_by_xpath("//span[@class='ant-input-group']//label[1]")
            if currentfuture.text == CurrentFutureIncome:
                currentfuture.click()
            else:
                print("unable to locate element income type")
                self.Attachscreenshot("Current_Future_income")
                assert False
        except:
            self.Attachscreenshot("Current_Future_income")


    def AddIncomeAmount(self, IncomeAmount):
        try:
            time.sleep(1)
            amount = self.driver.find_element_by_xpath("//input[@id='amount_amount']")
            amount.send_keys(IncomeAmount)
        except:
            self.Attachscreenshot("AddIncomeAmount")


    def Addincome(self, IncomeDescription):
        try:
            self.driver.find_element_by_xpath(
                "//button[@class='ant-btn ant-btn-link ant-btn-block']//span[contains(text(),'Add')]").click()
            incomenarrative = self.driver.find_element_by_xpath(f"//span[normalize-space()='{IncomeDescription}']")
            if incomenarrative.is_displayed():
                assert incomenarrative.text == IncomeDescription
            else:
                self.Attachscreenshot("Addincome")
                assert False
        except:
            self.Attachscreenshot("Addincome")


    def IncomeExclude(self, IncomeDescription):
        try:
            income = self.driver.find_element_by_xpath(f"//span[normalize-space()='{IncomeDescription}']")
            if income.is_displayed():
                income.click()
                excludefromscenario = self.driver.find_element_by_xpath(
                    "//button[normalize-space()='Exclude from Scenario']")
                if excludefromscenario.is_displayed():
                    excludefromscenario.click()
                    textalert = self.driver.find_element_by_xpath("//span[@class='text-red-800']")
                    assert textalert.text == "This income is excluded from the current scenario"
                    self.driver.find_element_by_xpath(
                        "//button[@type='button']//span[contains(text(),'Save Income')]").click()
                    if self.driver.find_element_by_xpath(
                            f"//span[@class='ant-tag ant-tag-red']//preceding::span[text()= '{IncomeDescription}']").is_displayed():
                        print("Income is excluded from scenario")
                    else:
                        print("income is not excluded from scenario")
                        self.Attachscreenshot("IncomeExclude")
            else:
                print("unable to locate the added income")
                self.Attachscreenshot("IncomeExclude")
                assert False
        except:
            self.Attachscreenshot("IncomeExclude")

