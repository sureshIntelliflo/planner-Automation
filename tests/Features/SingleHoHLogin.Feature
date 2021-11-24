Feature: Single Head of households login

  Scenario Outline: Verify Single HOH login feature
    Given user is on cashflow login page
    When User is on Login page and Login as <Username> <Password>
    And User successfully logged into application
    Then User Create client with single HeadofHousehold as <HoHName> <HoHKnowas> <DoB> <TaxResidency> <Gender>
    And User Provide the Client Name as <ClientName>
    Examples:
      | Username  | Password  | HoHName    | HoHKnowas | DoB        | TaxResidency | Gender | ClientName             |
      | Fla_Test1 | Fla_Test1 | Automation | QA        | 01/01/1990 | England      | Male   | Automation 1HoH Client |

