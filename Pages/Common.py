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
            assert True
        else:
            print("unable to delete the client")
            assert False

    def clientSerach(self, Clientname):
        self.driver.find_element_by_xpath(" //input[@placeholder='Search...' and @type='text']").send_keys(Clientname)
        self.driver.find_element_by_xpath("//button//span[@aria-label='search']").click()
        results = self.driver.find_elements_by_xpath(
            "//*[@id='i4c-application-ui']//div[@class='my-5']//span[@class='block text-lg truncate']")
        for resultslist in results:
            if Clientname in resultslist.text:
                resultslist.click()
                break
        time.sleep(1)



