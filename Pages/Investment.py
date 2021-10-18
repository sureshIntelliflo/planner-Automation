import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class investments:

    def __init__(self, driver):
        self.driver = driver

    def Attachscreenshot(self, Screenshotname):
        allure.attach(self.driver.get_screenshot_as_png(), name=f"{Screenshotname}",
                      attachment_type=AttachmentType.PNG)

    def Verify_user_in_home_page(self):
        try:
            element = self.driver.find_element_by_xpath("//span[normalize-space()='Client Settings']")
            if element.is_displayed():
                print("User is on home page")
            else:
                self.Attachscreenshot("Verify_user_in_home_page")
                assert False
        except:
            self.Attachscreenshot("Verify_user_in_home_page")


    def NavigatetoInvestment(self):
        try:
            self.driver.find_element_by_xpath("//span[normalize-space()='Plan Inputs']").click()
            self.driver.find_element_by_xpath(
                "//span[@class='text-sm font-normal'][normalize-space()='Investments']").click()
        except:
            self.Attachscreenshot("NavigatetoInvestment")


    def AddInvestments(self, InvestmentDescription):
        try:
            AddProperty = self.driver.find_element_by_xpath("//button//span[text()='Add Investment']")
            if AddProperty.is_displayed():
                AddProperty.click()
            self.driver.find_element_by_xpath("//input[@id='investmentDescription']").send_keys(InvestmentDescription)
        except:
            self.Attachscreenshot("AddInvestments")


    def investmentType(self, InvestmentType):
        try:
            invest_type = self.driver.find_element_by_xpath("//input[@id='investmentType']")
            invest_type.click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@id='investmentType']").send_keys(InvestmentType)
            type = self.driver.find_element_by_xpath(f"//div[contains(text(),'{InvestmentType}')]")
            if type.is_displayed():
                type.click()
            else:
                self.Attachscreenshot("investmentType")
                assert False
        except:
            self.Attachscreenshot("investmentType")


    def select_preexisting(self, Investment):
        try:
            time.sleep(1)
            propertydetails = self.driver.find_element_by_xpath(f"//span[normalize-space()='{Investment}']")
            propertydetails.click()
        except:
            self.Attachscreenshot("select_preexisting")

    def currentvalue(self, CurrentValue):
        try:
            self.driver.find_element_by_xpath("//input[@id='value_amount']").send_keys(CurrentValue)
        except:
            self.Attachscreenshot("currentvalue")


    def returns(self, AttitudetoRisk, GrossReturn, Interest, Dividends, Growth):
        try:
            riskdropdown = self.driver.find_element_by_xpath("//input[@id='riskProfileId']")
            riskdropdown.click()
            risktype = self.driver.find_element_by_xpath(
                f"//div[@class='ant-select-item-option-content'][normalize-space()='{AttitudetoRisk}']")
            time.sleep(1)
            if AttitudetoRisk == "High":
                risktype.click()
            elif AttitudetoRisk == "Cash":
                risktype.click()
            elif AttitudetoRisk == "Custom":
                risktype.click()
                self.driver.find_element_by_xpath("//input[@id='grossReturn_rate']").send_keys(GrossReturn)
                self.driver.find_element_by_xpath("//input[@id='grossReturn_allocation_interest']").send_keys(Interest)
                self.driver.find_element_by_xpath("//input[@id='grossReturn_allocation_dividend']").send_keys(Dividends)
                self.driver.find_element_by_xpath("//input[@id='grossReturn_allocation_growth']").send_keys(Growth)
        except:
            self.Attachscreenshot("returns")


    def Investmentadd(self, InvestmentDescription):
        try:
            self.driver.find_element_by_xpath(
                "//button[@type='button']//span[contains(text(),'Add Investment')]").click()
            investmentnarrative = self.driver.find_element_by_xpath(
                f"//span[normalize-space()='{InvestmentDescription}']")
            if investmentnarrative.is_displayed():
                assert investmentnarrative.text == InvestmentDescription
            else:
                self.Attachscreenshot("Investmentadd")
                assert False
        except:
            self.Attachscreenshot("Investmentadd")


    def excludefrombaseline(self, InvestmentDescription):
        try:
            investmentnarrative = self.driver.find_element_by_xpath(
                f"//span[normalize-space()='{InvestmentDescription}']")
            if investmentnarrative.is_displayed():
                investmentnarrative.click()
                excludeplan = self.driver.find_element_by_xpath("//button[normalize-space()='Exclude from Scenario']")
                excludeplan.click()
                textalert = self.driver.find_element_by_xpath("//span[@class='text-red-800']")
                assert textalert.text == "This investment is excluded from the current scenario"
            else:
                self.Attachscreenshot("excludefrombaseline")
                assert False
        except:
            self.Attachscreenshot("excludefrombaseline")


    def saveInvestment(self):
        try:
            self.driver.find_element_by_xpath(
                "//button[@type='button']//span[contains(text(),'Save Investment')]").click()
        except:
            self.Attachscreenshot("saveInvestment")

    def verifyinvestmentexclude(self, InvestmentDescription):
        try:
            investmentplanexclude = self.driver.find_element_by_xpath(
                f"//span[@class='ant-tag ant-tag-red']//preceding-sibling::span[text()='{InvestmentDescription}']")
            if investmentplanexclude.is_displayed():
                exclude = self.driver.find_element_by_xpath("//span[@class='ant-tag ant-tag-red']")
                assert exclude.text == "EXCLUDED FROM SCENARIO"
            else:
                self.Attachscreenshot("verifyinvestmentexclude")
                assert False

        except:
            self.Attachscreenshot("verifyinvestmentexclude")


    def createscenario(self, ScenarioName, ScenarioDescription):
        try:
            self.driver.find_element_by_xpath(
                "//div[@class='flex items-center hidden lg:block justify-center']//span[@class='hidden md:block mr-1 text-primary-500 text-sm font-semibold'][normalize-space()='Active Scenario']").click()
            time.sleep(1)
            AddScenariobtn = self.driver.find_element_by_xpath("//button//span[text()='Add scenario']")
            if AddScenariobtn.is_displayed():
                AddScenariobtn.click()
            time.sleep(1)
            addscenariodialog = self.driver.find_element_by_xpath("//div[@class='ant-modal-title']")
            if addscenariodialog.is_displayed():
                self.driver.find_element_by_xpath("//input[@id='name']").send_keys(ScenarioName)
                self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys(ScenarioDescription)
                self.driver.find_element_by_xpath("//span[normalize-space()='Add Scenario']").click()
                verifyscenario = self.driver.find_element_by_xpath(
                    f"//div[@class='flex items-center hidden lg:block justify-center']//span[@class='text-gray-900 text-sm'][normalize-space()='{ScenarioName}']")
                assert verifyscenario.text == ScenarioName
            else:
                self.Attachscreenshot("createscenario")
                assert False
        except:
            self.Attachscreenshot("createscenario")


    def excludeplantoinclude(self, InvestmentDescription):
        try:
            investmentplanexclude = self.driver.find_element_by_xpath(
                f"//span[@class='ant-tag ant-tag-red']//preceding-sibling::span[text()='{InvestmentDescription}']")
            if investmentplanexclude.is_displayed():
                investmentplanexclude.click()
                self.driver.find_element_by_xpath("//button[normalize-space()='Include in Scenario']").click()
            else:
                self.Attachscreenshot("excludeplantoinclude")
                assert False
        except:
            self.Attachscreenshot("excludeplantoinclude")


    def Investmentcontributions(self, contributionstype, contributionamount):
        try:
            self.driver.find_element_by_xpath("//button[@id='contributionsEnabled']").click()
            type = self.driver.find_element_by_xpath(f"//span[normalize-space()='{contributionstype}']")
            if type.is_displayed():
                type.click()
                self.driver.find_element_by_xpath("//input[@id='contributions_amount_amount']").send_keys(
                    contributionamount)
            else:
                self.Attachscreenshot("Investmentcontributions")
                assert False
        except:
            self.Attachscreenshot("Investmentcontributions")


    def withdrowls_custom(self, WithdrawalAmount):
        try:
            self.driver.find_element_by_xpath("//button[@id='withdrawalsEnabled']").click()
            withdrawalmethod = self.driver.find_element_by_xpath(
                "//div[@name='withdrawals,withdrawalType']//div[@class='ant-select-selector']")
            if withdrawalmethod.is_displayed():
                withdrawalmethod.click()
                self.driver.find_element_by_xpath("//div[contains(text(),'Amount')]").click()
                self.driver.find_element_by_xpath("//input[@id='withdrawals_amount_amount']").send_keys(
                    WithdrawalAmount)
                self.driver.find_element_by_xpath("//input[@id='withdrawals_payOutInterest']").click()
                self.driver.find_element_by_xpath("//span[contains(text(),'Payout Dividends')]").click()
            else:
                self.Attachscreenshot("withdrowls_custom")
                assert False
        except:
            self.Attachscreenshot("withdrowls_custom")


    def withdrawals_sell_whole_investment(self):
        try:
            self.driver.find_element_by_xpath("//button[@id='saleEventEnabled']").click()
            sellevent = self.driver.find_element_by_xpath(
                "//div[@name='saleEvent,id']//div[@class='ant-select-selector']")
            if sellevent.is_displayed():
                sellevent.click()
                time.sleep(1)
                self.driver.find_element_by_xpath("//div[contains(text(),'Forever')]").click()
                assert True
            else:
                self.Attachscreenshot("withdrawals_sell_whole_investment")
                assert False
        except:
            self.Attachscreenshot("withdrawals_sell_whole_investment")


    def specificcharge(self):
        try:
            self.driver.find_element_by_xpath("//button[@id='chargesEnabled']").click()
            self.driver.find_element_by_xpath(
                "//span[contains(text(),'Treat financial planning fee as an expense')]").click()
        except:
            self.Attachscreenshot("specificcharge")


    def deathoptions(self):
        try:
            self.driver.find_element_by_xpath("//span[contains(text(),'Business Relief Qualifying')]").click()
        except:
            self.Attachscreenshot("deathoptions")


    def verifyinvestmentinclude(self, InvestmentDescription):
        try:
            investmentplaninclude = self.driver.find_element_by_xpath(
                f"//span[normalize-space()='{InvestmentDescription}']//following::span[@class='line-through']")
            if investmentplaninclude.is_displayed():
                includeInscenario = self.driver.find_element_by_xpath("//span[@class='line-through']")
                assert includeInscenario.text == "EXCLUDED IN BASELINE"
            else:
                self.Attachscreenshot("verifyinvestmentinclude")
                assert False
        except:
            self.Attachscreenshot("verifyinvestmentinclude")


    def investmentreturn(self, Returns):
        try:
            self.driver.find_element_by_xpath("//input[@id='grossReturn_rate']").send_keys(Returns)
        except:
            self.Attachscreenshot("investmentreturn")


    def verifyInvestments(self, InvestmentDescription):
        try:
            savedinvestment = self.driver.find_element_by_xpath(f"//span[normalize-space()='{InvestmentDescription}']")
            if savedinvestment.is_displayed():
                assert savedinvestment.text == InvestmentDescription
            else:
                self.Attachscreenshot("verifyInvestments")
                assert False
        except:
            self.Attachscreenshot("verifyInvestments")


    def Contributions(self, Contribution_Amount):
        try:
            self.driver.find_element_by_xpath("//button[@id='contributionsEnabled']").click()
            contributionamount = self.driver.find_element_by_xpath("//input[@id='contributions_amount_amount']")
            if contributionamount.is_displayed():
                contributionamount.send_keys(Contribution_Amount)
            else:
                print("unable to add contributions")
                self.Attachscreenshot("Contributions")
                assert False
        except:
            self.Attachscreenshot("Contributions")


    def linkContribution(self, contributionstype, InvestmentDescription1):
        try:
            self.driver.find_element_by_xpath("//button[@id='contributionsEnabled']").click()
            time.sleep(1)
            type = self.driver.find_element_by_xpath(f"//span[normalize-space()='{contributionstype}']")
            if type.is_displayed():
                type.click()
                self.driver.find_element_by_xpath(
                    "//div[@name='bedAndIsaContributions,investment,id']//div[@class='ant-select-selector']").click()
                self.driver.find_element_by_xpath(f"//div[contains(text(),'{InvestmentDescription1}')]").click()
            else:
                self.Attachscreenshot("linkContribution")
                assert False
        except:
            self.Attachscreenshot("linkContribution")

