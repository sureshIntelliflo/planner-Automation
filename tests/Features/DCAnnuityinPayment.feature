Feature:  DC Annuity in Payment

  @functional
  Scenario Outline: Verify the DC Annuity in payment pensions
    Given user logged into application with email as "FLa_Test2" and password as "Suresh@2021"
    When user logged in and I add client with details name as "DCAnnuityinPayment", KnowAs "QA Automation", DOB "01/01/1990",Tax residency "England", gender as "Male" and Create client with case name as "AutomatedQA_DCAnnuityPension"
    When User in cashflow home page
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
      | PensionDescription   | DCType             | Income_as_Amount | Rate_of_Increase | AnnuityCeaseEvent | InheritedpensionType |
      | Automated_DC_Pension | Annuity in Payment | 10000000         | 12               | Forever           | TAX_FREE             |