import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@allure.severity(allure.severity_level.CRITICAL)
class Wizards:

    def __init__(self, driver):
        self.driver = driver

    wizardsresultstitle = "//span[@class='ant-page-header-heading-title']"

    def Attachscreenshot(self, Screenshotname):
        allure.attach(self.driver.get_screenshot_as_png(), name=f"{Screenshotname}", attachment_type=AttachmentType.PNG)

    def NavigatetoWizards(self):
        self.driver.find_element_by_xpath("//span[normalize-space()='Wizards']//a").click()
        time.sleep(1)

    def SelectOptimizedwizards(self):
        self.driver.find_element_by_xpath("//span[normalize-space()='Optimization']").click()
        time.sleep(1)

    def FinancialGoal(self, FinancialGoal, Goaltype, TargetYear):
        self.driver.find_element_by_xpath("//input[@id='financialGoal_amount']").send_keys(FinancialGoal)
        self.driver.find_element_by_xpath(f"//span[normalize-space()='{Goaltype}']").click()
        time.sleep(1)
        goalYear = self.driver.find_element_by_xpath("//input[@id='financialGoalYear']")
        goalYear.send_keys(Keys.CONTROL + "a")
        goalYear.send_keys(Keys.DELETE)
        goalYear.send_keys(TargetYear)
        time.sleep(1)

    def definevariables(self):
        self.driver.find_element_by_xpath("//input[@id='optimizationPreRetirement']").click()
        self.driver.find_element_by_xpath("//span[contains(text(),'Post Retirement')]").click()
        self.driver.find_element_by_xpath("//input[@id='optimizationDurationOfPlan']").click()
        time.sleep(2)

    def MaximumoneOffLumpsum(self, LumpSum):
        self.driver.find_element_by_xpath("//input[@id='optimizationMaxOneOffLumpSum']").click()
        LumpSumYear = self.driver.find_element_by_xpath("//input[@id='optimizationYear']")
        LumpSumYear.send_keys(Keys.CONTROL + "a")
        LumpSumYear.send_keys(Keys.DELETE)
        LumpSumYear.send_keys(LumpSum)
        time.sleep(2)

    def WizardsRisk(self):
        self.driver.find_element_by_xpath("//input[@id='optimizationMinAnnualReturn']").click()
        self.driver.find_element_by_xpath("//input[@id='optimizationCash']").click()
        time.sleep(1)

    Wizardresutltitle = "//span[@class='block mb-2 font-semibold']"

    def RunWizards(self):
        self.driver.find_element_by_xpath("//span[normalize-space()='Run Wizard']").click()
        WebDriverWait(self.driver, 60).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//span[@class='block mb-2 font-semibold']")))

    @allure.severity(allure.severity_level.CRITICAL)
    def Verifyresults(self):
        Tabresults = self.driver.find_elements_by_xpath("//div[@role='tablist']//div[@aria-selected]")

        for Tab in Tabresults:

            Tab.click()
            Goallabel = self.driver.find_element_by_xpath("//span[@class='ant-tag']")
            ResultBlue = self.driver.find_element_by_xpath("//span[@class='ant-tag ant-tag-blue']")
            if Goallabel.is_displayed and ResultBlue.is_displayed:
                Wizards = self.driver.find_element_by_xpath("//span[contains(text(),'Raise annual expenditure by')]")
                if Wizards.is_displayed():
                    WebDriverWait(self.driver, 60).until((expected_conditions.visibility_of_element_located((By.XPATH, Wizards))))
                    print("Wizards results are displaying -- >" + Wizards.text)
                    time.sleep(1)
                else:
                    allure.attach(self.driver.get_screenshot_as_png(), name="VerifyingWizards", attachment_type=AttachmentType.PNG)
                    assert False
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="VerifyingWizards",
                              attachment_type=AttachmentType.PNG)
                assert False
            continue

    @allure.severity(allure.severity_level.CRITICAL)
    def ExportWizards(self):
        Exportwizards = self.driver.find_element_by_xpath("//span[normalize-space()='Export']")
        if Exportwizards.is_displayed():
            Exportwizards.click()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="VerifyingWizards_Export", attachment_type=AttachmentType.PNG)
            assert False

    def CapacityofLoss(self, MarketCrashPlan, CrashYear, UserDefinedMaxLoss):
        self.driver.find_element_by_xpath(
            "//span[@class='text-sm font-normal'][normalize-space()='Capacity For Loss']").click()
        self.driver.find_element_by_xpath(
            f"//div[@id='capacityForLossPeriod']//span[contains(text(),'{MarketCrashPlan}')]").click()
        Crash = self.driver.find_element_by_xpath("//input[@id='capacityForLossYear']")
        Crash.send_keys(Keys.CONTROL + "a")
        Crash.send_keys(Keys.DELETE)
        Crash.send_keys(CrashYear)
        self.driver.find_element_by_xpath("//input[@id='capacityForLossCash']").click()
        self.driver.find_element_by_xpath("//button[@id='capacityForLossExpectedMaxLoss']").click()
        self.driver.find_element_by_xpath("//input[@id='capacityForLossReturn']").send_keys(UserDefinedMaxLoss)

    @allure.severity(allure.severity_level.CRITICAL)
    def VerifyCapacityofLossWizard(self):
        Result = self.driver.find_element_by_xpath("//span[@class='text-red-900']")
        if Result.is_displayed():
            allure.attach(self.driver.get_screenshot_as_png(), name="VerifyingWizards", attachment_type=AttachmentType.PNG)
            assert False
        else:
            assert True

    def NavigatetoProtectionWizard(self):
        self.driver.find_element_by_xpath(
            "//span[@class='text-sm font-normal'][normalize-space()='Protection']").click()

    def ProtectionWizard(self, BenefitType, Term):
        self.driver.find_element_by_xpath("//input[@id='protectionIllness0']").click()
        self.driver.find_element_by_xpath(
            f"(//div[@id='protectionBenefitTypeIllness0']//following::span[normalize-space()='{BenefitType}'])[1]").click()
        termyears = self.driver.find_element_by_xpath("//input[@id='protectionTermIllness0']")
        termyears.send_keys(Keys.CONTROL + "a")
        termyears.send_keys(Keys.DELETE)
        termyears.send_keys(Term)

    @allure.severity(allure.severity_level.CRITICAL)
    def VerifyProtectionWizard(self):
        event = self.driver.find_element_by_xpath("//span[normalize-space()='Events']")
        Blue = self.driver.find_element_by_xpath("//span[@class='ant-tag ant-tag-blue']")
        if Blue.is_displayed() and event.is_displayed():
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="VerifyingWizards", attachment_type=AttachmentType.PNG)
            assert False

