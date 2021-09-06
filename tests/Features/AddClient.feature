
Feature:Adding a new client to the PLanner
  @functional
  Scenario Outline: Single HoH Client creation for cashflow
    Given user is on cashflow login page
    When user enters email as "FLa_Test2" and password as "Suresh@2021"
    And user clicks on login

    When user sees add client button perform click action
    Then User sees add create client page click on add first head of household button
    And I add HoH name <name>
    And I add HohH knowas <knownAS>
    And I select HoH Badge colour
    And I select HoH DOB <DoB>
    And I select HoH Tax Residency <TaxResidency>
    And I select HoH Gender <Gender>
    Then I click on add person button
    Then I Provide case name for <ClientName>
    And I create client
    Then I verify Client <ClientName>
    And I logout from application

    Examples:
      | name           | knownAS       | DoB        | TaxResidency | Gender | ClientName  |
      | Automated User | QA Automation | 01/01/1990 | England      | Male   | AutomatedQA |