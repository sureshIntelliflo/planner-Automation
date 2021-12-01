Feature:
  Search and Rename Client

  @functional
  Scenario Outline: Search for existing client and Update Client
    Given user is on cashflow login page
    When User is on Login page and Login as <Username> <Password>
    And User successfully logged into application
    Then User Create client with single HeadofHousehold as <HoHName> <HoHKnowas> <DoB> <TaxResidency> <Gender>
    And User Provide the Client Name as <ClientName>
    Then Navigate to Clients page
    Then I search for Client <Clientname>
    And I select the Client from search results <Clientname>
    Then I goto Client Settings
    And I change the client name to new name <NewClientName>
    Then I update the client changes
    Then I verify client name on Cashflow
    Then I delete the created Client
    And I logout from application
    Examples:
      | Username  | Password  | HoHName    | HoHKnowas | DoB        | TaxResidency | Gender | ClientName                      | Clientname | NewClientName  |
      | Fla_Test1 | Fla_Test1 | Automation | QA        | 01/01/1990 | England      | Male   | Automation Search Rename Client | Automation | Client Remaned |


