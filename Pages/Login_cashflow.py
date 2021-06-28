

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