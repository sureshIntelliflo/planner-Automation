
Feature:Adding a new client with two HoH to the PLanner
  @functional
  Scenario Outline: Two HoH Client creation for cashflow
    Given user is on cashflow login page
    When user enters email as "FLa_Test2" and password as "Suresh@2021"
    And user clicks on login

    When user sees add client button perform click action
    Then User sees add create client page click on add first head of household button
    And I add First HoH name <Firstname>
    And I add First HohH knowas <FirstknownAS>
    And I select First HoH Badge colour
    And I select First HoH DOB <FirstDoB>
    And I select First HoH Tax Residency <FirstTaxResidency>
    And I select First HoH Gender <FirstGender>
    Then I click on add person button
    Then I click on Add partner/cohabitant button
    And I add Second HoH name <Secondname>
    And I add Second HohH knowas <SecondknownAS>
    And I select Second HoH Badge colour
    And I select Second HoH DOB <SecondDoB>
    And I select relationship between two HoH <relation>
    And I select Second HoH Gender <SecondGender>
    Then I click on add person button
    Then I Provide case name for <ClientName>
    And I create client
    Then I verify Client <ClientName>
    And I logout from application

    Examples:
      | Firstname      | FirstknownAS | FirstDoB   | FirstTaxResidency | FirstGender | Secondname     | SecondknownAS | SecondDoB  | relation | SecondGender | ClientName      |
      | Autonateduser1 | AutoUser1    | 01/01/1985 | England           | Male        | AutomatedUser2 | AutoUser2     | 01/01/1990 | Married  | Female       | AutomatedTwoHoH |