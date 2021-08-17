import time


class Protections:

    def __init__(self, driver):
        self.driver = driver

    def verifyuserisonHome(self):
        element = self.driver.find_element_by_xpath("//span[text()='Active Scenario']")
        if element.is_displayed():
            print("User is on home page")

    def AddNewProtections(self, ProtectionsDescription):
        Addprotectionbtn = self.driver.find_element_by_xpath("//span[normalize-space()='Add Protection']")
        if Addprotectionbtn.is_displayed():
            Addprotectionbtn.click()
            self.driver.find_element_by_xpath("//input[@id='protectionDescription']").send_keys(ProtectionsDescription)
        else:
            print("unable to find the add protections button")

    def NavigatetoProtections(self):
        self.driver.find_element_by_xpath("//span[normalize-space()='Plan Inputs']").click()
        self.driver.find_element_by_xpath(
            "//span[@class='text-sm font-normal'][normalize-space()='Protections']").click()

    def SelectProtectionType(self, ProtectionsType):
        self.driver.find_element_by_xpath("//div[@class='ant-select-selector']").click()
        time.sleep(1)
        policytype = self.driver.find_element_by_xpath(f"//div[contains(text(),'{ProtectionsType}')]")
        if policytype.is_displayed():
            policytype.click()
        else:
            print("unable to find the protection type")

    def ProtectionBenefit(self, IncomeDescription, DeathInServiceMultiplier):
        self.driver.find_element_by_xpath("//div[@name='linkedEmployment,id']//div[@class='ant-select-selector']").click()
        linkedemployment = self.driver.find_element_by_xpath(f"//div[contains(text(),'{IncomeDescription}')]")
        if linkedemployment.is_displayed():
            linkedemployment.click()
            self.driver.find_element_by_xpath("//input[@id='multiplier']").send_keys(DeathInServiceMultiplier)
        else:
            print("unable to locate the linked employment")

    def AddProtections(self):
        self.driver.find_element_by_xpath("//button[@type='button']//span[contains(text(),'Add Protection')]").click()

    def VerifyProtection(self, ProtectionsDescription):
        ProtectionName= self.driver.find_element_by_xpath(f"//span[normalize-space()='{ProtectionsDescription}']")
        if ProtectionName.is_displayed():
            assert ProtectionName.text == ProtectionsDescription

    def ViewProtectionDetails(self, ProtectionsDescription):
        ProtectionName = self.driver.find_element_by_xpath(f"//span[normalize-space()='{ProtectionsDescription}']")
        if ProtectionName.is_displayed():
            ProtectionName.click()
            self.driver.find_element_by_xpath("//button[@type='button']//span[contains(text(),'Save Protection')]").click()
            time.sleep(1)




