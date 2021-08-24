

class CashflowLogin:

        def __init__(self, driver):
            self.driver= driver

        Email_textbox_field = "#username"
        Password_textbox_field  = "#password"
        Login_Button = "//button[@class='btn btn-primary']"

        def enter_email(self, Email_Address):
            self.driver.find_element_by_css_selector(CashflowLogin.Email_textbox_field).clear()
            self.driver.find_element_by_css_selector(CashflowLogin.Email_textbox_field).send_keys(Email_Address)

        def enter_password(self, Password):
            self.driver.find_element_by_css_selector(CashflowLogin.Password_textbox_field).clear()
            self.driver.find_element_by_css_selector(CashflowLogin.Password_textbox_field).send_keys(Password)

        def click_login(self):
            self.driver.find_element_by_css_xpath(CashflowLogin.Login_Button).click()

        def VerifyLoginpage(self, pagetitle):
            assert pagetitle == self.driver.title

        def SimpleLogout(self):
            self.driver.find_element_by_link_text("Logout").click()

        def VerifyLogoutPage(self, SignedOut):
            assert SignedOut == self.driver.title

        def VerifyValidation(self, Validation):
            assert Validation == self.driver.find_element_by_xpath("//div[@cla  ss='alert alert-danger']").gettext()

        def logout(self):
            self.driver.find_element_by_xpath(
                "//button[@class='ant-btn ant-btn-link HeaderLogo_logo__lmyp5 Button_plain__3UtWY']").click()
            self.driver.find_element_by_link_text("Logout").click()

        def logoutfromClientpage(self):
            self.driver.find_element_by_xpath("//a[normalize-space()='Logout']").click()
