import time


class Exports:

    def __init__(self, driver):
        self.driver = driver

    def NavigatetoExports(self):
        self.driver.find_element_by_xpath("//span[@class='text-sm font-semibold'][normalize-space()='Plan Outputs']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//a[4]//div[1]//div[1]//*[local-name()='svg']").click()
        time.sleep(2)

    def Exportdownload(self):
        self.driver.find_element_by_xpath("//span[normalize-space()='Download Report']").click()
        time.sleep(4)
