import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class investments:

    def __init__(self, driver):
        self.driver = driver

    def Verify_user_in_home_page(self):
        element = self.driver.find_element_by_xpath("//span[text()='Active Scenario']")
        if element.is_displayed():
            print("User is on home page")

    def NavigatetoInvestment(self):

        self.driver.find_element_by_xpath("//span[normalize-space()='Plan Inputs']").click()
        self.driver.find_element_by_xpath(
            "//span[@class='text-sm font-normal'][normalize-space()='Investments']").click()

    def AddInvestments(self, InvestmentDescription):
        AddProperty = self.driver.find_element_by_xpath("//button//span[text()='Add Investment']")
        if AddProperty.is_displayed():
            AddProperty.click()
        self.driver.find_element_by_xpath("//input[@id='investmentDescription']").send_keys(InvestmentDescription)

    def investmentType(self, InvestmentType):
        invest_type= self.driver.find_element_by_xpath("//input[@id='investmentType']")
        invest_type.click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='investmentType']").send_keys(InvestmentType)
        type = self.driver.find_element_by_xpath(f"//div[contains(text(),'{InvestmentType}')]")
        if type.is_displayed():
            type.click()



    def select_preexisting(self, Investment):
        time.sleep(1)
        propertydetails = self.driver.find_element_by_xpath(f"//span[normalize-space()='{Investment}']")
        propertydetails.click()

    def currentvalue(self, CurrentValue):
        self.driver.find_element_by_xpath("//input[@id='value_amount']").send_keys(CurrentValue)

    def returns(self, AttitudetoRisk, GrossReturn, Interest, Dividends, Growth):
        riskdropdown = self.driver.find_element_by_xpath("//input[@id='riskProfileId']")
        riskdropdown.click()
        risktype = self.driver.find_element_by_xpath(f"//div[@class='ant-select-item-option-content'][normalize-space()='{AttitudetoRisk}']")
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

    def Investmentadd(self, InvestmentDescription):

        self.driver.find_element_by_xpath("//button[@type='button']//span[contains(text(),'Add Investment')]").click()
        investmentnarrative = self.driver.find_element_by_xpath(f"//span[normalize-space()='{InvestmentDescription}']")
        if investmentnarrative.is_displayed():
            assert investmentnarrative.text == InvestmentDescription

    def excludefrombaseline(self, InvestmentDescription):
        investmentnarrative = self.driver.find_element_by_xpath(f"//span[normalize-space()='{InvestmentDescription}']")
        if investmentnarrative.is_displayed():
            investmentnarrative.click()
            excludeplan = self.driver.find_element_by_xpath("//button[normalize-space()='Exclude from Scenario']")
            excludeplan.click()
            textalert = self.driver.find_element_by_xpath("//span[@class='text-red-800']")
            assert textalert.text == "This investment is excluded from the current scenario"


    def saveInvestment(self):
        self.driver.find_element_by_xpath("//button[@type='button']//span[contains(text(),'Save Investment')]").click()

    def verifyinvestmentexclude(self, InvestmentDescription):
        investmentplanexclude = self.driver.find_element_by_xpath(f"//span[@class='ant-tag ant-tag-red']//preceding-sibling::span[text()='{InvestmentDescription}']")
        if investmentplanexclude.is_displayed():
            exclude = self.driver.find_element_by_xpath("//span[@class='ant-tag ant-tag-red']")
            assert exclude.text == "EXCLUDED FROM SCENARIO"

    def createscenario(self, ScenarioName, ScenarioDescription):
        self.driver.find_element_by_xpath("//div[@class='flex items-center hidden lg:block justify-center']//span[@class='hidden md:block mr-1 text-primary-500 text-sm font-semibold'][normalize-space()='Active Scenario']").click()
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
            verifyscenario = self.driver.find_element_by_xpath(f"//div[@class='flex items-center hidden lg:block justify-center']//span[@class='text-gray-900 text-sm'][normalize-space()='{ScenarioName}']")
            assert verifyscenario.text == ScenarioName

    def excludeplantoinclude(self, InvestmentDescription):
        investmentplanexclude = self.driver.find_element_by_xpath(
            f"//span[@class='ant-tag ant-tag-red']//preceding-sibling::span[text()='{InvestmentDescription}']")
        if investmentplanexclude.is_displayed():
            investmentplanexclude.click()
            self.driver.find_element_by_xpath("//button[normalize-space()='Include in Scenario']").click()

    def Investmentcontributions(self, contributionstype, contributionamount):
        self.driver.find_element_by_xpath("//button[@id='contributionsEnabled']").click()
        type = self.driver.find_element_by_xpath(f"//span[normalize-space()='{contributionstype}']")
        if type.is_displayed():
            type.click()
            self.driver.find_element_by_xpath("//input[@id='contributions_amount_amount']").send_keys(contributionamount)

    def withdrowls_custom(self, WithdrawalAmount):
        self.driver.find_element_by_xpath("//button[@id='withdrawalsEnabled']").click()
        withdrawalmethod= self.driver.find_element_by_xpath("//input[@id='withdrawals_withdrawalType']")
        if withdrawalmethod.is_displayed():
            withdrawalmethod.click()
            self.driver.find_element_by_xpath("//div[contains(text(),'Amount')]").click()
            self.driver.find_element_by_xpath("//input[@id='withdrawals_amount_amount']").send_keys(WithdrawalAmount)
            self.driver.find_element_by_xpath("//input[@id='withdrawals_payOutInterest']").click()
            self.driver.find_element_by_xpath("//span[contains(text(),'Payout Dividends')]").click()

    def withdrawals_sell_whole_investment(self):
        self.driver.find_element_by_xpath("//button[@id='saleEventEnabled']").click()
        sellevent = self.driver.find_element_by_xpath("//input[@id='saleEvent_id']")
        if sellevent.is_displayed():
            sellevent.click()
            self.driver.find_element_by_xpath("//div[@id='saleEvent_id_list']//following::div[@title='Forever']").click()

    def specificcharge(self):
        self.driver.find_element_by_xpath("//button[@id='chargesEnabled']").click()
        self.driver.find_element_by_xpath("//span[contains(text(),'Treat financial planning fee as an expense')]").click()

    def deathoptions(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Business Relief Qualifying')]").click()

    def verifyinvestmentinclude(self, InvestmentDescription):
        investmentplaninclude = self.driver.find_element_by_xpath(f"//span[normalize-space()='{InvestmentDescription}']//following::span[@class='line-through']")
        if investmentplaninclude.is_displayed():
            includeInscenario = self.driver.find_element_by_xpath("//span[@class='line-through']")
            assert includeInscenario.text == "EXCLUDED IN BASELINE"

    def investmentreturn(self, Returns):
        self.driver.find_element_by_xpath("//input[@id='grossReturn_rate']").send_keys(Returns)

    def verifyInvestments(self, InvestmentDescription):
        savedinvestment = self.driver.find_element_by_xpath(f"//span[normalize-space()='{InvestmentDescription}']")

        if savedinvestment.is_displayed():
            assert  savedinvestment.text == InvestmentDescription













