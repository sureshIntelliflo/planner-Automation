Feature: Income and Protections Linking

  @functional
  Scenario Outline: Verify the income and Death in service Protections linking
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
    And I navigate to protections
    Then I add new Protections <ProtectionDescription>
    Then I select the Type of Protection <ProtectionsType>
    Then I Add protection benefit <IncomeDescription> <DeathInServiceMultiplier>
    And I Add Protections and Verify the Protections <ProtectionDescription>
    Then I logout from application
    Examples:
      | Username  | Password    | HoHName    | HoHKnowas | DoB        | TaxResidency | Gender | ClientName                    | IncomeDescription | IncomeType | CurrentFutureIncome | IncomeAmount | ProtectionDescription | ProtectionsType  | DeathInServiceMultiplier |
      | Fla_Test1 | Suresh@2021 | Automation | QA        | 01/01/1990 | England      | Male   | Automation Income Protections | Automated_income  | Salary     | Current Income      | 450000       | Automated_Protection  | Death in Service | 2                        |


