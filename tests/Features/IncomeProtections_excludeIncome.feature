Feature: Protection income linking and income excluded from scenario

  Scenario Outline: Verify the income and Death in service Protections linking then Exclude income from scenario
    Given user logged into application with email as "FLa_Test2" and password as "Suresh@2021"
    When user logged in and I add client with details name as "incomeProtectionlinking", KnowAs "QA Automation", DOB "01/01/1990",Tax residency "England", gender as "Male" and Create client with case name as "AutomatedQA_IncomeProtection"
    When User in cashflow home page
    Then I navigate to Income page
    And I add new income from income Page
    And I add income description <IncomeDescription>
    And I add Income type <IncomeType>
    And I add income current or future type <CurrentFutureIncome>
    And I add income amount <IncomeAmount>
    Then I add income and verify added income <IncomeDescription>
    And I navigate to protections
    Then I add new Protections <ProtectionDescription>
    Then I select the Type of Protection <ProtectionsType>
    Then I Add protection benefit <IncomeDescription> <DeathInServiceMultiplier>
    And I Add Protections and Verify the Protections <ProtectionDescription>
    Then I exclude Income form Baseline <IncomeDescription>
    And Verify the Protections for any breakages <ProtectionDescription>
    Then I logout from application
    Examples:
      | IncomeDescription | IncomeType | CurrentFutureIncome | IncomeAmount | ProtectionDescription | ProtectionsType  | DeathInServiceMultiplier |
      | Automated_income  | Salary     | Current Income      | 450000       | Automated_Protection  | Death in Service | 2                        |


