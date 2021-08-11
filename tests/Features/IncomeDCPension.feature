Feature:  Income and DC Pension

  Scenario Outline: Verify the DC Pension and Income linking
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
    Then I select policy status <DCType>
    Then I enter pension fund value <TotalFundValue> <DrawdownValue> <OriginalCrystallisedAmount>
    And I select returns <Risk> <GrossReturn>
    Then I enable Specific charges switch
    Then I add DC Contributions <ContributionType> <TakenBy> <IncomeDescription> <ContributionAmount> <Contribution> <Frequency> <PeriodSet> <StartYear> <EndYear>
    Examples:
      | IncomeDescription | IncomeType | CurrentFutureIncome | IncomeAmount | PensionDescription | DCType       | TotalFundValue | DrawdownValue | OriginalCrystallisedAmount | Risk | GrossReturn | ContributionType            | TakenBy | ContributionAmount | Contribution | Frequency | PeriodSet | StartYear | EndYear |
      | Automated_income  | Salary     | Current Income      | 450000       | Automated_Pension  | Occupational | 45000          | 4000          | 5000                       | High | 11          | Personal - Salary Sacrifice | AMOUNT  | 5000               | 9 |