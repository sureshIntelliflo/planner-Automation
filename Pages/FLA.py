import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class FLA:

    def __init__(self, driver):
        self.driver = driver

    def NavigatetoFLA(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//a[text() ='Firm Level Assumptions']"))).click()
        time.sleep(2)
        GLDSwitch = self.driver.find_element_by_xpath("//button[@role='switch']")

        status = GLDSwitch.get_attribute("aria-checked")

        if status == "false":
            GLDSwitch.click()
            time.sleep(1)
            self.driver.find_element_by_xpath(
                "//button[@type='submit']//span[text()='Override Assumptions']").click()

            WebDriverWait(self.driver, 5).until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, "//button[@type='submit']//span[text()='Confirm']"))).click()
        elif status == "true":
            print("GLD is enabled")

    def DeleteRiskprofile_ifdisplayed(self, Name):

        try:
            #verify_riskprofile = WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, f"//td[normalize-space()='{Name}']")))

            self.driver.find_element_by_xpath(
                f"//td[normalize-space()='{Name}']//following-sibling::td//button[@title='Delete']").click()
            self.driver.find_element_by_xpath("//span[normalize-space()='Delete Risk Profile']").click()
        except:
            print("no Risk profile to delete with matching")

    def AddRiskProfile(self, Name, GrossReturn, Interest, Dividends, Growth, Fund_Platform, FinancialPlanning):


        time.sleep(3)
        self.driver.find_element_by_xpath("//div[@class='flex items-center']//*[name()='svg']").click()

        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//input[@id='riskProfileName']"))).send_keys(Name)

        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//input[@id='grossReturn']"))).send_keys(GrossReturn)

        self.driver.find_element_by_xpath("//input[@id='allocations_interest']").send_keys(Interest)

        self.driver.find_element_by_xpath("//input[@id='allocations_dividend']").send_keys(Dividends)

        self.driver.find_element_by_xpath("//input[@id='allocations_growth']").send_keys(Growth)

        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//input[@id='platformFundCharge']"))).send_keys(Fund_Platform)

        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//input[@id='financialPlanningCharge']"))).send_keys(FinancialPlanning)

        self.driver.find_element_by_xpath(
            "//button[@type='submit']//span[normalize-space()='Add Risk Profile']").click()

        time.sleep(5)
        verify_riskprofile = self.driver.find_element_by_xpath(f"//td[normalize-space()='{Name}']")
        assert verify_riskprofile.text == Name

    def navigatetoClientpage(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, "//a[normalize-space()='Clients']"))).click()

    def NavigatetoFLApage_disableGLD(self):
        WebDriverWait(self.driver, 1).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, "//img[@alt='Application Menu']"))).click()
        WebDriverWait(self.driver, 1).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, "//a[normalize-space()='Firm Level Assumptions']"))).click()

        GLDSwitch = self.driver.find_element_by_xpath("//button[@role='switch']")
        status = GLDSwitch.get_attribute("aria-checked")

        if status == "true":
            GLDSwitch.click()
            WebDriverWait(self.driver, 5).until(
                expected_conditions.element_to_be_clickable(
                    (By.XPATH, "//span[normalize-space()='Disable Assumptions']"))).click()

            WebDriverWait(self.driver, 5).until(
                expected_conditions.element_to_be_clickable(
                    (By.XPATH, "//span[normalize-space()='Confirm']"))).click()

    def UnlockPlan(self, ParentRiskprofile):
        elements = self.driver.find_elements_by_xpath("//div[@class='ant-select-selector']")
        value = 1
        for element in elements:
            time.sleep(1)
            element.click()
            WebDriverWait(self.driver, 1).until(
                expected_conditions.visibility_of_element_located(
                    (By.XPATH, f"(//input[@type='search']//following::div[text()='{ParentRiskprofile}'])[{value}]"))).click()
            value = value + 1
            continue
        time.sleep(1)
        self.driver.find_element_by_xpath("//span[normalize-space()='Unlock Plan']").click()
