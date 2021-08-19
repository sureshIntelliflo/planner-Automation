import time


class CommonFunctions:

    def __init__(self, driver):
        self.driver = driver

    def DeleteClient(self):
        self.driver.find_element_by_xpath("//span[normalize-space()='Summary']").click()
        self.driver.find_element_by_xpath("//span[normalize-space()='Client Settings']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@type='submit']//span[contains(text(),'Delete Client')]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class='flex justify-end']//div//span[contains(text(),'Delete Client')]").click()
        time.sleep(2)
        success = self.driver.find_element_by_xpath("//span[normalize-space()='Client has been deleted']")
        if success.is_displayed:
            print("Client deleted successfully")
        else:
            print("unable to delete the client")