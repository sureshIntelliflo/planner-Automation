Feature: Income and DC pensions

  Scenario Outline: Verify the income and DC Pensions Linking
    Given user logged into application with email as "spped_12499" and password as "Suresh@2021"
    When user logged in and I add client with details name as "IncomePensionlinked", KnowAs "QA Automation", DOB "01/01/1990",Tax residency "England", gender as "Male" and Create client with case name as "AutomatedQA_IncomePension"
    When User in cashflow home page
    Then I navigate to Income page
    And I add new income from income Page
    And I add income description <IncomeDescription>
    And I add Income type <IncomeType>
    And I add income current or future type <CurrentFutureIncome>
    And I add income amount <IncomeAmount>
    Then I add income and verify added income <IncomeDescription>
    And I navigate to pensions
    Then I Add pensions from pensions page
    Then I add pension description <PensionDescription>
    Then I select policy structure is Defined Contribution
    Then I select policy type <pensionstype>
    Then I add pension fund value <TotalFundValue> <DropdownValue> <OriginalCrystallisedAmount>
    Then I add pensions return <AttitudetoRisk>
    Then I enable specific charges
    And I add contributions type <ContributionType> <TakenBy> <IncomeDescription> <ContributionAmount> <Contribution> <Frequency> <StartYear> <EndYear>
    Then I select Uncrystallised Withdrawal - As Required Method <UncrystallisedWithdrawal>
    Then I enable Uncrystallised Withdrawal - Custom <withdrawlType> <CrystalliseValue> <AmountValue> <PercentageValue> <FrequencyType> <PeriodSetValueevent>
    Then I enable Crystallised Withdrawal – Custom <WithdrawalMethod> <FrequencyType> <PeriodSetValueevent>
    Then I enable Scheme Specific PCLS
    And I add Pension and verify added pensions <PensionDescription>
    Examples:
      | IncomeDescription | IncomeType | CurrentFutureIncome | IncomeAmount | PensionDescription | pensionstype | TotalFundValue | DropdownValue | OriginalCrystallisedAmount | AttitudetoRisk | ContributionType            | TakenBy | ContributionAmount | Contribution | Frequency | StartYear | EndYear | UncrystallisedWithdrawal             | withdrawlType                        | CrystalliseValue | AmountValue | PercentageValue | FrequencyType | PeriodSetValueevent | WithdrawalMethod |
      | Automated Income  | Salary     | Current Income      | 450000       | Automated Pension  | Occupational | 123000         | 5000          | 8000                       | High           | Personal - Salary Sacrifice | AMOUNT  | 12000              | 9            | Regular   | 2020      | 2050    | Uncrystallised Fund Pension Lump Sum | Uncrystallised Fund Pension Lump Sum | AMOUNT           | 5400        | 9               | Regular       | EVENT               | Amount           |
