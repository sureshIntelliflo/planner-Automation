import time


class Pensions:

    def __init__(self, driver):
        self.driver = driver

    def Navigatetopensions(self):
        self.driver.find_element_by_xpath("//span[normalize-space()='Plan Inputs']").click()
        self.driver.find_element_by_xpath(
            "//span[@class='text-sm font-normal'][normalize-space()='Pensions']").click()

    def AddNewPensions(self):
        AddnewPension = self.driver.find_element_by_xpath("//span[contains(text(),'Add Pension')]")
        if AddnewPension.is_displayed():
            AddnewPension.click()
        else:
            print("Add Pensions options is not displaying")

    def AddPensionDescription(self, PensionDescription):
        self.driver.find_element_by_xpath("//input[@id='policyDescription']").send_keys(PensionDescription)

    def AddPensionPolicyStructure(self):
       self.driver.find_element_by_xpath("//fieldset[@class='mb-5']//label[1]").click()


    def policyStatus(self,pensionstype):
        status = self.driver.find_element_by_xpath("//div[@class='pt-5']//div[@class='ant-select-selector']")
        if status.is_displayed():
            status.click()
            statustype =  self.driver.find_element_by_xpath(f"//div[contains(text(),'{pensionstype}')]")
            statustype.click()
        else:
            print("status dropdown is not displaying")

    def BenefitBasis(self, Benefitstype):
        type = self.driver.find_element_by_xpath(f"//span[normalize-space()='{Benefitstype}']")
        if type.is_displayed():
            type.click()

    def BenefitStatementValues(self, BenefitIncome, LumpSum):
        benefitamount = self.driver.find_element_by_xpath("//input[@id='benefit_statementBenefit_income_amount']")
        benefitamount.send_keys(BenefitIncome)

        lumpamount = self.driver.find_element_by_xpath("//input[@id='benefit_statementBenefit_lumpSum_amount']")
        lumpamount.send_keys(LumpSum)

    def BenefitContributions(self, IncomeDescription, GrossContributions, PensionBasis):
        linkedemploymentdropdown = self.driver.find_element_by_xpath("//div[@class='flex mb-4']//div[@class='ant-select-selector']")
        if linkedemploymentdropdown.is_displayed():
            linkedemploymentdropdown.click()
            linkedemployemnttype = self.driver.find_element_by_xpath(f"//div[contains(text(),'{IncomeDescription}')]")
            linkedemployemnttype.click()
            GrossContributionseditbox = self.driver.find_element_by_xpath("//input[@id='contribution_grossContribution']")
            if GrossContributionseditbox.is_displayed():
                GrossContributionseditbox.send_keys(GrossContributions)
            else:
                print("unable to find the gross contributions box")
            pensionbasis = self.driver.find_element_by_xpath(f"//span[normalize-space()='{PensionBasis}']")
            pensionbasis.click()
        else:
            print("linked employment dropdown is not displaying")

    def BenefitDeathOptions(self, SpouseIncomeAfterDeath, LumpSumOptions, ServiceMultiplier):
        deathlumpsumoptions = self.driver.find_element_by_xpath("//div[@class='ant-row ant-form-item PensionFormDBDeathSection_wrapper__67YfN ant-form-item-has-success']//div[@class='ant-select-selector']")
        if deathlumpsumoptions.is_displayed():
            deathlumpsumoptions.click()
            self.driver.find_element_by_xpath(f"//div[contains(text(),'{LumpSumOptions}')]").click()
            self.driver.find_element_by_xpath("//input[@id='deathBenefit_multipleDeathLumpSumOption_deathInServiceMultiplier']").send_keys(ServiceMultiplier)

    def AdjustLifetimeAllowance(self):
        self.driver.find_element_by_xpath("//button[@id='lifetimeAllowanceAdjustmentEnabled']").click()

    def AddPension(self, PensionDescription):
        self.driver.find_element_by_xpath("//button[@type='button']//span[contains(text(),'Add Pension')]").click()
        pensionnarrative = self.driver.find_element_by_xpath(f"//span[normalize-space()='{PensionDescription}']")
        if pensionnarrative.is_displayed():
            assert pensionnarrative.text == PensionDescription