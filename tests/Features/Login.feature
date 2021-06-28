
Feature: Login

    Scenario: login to cashflow with valid credentials
        Given user is on cashflow login page
        When user enters email as "spped_12501" and password as "Suresh@2021"
        And user clicks on login
        Then user sees page title as "intelliflo planning"

    Scenario: User successful Logout from cashflow
        Then user click on logout
        And User sees logout page title as "Signed Out"

