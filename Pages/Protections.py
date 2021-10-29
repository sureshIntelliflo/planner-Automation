import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Protections:

    def __init__(self, driver):
        self.driver = driver

    def Attachscreenshot(self, Screenshotname):
        allure.attach(self.driver.get_screenshot_as_png(), name=f"{Screenshotname}",
                      attachment_type=AttachmentType.PNG)

    def verifyuserisonHome(self):

        element = self.driver.find_element_by_xpath(
            "//span[normalize-space()='Client Settings']")
        if element.is_displayed():
            print("User is on home page")
        else:
            self.Attachscreenshot("verifyuserisonHome")


    def AddNewProtections(self, ProtectionsDescription):

        Addprotectionbtn = self.driver.find_element_by_xpath("//span[normalize-space()='Add Protection']")
        if Addprotectionbtn.is_displayed():
            Addprotectionbtn.click()
            self.driver.find_element_by_xpath("//input[@id='protectionDescription']").send_keys(ProtectionsDescription)
        else:
            print("unable to find the add protections button")
            self.Attachscreenshot("AddNewProtections")
            assert False

    def NavigatetoProtections(self):
        try:
            self.driver.find_element_by_xpath("//span[normalize-space()='Plan Inputs']").click()
            self.driver.find_element_by_xpath(
                "//span[@class='text-sm font-normal'][normalize-space()='Protections']").click()
        except:
            self.Attachscreenshot("NavigatetoProtections")

    def SelectProtectionType(self, ProtectionsType):

        self.driver.find_element_by_xpath("//div[@class='ant-select-selector']").click()
        time.sleep(1)
        policytype = self.driver.find_element_by_xpath(f"//div[contains(text(),'{ProtectionsType}')]")
        if policytype.is_displayed():
            policytype.click()
        else:
            print("unable to find the protection type")
            self.Attachscreenshot("SelectProtectionType")
            assert False

    def ProtectionBenefit(self, IncomeDescription, DeathInServiceMultiplier):

        self.driver.find_element_by_xpath(
            "//div[@name='linkedEmployment,id']//div[@class='ant-select-selector']").click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, f"//div[contains(text(),'{IncomeDescription}')]"))).click()
        self.driver.find_element_by_xpath("//input[@id='multiplier']").send_keys(DeathInServiceMultiplier)


    def AddProtections(self):
        try:
            self.driver.find_element_by_xpath(
                "//button[@type='button']//span[contains(text(),'Add Protection')]").click()
        except:
            self.Attachscreenshot("AddProtections")

    def VerifyProtection(self, ProtectionsDescription):

        ProtectionName = self.driver.find_element_by_xpath(f"//span[normalize-space()='{ProtectionsDescription}']")
        if ProtectionName.is_displayed():
            assert ProtectionName.text == ProtectionsDescription
        else:
            self.Attachscreenshot("VerifyProtection")
            assert False

    def ViewProtectionDetails(self, ProtectionsDescription):

        ProtectionName = self.driver.find_element_by_xpath(f"//span[normalize-space()='{ProtectionsDescription}']")
        if ProtectionName.is_displayed():
            ProtectionName.click()
            self.driver.find_element_by_xpath(
                "//button[@type='button']//span[contains(text(),'Save Protection')]").click()
            time.sleep(1)
        else:
            self.Attachscreenshot("ViewProtectionDetails")
            assert False
