Feature: Income and DB pensions

  @functional
  Scenario Outline: Verify the income and DB Pensions Linking
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
    Then I select policy structure is Defined Benefit
    Then I select policy status <pensionstype>
    Then I add benefit basis <Benefitstype>
    Then I add benefit income <BenefitIncome> and benefit lump sum <LumpSum>
    Then I add contributions with income linking <IncomeDescription> with gross contributions <GrossContributions> pension basis <PensionBasis>
    Then I add death options with spouse income after death and death lump sum <LumpSumOptions> <ServiceMultiplier>
    Then I enable adjust lifetime allowance
    And I add Pension and verify added pensions <PensionDescription>z
    And I logout from application
    Examples:
      | Username  | Password    | HoHName    | HoHKnowas | DoB        | TaxResidency | Gender | ClientName                   | IncomeDescription | IncomeType | CurrentFutureIncome | IncomeAmount | PensionDescription  | pensionstype | Benefitstype | BenefitIncome | LumpSum | GrossContributions | PensionBasis     | LumpSumOptions | ServiceMultiplier |
      | Fla_Test1 | Suresh#2021 | Automation | QA        | 01/01/1990 | England      | Male   | Automation Income DB Pension | Automated_income  | Salary     | Current Income      | 450000       | Automated_DBPension | Active       | Statement    | 31200         | 500000  | 12.7               | Relief At Source | Multiple       | 2                 |


