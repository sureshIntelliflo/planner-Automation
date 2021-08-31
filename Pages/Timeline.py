class Timeline:

    def __init__(self, driver):
        self.driver = driver

    def NavigatetoTimeline(self):
        self.driver.find_element_by_xpath("//span[normalize-space()='Timeline']").click()

    def Addevent(self, EventName, EventYear):
        self.driver.find_element_by_xpath("//button[normalize-space()='Add Event']").click()
        self.driver.find_element_by_xpath("//input[@id='eventName']").send_keys(EventName)
        Year = self.driver.find_element_by_xpath("//input[@id='year']")
        Year.clear()
        Year.send_keys(EventYear)
        self.driver.find_element_by_xpath("//span[contains(text(),'Add Event')]").click()
        timelineyear = self.driver.find_element_by_xpath(f"//span[contains(text(),'{EventName}')]")
        if timelineyear.is_displayed():
            assert True
        else:
            assert False


