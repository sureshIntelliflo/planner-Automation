import time

import allure
from allure_commons.types import AttachmentType


class Protections:

    def __init__(self, driver):
        self.driver = driver
    def Attachscreenshot(self, Screenshotname):
        allure.attach(self.driver.get_screenshot_as_png(), name=f"{Screenshotname}",
                      attachment_type=AttachmentType.PNG)

    def verifyuserisonHome(self):
        try:
            element = self.driver.find_element_by_xpath("//span[text()='Active Scenario']")
            if element.is_displayed():
                print("User is on home page")
            else:
                self.Attachscreenshot("verifyuserisonHome")
                assert False
        except:
            self.Attachscreenshot("verifyuserisonHome")


    def AddNewProtections(self, ProtectionsDescription):
        try:
            Addprotectionbtn = self.driver.find_element_by_xpath("//span[normalize-space()='Add Protection']")
            if Addprotectionbtn.is_displayed():
                Addprotectionbtn.click()
                self.driver.find_element_by_xpath("//input[@id='protectionDescription']").send_keys(ProtectionsDescription)
            else:
                print("unable to find the add protections button")
                self.Attachscreenshot("AddNewProtections")
                assert False
        except:
            self.Attachscreenshot("AddNewProtections")


    def NavigatetoProtections(self):
        try:
            self.driver.find_element_by_xpath("//span[normalize-space()='Plan Inputs']").click()
            self.driver.find_element_by_xpath(
                "//span[@class='text-sm font-normal'][normalize-space()='Protections']").click()
        except:
            self.Attachscreenshot("NavigatetoProtections")


    def SelectProtectionType(self, ProtectionsType):
        try:
            self.driver.find_element_by_xpath("//div[@class='ant-select-selector']").click()
            time.sleep(1)
            policytype = self.driver.find_element_by_xpath(f"//div[contains(text(),'{ProtectionsType}')]")
            if policytype.is_displayed():
                policytype.click()
            else:
                print("unable to find the protection type")
                self.Attachscreenshot("SelectProtectionType")
                assert False
        except:
            self.Attachscreenshot("SelectProtectionType")


    def ProtectionBenefit(self, IncomeDescription, DeathInServiceMultiplier):
        try:
            self.driver.find_element_by_xpath("//div[@name='linkedEmployment,id']//div[@class='ant-select-selector']").click()
            linkedemployment = self.driver.find_element_by_xpath(f"//div[contains(text(),'{IncomeDescription}')]")
            if linkedemployment.is_displayed():
                linkedemployment.click()
                self.driver.find_element_by_xpath("//input[@id='multiplier']").send_keys(DeathInServiceMultiplier)
            else:
                print("unable to locate the linked employment")
                self.Attachscreenshot("ProtectionBenefit")
                assert False
        except:
            self.Attachscreenshot("ProtectionBenefit")


    def AddProtections(self):
        try:
            self.driver.find_element_by_xpath("//button[@type='button']//span[contains(text(),'Add Protection')]").click()
        except:
            self.Attachscreenshot("AddProtections")


    def VerifyProtection(self, ProtectionsDescription):
        try:
            ProtectionName= self.driver.find_element_by_xpath(f"//span[normalize-space()='{ProtectionsDescription}']")
            if ProtectionName.is_displayed():
                assert ProtectionName.text == ProtectionsDescription
            else:
                self.Attachscreenshot("VerifyProtection")
                assert False
        except:
            self.Attachscreenshot("VerifyProtection")


    def ViewProtectionDetails(self, ProtectionsDescription):
        try:
            ProtectionName = self.driver.find_element_by_xpath(f"//span[normalize-space()='{ProtectionsDescription}']")
            if ProtectionName.is_displayed():
                ProtectionName.click()
                self.driver.find_element_by_xpath("//button[@type='button']//span[contains(text(),'Save Protection')]").click()
                time.sleep(1)
            else:
                self.Attachscreenshot("ViewProtectionDetails")
                assert False
        except:
            self.Attachscreenshot("ViewProtectionDetails")




