Feature: Verify the update Assumptions

  Scenario Outline: Verify the Assumptions update and Verify assumptions
    Given user is on cashflow login page
    When User is on Login page and Login as <Username> <Password>
    And User successfully logged into application
    Then User Create client with single HeadofHousehold as <HoHName> <HoHKnowas> <DoB> <TaxResidency> <Gender>
    And User Provide the Client Name as <ClientName>
    Then User Navigate to Assumptions page
    Then User update Tax Residency <NewTaxResidency>
    Then User Update property inflation <NewPropertyInflation>
    Then user enable the Override Returns <FirstYearofOverride> <GrossReturn> <RepeatFrequency>
    And User save assumptions
    Then Verify the Assumptions Narrative <NewPropertyInflation>
    And I logout from application
    Examples:
      | Username  | Password  | HoHName    | HoHKnowas | DoB        | TaxResidency | Gender | ClientName             | NewTaxResidency | NewPropertyInflation | FirstYearofOverride | GrossReturn | RepeatFrequency |
      | Fla_Test1 | Fla_Test1 | Automation | QA        | 01/01/1990 | England      | Male   | Automation Assumptions | Scotland        | 7.7                  | 2035                | 12          | One Off         |
