Feature:  Income and DC Pension then Exclude income

  Scenario Outline: Verify the DC Pension and Income linking and exclude income
    Given user is on cashflow login page
    When User is on Login page and Login as <Username> <Password>
    And User successfully logged into application
    Then User Create client with single HeadofHousehold as <HoHName> <HoHKnowas> <DoB> <TaxResidency> <Gender>
    And User Provide the Client Name as <ClientName>
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
    And I select Uncrystallised Withdrawal - As Required Method as <UncrystallisedWithdrawal>
    Then I Enable Uncrystallised Withdrawal - Custom <withdrawlType> <CrystalliseValue> <AmountValue> <PercentageValue> <FrequencyType> <PeriodSetValueevent>
    Then I Enable Crystallised Withdrawal_Custom <WithdrawalMethod> <CrystallisedAmount> <FrequencyType_cy> <PeriodSetValueevent_cy>
    Then I enable Scheme Specific PCLS
    And I Add DC Pension and Verify the Pension <PensionDescription>
    Then I exclude Income form Baseline <IncomeDescription>
    And Verify the DC pensions for any breakages <PensionDescription>
    And I logout from application
    Examples:
      | Username  | Password  | HoHName    | HoHKnowas | DoB        | TaxResidency | Gender | ClientName                                    | IncomeDescription | IncomeType | CurrentFutureIncome | IncomeAmount | PensionDescription | DCType       | TotalFundValue | DrawdownValue | OriginalCrystallisedAmount | Risk | GrossReturn | ContributionType            | TakenBy | ContributionAmount | Contribution | Frequency | PeriodSet | StartYear | EndYear | UncrystallisedWithdrawal             | withdrawlType                        | CrystalliseValue | AmountValue | PercentageValue | FrequencyType | PeriodSetValueevent | WithdrawalMethod | CrystallisedAmount | FrequencyType_cy | PeriodSetValueevent_cy |
      | Fla_Test1 | Fla_Test1 | Automation | QA        | 01/01/1990 | England      | Male   | Automation Income DC pension & exclude income | Automated_income  | Salary     | Current Income      | 450000       | Automated_Pension  | Occupational | 45000          | 4000          | 5000                       | High | 11          | Personal - Salary Sacrifice | AMOUNT  | 5000               | 9            | Regular   | EVENT     | 2020      | 2060    | Uncrystallised Fund Pension Lump Sum | Uncrystallised Fund Pension Lump Sum | AMOUNT           | 1000        | 9               | Regular       | YEAR                | Amount           | 5000               | Regular          | YEAR                   |