import allure
from allure_commons.types import AttachmentType


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

