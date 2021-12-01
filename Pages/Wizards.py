import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Pages.Common import CommonFunctions
from Pages.Login_cashflow import CashflowLogin


@allure.severity(allure.severity_level.CRITICAL)
class Wizards:

    def __init__(self, driver):
        self.driver = driver

    wizardsresultstitle = "//span[@class='ant-page-header-heading-title']"

    def Attachscreenshot(self, Screenshotname):
        allure.attach(self.driver.get_screenshot_as_png(), name=f"{Screenshotname}", attachment_type=AttachmentType.PNG)

    def NavigatetoWizards(self):
        try:
            self.driver.find_element_by_xpath("//span[normalize-space()='Wizards']//a").click()
        except:
            self.Attachscreenshot("NavigatetoWizards")

        time.sleep(1)

    def SelectOptimizedwizards(self):
        try:
            self.driver.find_element_by_xpath("//span[normalize-space()='Optimization']").click()
        except:
            self.Attachscreenshot("SelectOptimizedwizards")

        time.sleep(1)

    def NavigatetoCapacityofLoss(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(
            "//span[@class='text-sm font-normal'][normalize-space()='Capacity For Loss']").click()

    def FinancialGoal(self, FinancialGoal, Goaltype, TargetYear):
        try:
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@id='financialGoal_amount']").send_keys(FinancialGoal)
            self.driver.find_element_by_xpath(f"//span[normalize-space()='{Goaltype}']").click()
            time.sleep(1)
            if Goaltype == "Specific Year":
                goalYear = self.driver.find_element_by_xpath("//input[@id='financialGoalYear']")
                goalYear.send_keys(Keys.CONTROL + "a")
                goalYear.send_keys(Keys.DELETE)
                goalYear.send_keys(TargetYear)
            time.sleep(1)
        except:
            self.Attachscreenshot("FinancialGoal")

    def definevariables(self):
        try:
            self.driver.find_element_by_xpath("//input[@id='optimizationPreRetirement']").click()
            self.driver.find_element_by_xpath("//span[contains(text(),'Post Retirement')]").click()
            self.driver.find_element_by_xpath("//input[@id='optimizationDurationOfPlan']").click()
            time.sleep(2)
        except:
            self.Attachscreenshot("definevariables")

    def MaximumoneOffLumpsum(self, LumpSum):
        try:
            self.driver.find_element_by_xpath("//input[@id='optimizationMaxOneOffLumpSum']").click()
            LumpSumYear = self.driver.find_element_by_xpath("//input[@id='optimizationYear']")
            LumpSumYear.send_keys(Keys.CONTROL + "a")
            LumpSumYear.send_keys(Keys.DELETE)
            LumpSumYear.send_keys(LumpSum)
            time.sleep(2)
        except:
            self.Attachscreenshot("MaximumoneOffLumpsum")

    def WizardsRisk(self):
        try:
            self.driver.find_element_by_xpath("//input[@id='optimizationMinAnnualReturn']").click()
            self.driver.find_element_by_xpath("//input[@id='optimizationCash']").click()
            time.sleep(1)
        except:
            self.Attachscreenshot("WizardsRisk")

    Wizardresutltitle = "//span[@class='block mb-2 font-semibold']"

    def RunWizards(self):
        try:
            self.driver.find_element_by_xpath("//span[normalize-space()='Run Wizard']").click()
            WebDriverWait(self.driver, 60).until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, "//span[@class='block mb-2 font-semibold']")))
        except:
            self.Attachscreenshot("RunWizards")

    @allure.severity(allure.severity_level.CRITICAL)
    def Verifyresults(self):

        Tabresults = self.driver.find_elements_by_xpath("//div[@role='tablist']//div[@aria-selected]")

        for Tab in Tabresults:

            Tab.click()
            Goallabel = self.driver.find_element_by_xpath("//span[@class='ant-tag']")
            ResultBlue = self.driver.find_element_by_xpath("//span[@class='ant-tag ant-tag-blue']")
            if Goallabel.is_displayed and ResultBlue.is_displayed:
                WebDriverWait(self.driver, 60).until(
                    (expected_conditions.visibility_of_element_located(
                        (By.XPATH, "(//span[@class='ant-tag ant-tag-blue']//following::span)[1]"))))
            else:
                self.Attachscreenshot("Verifyresults")
                CommonFunctions.DeleteClient()
                CashflowLogin.logoutfromClientpage()
                assert False

    @allure.severity(allure.severity_level.CRITICAL)
    def ExportWizards(self):

        Exportwizards = self.driver.find_element_by_xpath("//span[normalize-space()='Export']")
        if Exportwizards.is_displayed():
            Exportwizards.click()
            self.driver.find_element_by_link_text("Download").click()

        else:
            self.Attachscreenshot("ExportWizards")
            CommonFunctions.DeleteClient()

    def CapacityofLoss(self, MarketCrashPlan, CrashYear, UserDefinedMaxLoss):
        try:

            time.sleep(1)
            self.driver.find_element_by_xpath(
                f"//div[@id='capacityForLossPeriod']//span[contains(text(),'{MarketCrashPlan}')]").click()
            Crash = self.driver.find_element_by_xpath("//input[@id='capacityForLossYear']")
            Crash.send_keys(Keys.CONTROL + "a")
            Crash.send_keys(Keys.DELETE)
            Crash.send_keys(CrashYear)
            self.driver.find_element_by_xpath("//input[@id='capacityForLossCash']").click()
            self.driver.find_element_by_xpath("//button[@id='capacityForLossExpectedMaxLoss']").click()
            self.driver.find_element_by_xpath("//input[@id='capacityForLossReturn']").send_keys(UserDefinedMaxLoss)
        except:
            self.Attachscreenshot("CapacityofLoss")

    @allure.severity(allure.severity_level.CRITICAL)
    def VerifyCapacityofLossWizard(self):

        Result = self.driver.find_element_by_xpath("//span[@class='ant-tag ant-tag-blue']")
        if Result.is_displayed():
            statement = self.driver.find_element_by_xpath("//span[contains(text(),'The plan could sustain a loss of')]")
            if statement.is_displayed():
                print(statement.text)
            else:
                self.Attachscreenshot("VerifyCapacityofLossWizard")
                assert False
        else:
            self.Attachscreenshot("VerifyCapacityofLossWizard")
            assert False

    def NavigatetoProtectionWizard(self):
        try:
            self.driver.find_element_by_xpath(
                "//span[@class='text-sm font-normal'][normalize-space()='Protection']").click()
        except:
            self.Attachscreenshot("NavigatetoProtectionWizard")

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
            self.Attachscreenshot("VerifyProtectionWizard")
            assert False
