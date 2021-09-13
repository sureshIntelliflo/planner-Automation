import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Properties:

    def __init__(self, driver):
        self.driver = driver

    PropertiesOption = "//a//span[text()='Properties']"
    ActiveScenario = "//span[text()='Active Scenario']"
    AddProperty_btn = "//button//span[text()='Add Property']"
    Preexsiting_btn = "//*[@id='isPreexisting']//input"
    currentvalue = "value_amount"
    CGT = "capitalGainsTaxBaseCost_amount"
    Plans_menu = "//span[text()='Plan Inputs']/ancestor::a"

    def Attachscreenshot(self, Screenshotname):
        allure.attach(self.driver.get_screenshot_as_png(), name=f"{Screenshotname}",
                      attachment_type=AttachmentType.PNG)

    def Verify_user_in_home_page(self):
        try:
            element = self.driver.find_element_by_xpath(Properties.ActiveScenario)
            if element.is_displayed():
                print("User is on home page")
            else:
                self.Attachscreenshot("Verify_user_in_home_page")
                assert False
        except:
            self.Attachscreenshot("Verify_user_in_home_page")


    def i_add_property_plan_from_property_page(self):
        try:
            self.driver.find_element_by_xpath("//span[normalize-space()='Plan Inputs']").click()
            self.driver.find_element_by_xpath(
                "//span[@class='text-sm font-normal'][normalize-space()='Properties']").click()
        except:
            self.Attachscreenshot("i_add_property_plan_from_property_page")


    def i_provide_propertydescription(self, PropertyDescription):
        try:
            AddProperty = self.driver.find_element_by_xpath(Properties.AddProperty_btn)
            if AddProperty.is_displayed():
                AddProperty.click()
                self.driver.find_element_by_id("name").send_keys(PropertyDescription)
            else:
                self.Attachscreenshot("i_provide_propertydescription")
                assert False
        except:
            self.Attachscreenshot("i_provide_propertydescription")


    def select_preexisting(self, PreExisting):
        try:
            propertydetails = self.driver.find_elements_by_xpath(Properties.Preexsiting_btn)
            for type in propertydetails:
                if type.text == PreExisting:
                    type.click()
                else:
                    self.Attachscreenshot("select_preexisting")
        except:
            self.Attachscreenshot("select_preexisting")


    def currentvalue(self, CurrentValue):
        try:
            self.driver.find_element_by_id("value_amount").send_keys(CurrentValue)
        except:
            self.Attachscreenshot("currentvalue")


    def basecostCGTvalue(self, BaseCostCGT):
        try:
            self.driver.find_element_by_id("capitalGainsTaxBaseCost_amount").send_keys(BaseCostCGT)
            time.sleep(1)
        except:
            self.Attachscreenshot("basecostCGTvalue")


    def Saleevent(self, SaleExpense):
        try:
            print("sale event")
            Sale_event_switch = self.driver.find_element_by_xpath("//button[@id='salePlanEnabled']")
            if Sale_event_switch.get_attribute('aria-checked') == 'false':
                Sale_event_switch.click()
                self.driver.find_element_by_xpath("//input[@id='salePlan_saleExpensePercentage']").send_keys(SaleExpense)
                time.sleep(2)
            else:
                self.Attachscreenshot("Saleevent")
                assert False
        except:
            self.Attachscreenshot("Saleevent")


    def mortage(self, MortagageDescription, ReplaymentType, MortagageValue, InterestRate, MortgageStartEvent,
                MortgageCeaseEvent):
        try:
            mortgageswitch = self.driver.find_element_by_xpath("//button[@id='mortgagesEnabled']")
            if mortgageswitch.get_attribute('aria-checked') == 'false':
                mortgageswitch.click()
            Addmortgage = self.driver.find_element_by_xpath("//span[normalize-space()='Add mortgage']")
            if Addmortgage.is_displayed():
                Addmortgage.click()
            NewMortgage = self.driver.find_element_by_xpath("//span[@title='New Mortgage']")
            if NewMortgage.is_displayed():
                self.driver.find_element_by_xpath("//input[@id='description']").send_keys(MortagageDescription)
                self.driver.find_element_by_id("repaymentType").click()
                time.sleep(2)
                self.driver.find_element_by_xpath(f"//div[contains(text(),'{ReplaymentType}')]").click()

            self.driver.find_element_by_xpath("//input[@id='value_amount']").send_keys(MortagageValue)
            self.driver.find_element_by_xpath("//input[@id='interestRate']").send_keys(InterestRate)
            mortgagestartevent = self.driver.find_elements_by_xpath("//*[@id='usePropertyPurchaseEvent']//label//span[2]")
            for event in mortgagestartevent:
                if event == MortgageStartEvent:
                    event.click()
            self.driver.find_element_by_id("endEvent_id").click()
            time.sleep(2)
            self.driver.find_element_by_xpath(f"//div[contains(text(),'{MortgageCeaseEvent}')]").click()

            self.driver.find_element_by_xpath("//button[@type='button']//span[contains(text(),'Add Mortgage')]").click()
            time.sleep(1)
        except:
            self.Attachscreenshot("mortage")


    def rental(self, Rental, RentalExpense):
        try:
            rentalswitch = self.driver.find_element_by_xpath("//button[@id='rentEnabled']")
            if rentalswitch.get_attribute("aria-checked") == "false":
                rentalswitch.click()
            rentincome = self.driver.find_element_by_xpath("//input[@id='rent_income_value_amount']")
            rentincome.send_keys(Rental)

            rentexpense = self.driver.find_element_by_xpath("//input[@id='rent_expense_value_amount']")
            rentexpense.send_keys(RentalExpense)
        except:
            self.Attachscreenshot("rental")


    def renovation(self, RenovationCost, IncreasedtoPropertyValue, RenovationEvent):
        try:
            renovationswitch = self.driver.find_element_by_xpath("//button[@id='renovationEnabled']")
            if renovationswitch.get_attribute("aria-checked") == "false":
                renovationswitch.click()
            renovationcost = self.driver.find_element_by_xpath("//input[@id='renovation_cost_amount']")
            renovationcost.send_keys(RenovationCost)

            increasepropertyvalue = self.driver.find_element_by_xpath(
                "//input[@id='renovation_increaseToPropertyValue_amount']")
            increasepropertyvalue.send_keys(IncreasedtoPropertyValue)

            self.driver.find_element_by_xpath("(//*[@id='renovation_event_id']/following::span)[1]").click()
            time.sleep(3)
            renovationevent = self.driver.find_element_by_xpath(f"//div[contains(text(),'{RenovationEvent}')]")
            renovationevent.click()
        except:
            self.Attachscreenshot("renovation")


    def addpropery(self, PropertyDescription):
        try:
            addproperty = self.driver.find_element_by_xpath(
                "//button[@type='button']//span[contains(text(),'Add Property')]")
            addproperty.click()
            time.sleep(2)
            propertynarrative = self.driver.find_element_by_xpath(f"//div[contains(text(),'{PropertyDescription}')]")
            if propertynarrative.is_displayed():
                assert propertynarrative.text == PropertyDescription
        except:
            self.Attachscreenshot("addpropery")


    def searchclient(self, Existingclient):
        try:
            self.driver.find_element_by_xpath(" //input[@placeholder='Search...' and @type='text']").send_keys(
                Existingclient)
            self.driver.find_element_by_xpath("//button//span[@aria-label='search']").click()
            results = self.driver.find_elements_by_xpath(
                "//*[@id='i4c-application-ui']//div[@class='my-5']//span[@class='block text-lg truncate']")
            for resultslist in results:
                if resultslist.text == Existingclient:
                    resultslist.click()
                    break
            time.sleep(1)
        except:
            self.Attachscreenshot("searchclient")


    def navigaetoPropertypage(self):
        try:
            self.driver.find_element_by_xpath("//span[normalize-space()='Plan Inputs']").click()
            self.driver.find_element_by_xpath(
                "//span[@class='text-sm font-normal'][normalize-space()='Properties']").click()
            time.sleep(1)
        except:
            self.Attachscreenshot("navigaetoPropertypage")


    def createscenario(self, ScenarioName, ScenarioDescription):
        try:
            self.driver.find_element_by_xpath(
                "//div[@class='flex items-center hidden lg:block justify-center']//span[@class='hidden md:block mr-1 text-primary-500 text-sm font-semibold'][normalize-space()='Active Scenario']").click()
            time.sleep(1)
            AddScenariobtn = self.driver.find_element_by_xpath("//button//span[text()='Add scenario']")
            if AddScenariobtn.is_displayed():
                AddScenariobtn.click()
            time.sleep(1)

            self.driver.find_element_by_xpath("//div[@class='ant-modal-body']//input[@id='name']").send_keys(ScenarioName)
            self.driver.find_element_by_xpath("//textarea[@id='description']").send_keys(ScenarioDescription)
            self.driver.find_element_by_xpath("//span[normalize-space()='Add Scenario']").click()
            verifyscenario = self.driver.find_element_by_xpath(
                f"//div[@class='flex items-center hidden lg:block justify-center']//span[@class='text-gray-900 text-sm'][normalize-space()='{ScenarioName}']")
            assert verifyscenario.text == ScenarioName
            time.sleep(1)
        except:
            self.Attachscreenshot("createscenario")


    def navigatetonarrativedetails(self):
        try:
            self.driver.find_element_by_xpath("//div[contains(text(),'AutomatedProperty1')]").click()
        except:
            self.Attachscreenshot("navigatetonarrativedetails")


    def excludeplanwithallSwitchesON(self):
        try:
            time.sleep(2)
            self.driver.find_element_by_xpath("//button[normalize-space()='Exclude from Scenario']").click()

            textalert = self.driver.find_element_by_xpath("//span[@class='text-red-800']")
            assert textalert.text == "This property is excluded from the current scenario"
        except:
            self.Attachscreenshot("excludeplanwithallSwitchesON")


    def savepropery(self, PropertyDescription):
        try:
            self.driver.find_element_by_xpath("//button[@type='submit']//span[contains(text(),'Save Property')]").click()
            time.sleep(1)
            propertynarrative = self.driver.find_element_by_xpath("//div[contains(text(),'AutomatedProperty1')]")
            if propertynarrative.is_displayed():
                assert propertynarrative.text == PropertyDescription
        except:
            self.Attachscreenshot("savepropery")


    def excludedscenario(self):
        try:
            exclude = self.driver.find_element_by_xpath("//span[@class='ant-tag ant-tag-yellow']")
            assert exclude.text == "EXCLUDED FROM SCENARIO"
        except:
            self.Attachscreenshot("excludedscenario")


    def Mortgage_linking(self, MortagageDescription, ReplaymentType, MortagageValue, InterestRate, MortgageStartEvent,
                         MortgageCeaseEvent):
        try:
            mortgageswitch = self.driver.find_element_by_xpath("//button[@id='mortgagesEnabled']")
            if mortgageswitch.get_attribute('aria-checked') == 'false':
                mortgageswitch.click()
            Addmortgage = self.driver.find_element_by_xpath("//span[normalize-space()='Add mortgage']")
            if Addmortgage.is_displayed():
                Addmortgage.click()
            NewMortgage = self.driver.find_element_by_xpath("//span[@title='New Mortgage']")
            if NewMortgage.is_displayed():
                self.driver.find_element_by_xpath("//input[@id='description']").send_keys(MortagageDescription)
                self.driver.find_element_by_id("repaymentType").click()
                time.sleep(1)
                self.driver.find_element_by_xpath(f"//div[contains(text(),'{ReplaymentType}')]").click()

            self.driver.find_element_by_xpath("//input[@id='value_amount']").send_keys(MortagageValue)
            self.driver.find_element_by_xpath("//input[@id='interestRate']").send_keys(InterestRate)
            mortgagestartevent = self.driver.find_elements_by_xpath("//*[@id='usePropertyPurchaseEvent']//label//span[2]")
            for event in mortgagestartevent:
                if event == MortgageStartEvent:
                    event.click()
            self.driver.find_element_by_id("endEvent_id").click()
            time.sleep(2)
            self.driver.find_element_by_xpath(f"//div[contains(text(),'{MortgageCeaseEvent}')]").click()
            time.sleep(1)
        except:
            self.Attachscreenshot("Mortgage_linking")


    def MortgageOffet(self, InvestmentDescription, OffsetOptions):
        try:

            self.driver.find_element_by_xpath("//button[@id='offsetEnabled']").click()
            time.sleep(1)
            LinkedcurrentAcccount = self.driver.find_element_by_xpath("//input[@id='offset_investment_id']")
            LinkedcurrentAcccount.click()
            self.driver.find_element_by_xpath(f"//div[contains(text(),'{InvestmentDescription}')]").click()

            offsetOptions = self.driver.find_element_by_xpath("//input[@id='offset_option']//following::span[@title]")
            offsetOptions.click()
            self.driver.find_element_by_xpath(f"//div[contains(text(),'{OffsetOptions}')]").click()
        except:
            self.Attachscreenshot("Mortgage_linking")

    def AddMortgage(self):
        try:
            self.driver.find_element_by_xpath("//button[@type='button']//span[contains(text(),'Add Mortgage')]").click()
        except:
            self.Attachscreenshot("AddMortgage")

