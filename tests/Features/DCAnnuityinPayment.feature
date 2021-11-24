Feature:  DC Annuity in Payment

  @functional
  Scenario Outline: Verify the DC Annuity in payment pensions
    Given user is on cashflow login page
    When User is on Login page and Login as <Username> <Password>
    And User successfully logged into application
    Then User Create client with single HeadofHousehold as <HoHName> <HoHKnowas> <DoB> <TaxResidency> <Gender>
    And User Provide the Client Name as <ClientName>
    And I navigate to pensions
    Then I Add pensions from pensions page
    Then I add pension description <PensionDescription>
    Then I select policy structure is Defined Contribution
    Then I select policy status <DCType>
    Then I enter pension fund value <Income_as_Amount> <Rate_of_Increase> <AnnuityCeaseEvent>
    And I enable the Inherited pension and select <InheritedpensionType>
    And I Add DC Pension and Verify the Pension <PensionDescription>
    And I logout from application

    Examples:
      | Username  | Password  | HoHName    | HoHKnowas | DoB        | TaxResidency | Gender | ClientName            | PensionDescription   | DCType             | Income_as_Amount | Rate_of_Increase | AnnuityCeaseEvent | InheritedpensionType |
      | Fla_Test1 | Fla_Test1 | Automation | QA        | 01/01/1990 | England      | Male   | Automation DC Annuity | Automated_DC_Pension | Annuity in Payment | 10000000         | 12               | Forever           | TAX_FREE             |