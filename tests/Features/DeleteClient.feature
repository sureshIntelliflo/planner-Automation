Feature: Delete Migrate user from planner

  @functional
  Scenario: login to cashflow with valid credentials
    Given user is on cashflow login page
    When user enters email as "PlanningGroupUser0001" and password as "PlanningGroupUser0001"
    And user clicks on login
    Then user sees page title as "intelliflo planning"

  @functional
  Scenario Outline: Delete users from planner
    When I search for user in Client page <ClientName>
    Then I Delete client from planner
    And I verify Client deletion successful <ClientName>
    Examples:
      | ClientName |


