Feature:
  Search and Rename Client

  @functional
  Scenario Outline: Search for existing client and Update Client
    Given user is on cashflow login page
    When user enters email as "Fla_Test1" and password as "Fla_Test1"
    And user clicks on login

    Then I search for Client <Clientname>
    And I select the Client from search results <Clientname>
    Then I goto Client Settings
    And I change the client name to new name <NewClientName>
    Then I update the client changes
    Then I verify client name on Cashflow

    And I logout from application
    Examples:
      | Clientname | NewClientName       |
      | Automation | AutomatedQA_Updated |