import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CashflowLogin:

    def __init__(self, driver):
        self.driver = driver

    Email_textbox_field = "#username"
    Password_textbox_field = "#password"
    Login_Button = "//button[@class='btn btn-primary']"

    def Attachscreenshot(self, Screenshotname):
        allure.attach(self.driver.get_screenshot_as_png(), name=f"{Screenshotname}",
                      attachment_type=AttachmentType.PNG)

    def enter_email(self, Email_Address):
        try:
            self.driver.find_element_by_css_selector(CashflowLogin.Email_textbox_field).clear()
            self.driver.find_element_by_css_selector(CashflowLogin.Email_textbox_field).send_keys(Email_Address)
        except:
            self.Attachscreenshot("enter_email")

    def enter_password(self, Password):
        try:
            self.driver.find_element_by_css_selector(CashflowLogin.Password_textbox_field).clear()
            self.driver.find_element_by_css_selector(CashflowLogin.Password_textbox_field).send_keys(Password)
        except:
            self.Attachscreenshot("enter_password")

    def click_login(self):
        try:
            self.driver.find_element_by_xpath("//button[normalize-space()='Login']").click()
        except:
            self.Attachscreenshot("click_login")

    def VerifyLoginpage(self, pagetitle):
        try:
            assert pagetitle == self.driver.title
        except:
            self.Attachscreenshot("VerifyLoginpage")

    def SimpleLogout(self):
        try:
            self.driver.find_element_by_link_text("Logout").click()
        except:
            self.Attachscreenshot("SimpleLogout")

    def VerifyLogoutPage(self, SignedOut):
        try:
            assert SignedOut == self.driver.title
        except:
            self.Attachscreenshot("SimpleLogout")

    def VerifyValidation(self, Validation):
        try:
            assert Validation == self.driver.find_element_by_xpath("//div[@class='alert alert-danger']").text
        except:
            self.Attachscreenshot("VerifyValidation")

    def logoutVerification(self, Validation):
        try:
            assert Validation == self.driver.find_element_by_xpath("//div[@class='alert alert-danger']").text
        except:
            self.Attachscreenshot("logoutVerification")

    def logout(self):
        try:
            self.driver.find_element_by_xpath(
                "//button[@class='ant-btn ant-btn-link HeaderLogo_logo__lmyp5 Button_plain__3UtWY']").click()
            self.driver.find_element_by_link_text("Logout").click()
        except:
            self.Attachscreenshot("logoutVerification")

    def logoutfromClientpage(self):
        try:
            self.driver.find_element_by_xpath("//a[normalize-space()='Logout']").click()
        except:
            self.Attachscreenshot("logoutVerification")

    def CallUserLogin(self, Username, Password):
        try:
            """Entering the user login details"""
            self.driver.find_element_by_css_selector('#username').send_keys(Username)
            self.driver.find_element_by_css_selector('#password').send_keys(Password)
            signin = "//button[@class='btn btn-primary']"
            self.driver.find_element_by_xpath(signin).click()
            time.sleep(3)
        except:
            self.Attachscreenshot("CallUserLogin")

    def VerifyUserLogingsuccessful(self):
        clientpage = "//span[@title='Clients']"
        client = self.driver.find_element_by_xpath(clientpage)
        if client.is_displayed():
            assert True
        else:
            self.Attachscreenshot("CallUserLogin")
            assert False

    def AddSingleHOHclient(self, HoHName, HoHKnowas, DoB, TaxResidency, Gender):
        element = self.driver.find_element_by_xpath("//button[@title = 'Create a new client']")
        if element.is_enabled():
            element.click()
            createclient = self.driver.find_element_by_xpath("//form/child::span[text()='Create Client']")
            if createclient.is_displayed():
                print("Create client page is displaying")
                self.driver.find_element_by_xpath("//button//span[text()= 'Add first head of household']").click()
                time.sleep(1)
                self.driver.find_element_by_id("fullName").clear()
                self.driver.find_element_by_id("fullName").send_keys(HoHName)

                self.driver.find_element_by_id("knownAs").clear()
                self.driver.find_element_by_id("knownAs").send_keys(HoHKnowas)

                self.driver.find_element_by_xpath("(//*[@class='flex items-center'])[1]").click()
                time.sleep(1)
                self.driver.find_element_by_xpath(
                    "//*[@class='rc-virtual-list-holder-inner']/child::div//div[contains(text(),'Red')]").click()

                self.driver.find_element_by_id("dateOfBirth").send_keys(DoB)

                self.driver.find_element_by_xpath("//span[@title='England']").click()
                elements = self.driver.find_elements_by_xpath(
                    "//*[@id='taxResidence_list']/following::div//*[@class='ant-select-item-option-content']")
                time.sleep(1)
                for element in elements:
                    if TaxResidency == element.text:
                        element.click()
                        break
                    else:
                        print("no Tax residency found")
                self.driver.find_element_by_id("gender").click()
                Genderlist = self.driver.find_elements_by_xpath("//*[@id='gender_list']/following::div[@aria-selected='false']")

                for list in Genderlist:
                    element3 = list.get_attribute("title")
                    if element3 == Gender:
                        list.click()
                        break
                self.driver.find_element_by_xpath("//button/span[text()= 'Add Person']").click()
            else:
                self.Attachscreenshot("createclient")
                assert False
        else:
            self.Attachscreenshot("Create a new client")
            assert False

    def ClientName(self, ClientName):
        self.driver.find_element_by_id("caseName").send_keys(ClientName)
        self.driver.find_element_by_xpath("//button/span[text()= 'Create Client']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//button//span[text()='Client Settings']").click()
        clientelement = self.driver.find_element_by_id("caseName")
        assert ClientName == clientelement.get_attribute("value")
        close = "//button[@aria-label='Close']"
        self.driver.find_element_by_xpath(close).click()
        WebDriverWait(self.driver, 2).until(expected_conditions.invisibility_of_element_located((By.XPATH, close)))


    def AddSecondHoH(self, HohName_2, HoHKnowas_2, DoB_2, SecondGender, relation):
        self.driver.find_element_by_xpath("//span[text()= 'Add partner/cohabitant']").click()

        self.driver.find_element_by_id("fullName").clear()
        self.driver.find_element_by_id("fullName").send_keys(HohName_2)

        self.driver.find_element_by_id("knownAs").clear()
        self.driver.find_element_by_id("knownAs").send_keys(HoHKnowas_2)

        self.driver.find_element_by_id("dateOfBirth").send_keys(DoB_2)

        self.driver.find_element_by_xpath("(//*[@class='flex items-center'])[1]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            "//*[@class='rc-virtual-list-holder-inner']/child::div//div[contains(text(),'Blue')]").click()

        self.driver.find_element_by_id("relationship").click()
        time.sleep(1)
        # Relationlist = self.driver.find_elements_by_xpath(
        #     "//*[@id='relationship_list']/following::div[@aria-selected='false']")
        # time.sleep(1)
        # for list in Relationlist:
        #     element3 = list.get_attribute("title")
        #     print(element3)
        #     if element3 == relation:
        #         list.click()
        #         break
        self.driver.find_element_by_xpath(f"//div[contains(text(),'{SecondGender}')]").click()


        self.driver.find_element_by_id("gender").click()
        # Genderlist = self.driver.find_elements_by_xpath("//*[@id='gender_list']/following::div[@aria-selected='false']")
        # time.sleep(1)
        # for list in Genderlist:
        #     element3 = list.get_attribute("title")
        #     if element3 == SecondGender:
        #         list.click()
        #         break
        time.sleep(1)
        self.driver.find_element_by_xpath(f"//div[contains(text(),'{relation}')]").click()
        self.driver.find_element_by_xpath("//button/span[text()= 'Add Person']").click()


