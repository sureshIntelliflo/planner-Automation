Feature: Two Head of households login

  Scenario Outline: Verify Two HOH login feature
    Given user is on cashflow login page
    When User is on Login page and Login as <Username> <Password>
    And User successfully logged into application
    Then User Create client with single HeadofHousehold as <HoHName> <HoHKnowas> <DoB> <TaxResidency> <Gender>
    And User Add second HoH details as <HohName_2> <HoHKnowas_2> <DoB_2> <relation> <SecondGender>
    And User Provide the Client Name as <ClientName>
    Examples:
      | Username  | Password    | HoHName        | HoHKnowas | DoB        | TaxResidency | Gender | HohName_2      | HoHKnowas_2 | DoB_2      | SecondGender | relation | ClientName              |
      | Fla_Test1 | Suresh@2021 | AutomationHOH1 | QA        | 01/01/1990 | England      | Male   | AutomationHOH1 | QA2         | 01/01/1991 | Married      | Female   | Automation 2HoH Clients |

