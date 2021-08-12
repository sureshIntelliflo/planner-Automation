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

    def BenefitDeathOptions(self, LumpSumOptions, ServiceMultiplier):
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

    def SelectDCpensions(self):
        self.driver.find_element_by_xpath("//span[normalize-space()='Defined Contribution']").click();

    def PolicyType(self, DCType):
        self.driver.find_element_by_xpath("//div[@class='ant-select-selector']").click()
        self.driver.find_element_by_xpath(f"//div[contains(text(),'{DCType}')]").click()


    def DCPensionFund(self, TotalFundValue, DrawdownValue, OriginalCrystallisedAmount):
        self.driver.find_element_by_xpath("//input[@id='totalFundValue_amount']").send_keys(TotalFundValue)
        self.driver.find_element_by_xpath("//input[@id='drawdownValue_amount']").send_keys(DrawdownValue)
        self.driver.find_element_by_xpath("//input[@id='originalAmount_amount']").send_keys(OriginalCrystallisedAmount)

    def Return(self, Risk, GrossReturn):
        self.driver.find_element_by_xpath("//input[@id='riskProfile_id']").click()
        time.sleep(1)
        AttitudetoRisk = self.driver.find_element_by_xpath(f"//div[contains(text(),'{Risk}')]")
        if AttitudetoRisk == "Custom":
            AttitudetoRisk.click()
            self.driver.find_element_by_xpath("//input[@id='grossReturn']").send_keys(GrossReturn)
        else:
            AttitudetoRisk.click()

    def SpecificCharges(self):
        self.driver.find_element_by_xpath("//button[@id='specificChargesEnabled']").click()

    def Contributions(self, ContributionType, TakenBy, IncomeDescription, ContributionAmount, Contribution, Frequency, PeriodSet, StartYear, EndYear):
        self.driver.find_element_by_xpath("//button[@id='contributionsEnabled']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//span[normalize-space()='Add contribution']").click()
        time.sleep(1)
        Contributiontypedropdown = self.driver.find_element_by_xpath("//*[@id='contributionType']//parent::span//parent::div")
        if Contributiontypedropdown.is_displayed():
            Contributiontypedropdown.click()
            time.sleep(1)
            if ContributionType == "Personal - Salary Sacrifice":
                self.driver.find_element_by_xpath(f"//div[contains(text(),'{ContributionType}')]").click()
                time.sleep(1)
                self.driver.find_element_by_xpath(f"(//input[@value='{TakenBy}']//following::span//following::span)[1]").click()
                self.driver.find_element_by_xpath("//div[@class='mb-5']//div[@class='ant-select-selector']").click()
                if TakenBy == "AMOUNT":
                    self.driver.find_element_by_xpath(f"//div[contains(text(),'{IncomeDescription}')]").click()
                    self.driver.find_element_by_xpath("//input[@id='amount_amount']").send_keys(ContributionAmount)
                elif TakenBy == "PERCENTAGE":
                    self.driver.find_element_by_xpath(f"//div[contains(text(),'{IncomeDescription}')]").click()
                    self.driver.find_element_by_xpath("//input[@id='percentage']").send_keys(Contribution)
                time.sleep(1)
                self.driver.find_element_by_xpath(f"//span[normalize-space()='{Frequency}']").click()
                self.driver.find_element_by_xpath(f"(//input[@value='{PeriodSet}']//following::span//following::span)[1]").click()
                if PeriodSet == "YEAR":
                    self.driver.find_element_by_xpath("//input[@id='start_year']").send_keys(StartYear)
                    self.driver.find_element_by_xpath("//input[@id='stop_year']").send_keys(EndYear)
                    self.driver.find_element_by_xpath("//span[normalize-space()='Add Contribution']").click()
                elif PeriodSet == "EVENT":
                    self.driver.find_element_by_xpath("//input[@id='start_event_id']").click()
                    time.sleep(1)
                    self.driver.find_element_by_xpath("//div[contains(text(),'Pre-Existing')]").click()
                    self.driver.find_element_by_xpath("//span[normalize-space()='Add Contribution']").click()
                    time.sleep(2)
            else:
                print("unable to select the contributions type")
        else:
            print("problem wit Contributions dialog")

    def UncrystallisedWithdrawal(self, UncrystallisedWithdrawal):
        self.driver.find_element_by_xpath(f"//span[normalize-space()='{UncrystallisedWithdrawal}']").click()

    def UncrystallisedWithdrawal_Custom(self, withdrawlType, CrystalliseValue, AmountValue, PercentageValue, FrequencyType, PeriodSetValueevent):
        self.driver.find_element_by_xpath("//button[@id='accumulationBenefitsEnabled']").click()
        self.driver.find_element_by_xpath("//span[normalize-space()='Add Uncrystallised Withdrawal']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("(//input[@id='withdrawalType']/following::span)[1]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(f"//div[contains(text(),'{withdrawlType}')]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(f"(//input[@value='{CrystalliseValue}']/following::span)[2]").click()
        time.sleep(1)
        if CrystalliseValue == "AMOUNT":
            self.driver.find_element_by_xpath("//input[@id='amount_amount']").send_keys(AmountValue)
        elif CrystalliseValue == "PERCENTAGE":
            self.driver.find_element_by_xpath("//input[@id='percentage']").send_keys(PercentageValue)

        time.sleep(1)
        self.driver.find_element_by_xpath(f"//span[normalize-space()='{FrequencyType}']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(f"//input[@value='{PeriodSetValueevent}']").click()
        if PeriodSetValueevent == "YEAR":
            self.driver.find_element_by_xpath("//input[@id='stop_year']").send_keys("2100")
        time.sleep(1)
        self.driver.find_element_by_xpath("//span[normalize-space()='Add Withdrawal']").click()
        time.sleep(1)

    def CrystallisedWithdrawal_Custom(self, WithdrawalMethod, CrystallisedAmount, FrequencyType_cy, PeriodSetValueevent_cy):
        self.driver.find_element_by_xpath("//button[@id='decumulationBenefitsEnabled']").click()
        self.driver.find_element_by_xpath("//span[normalize-space()='Add Crystallised Withdrawal']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("(//input[@id='drawdownType']//following::span)[1]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(f"//div[contains(text(),'{WithdrawalMethod}')]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='amount_amount']").send_keys(CrystallisedAmount)
        AddButton = self.driver.find_element_by_xpath("//span[normalize-space()='Add Withdrawal']")
        time.sleep(1)
        self.driver.find_element_by_xpath(f"//span[normalize-space()='{FrequencyType_cy}']").click()
        time.sleep(1)
        if FrequencyType_cy == "Regular":
            self.driver.find_element_by_xpath(f"(//input[@value='{PeriodSetValueevent_cy}']/following::span/following::span)[1]").click()

            if PeriodSetValueevent_cy == "EVENT":
                AddButton.click()
            elif PeriodSetValueevent_cy == "YEAR":
                self.driver.find_element_by_xpath("//input[@id='stop_year']").send_keys("2100")
                AddButton.click()
        elif FrequencyType_cy == "One Off":
            self.driver.find_element_by_xpath(f"(//input[@value='{PeriodSetValueevent_cy}']/following::span/following::span)[1]").click()
            if PeriodSetValueevent_cy == "EVENT":
                AddButton.click()
            elif PeriodSetValueevent_cy == "YEAR":
                AddButton.click()
        time.sleep(2)

    def SchemeSpecificPCLS(self):
        self.driver.find_element_by_xpath("//button[@id='schemeSpecificPensionCommencementLumpSumEnabled']").click()
        self.driver.find_element_by_xpath("//input[@id='schemeSpecificPensionCommencementLumpSum_aDayFundValue_amount']").send_keys("130000")
        self.driver.find_element_by_xpath("//input[@id='schemeSpecificPensionCommencementLumpSum_aDayPclsValue_amount']").send_keys("230000")


    def AddPension(self):
        self.driver.find_element_by_xpath("//button[@type='button']//span[contains(text(),'Add Pension')]").click()

    def VerifyPension(self, PensionDescription):
        Pension = self.driver.find_element_by_xpath(f"//span[normalize-space()='{PensionDescription}']")
        if Pension.is_displayed():
            assert Pension.text == PensionDescription



