Feature: Income and DB pensions

  Scenario Outline: Verify the income and DB Pensions Linking
    Given user logged into application with email as "FLa_Test2" and password as "Suresh@2021"
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
      | IncomeDescription | IncomeType | CurrentFutureIncome | IncomeAmount | PensionDescription  | pensionstype | Benefitstype | BenefitIncome | LumpSum | GrossContributions | PensionBasis     | LumpSumOptions | ServiceMultiplier |
      | Automated_income  | Salary     | Current Income      | 450000       | Automated_DBPension | Active       | Statement    | 31200         | 500000  | 12.7               | Relief At Source | Multiple       | 2                 |


