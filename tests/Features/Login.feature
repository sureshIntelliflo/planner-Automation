Feature: Login

  @functional
  Scenario: login to cashflow with valid credentials
    Given user is on cashflow login page
    When user enters email as "PlanningGroupUser0001" and password as "PlanningGroupUser0001"
    And user clicks on login
    Then user sees page title as "intelliflo planning"

  @functional
  Scenario: User successful Logout from cashflow
    Then user click on logout
    And User sees logout page title as "intelliflo planning"