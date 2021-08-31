class Graphs:

    def __init__(self, driver):
        self.driver = driver

    def NavigatetoGraphs(self):
        self.driver.find_element_by_xpath("//a//child::span[text()='Plan Outputs']").click()
