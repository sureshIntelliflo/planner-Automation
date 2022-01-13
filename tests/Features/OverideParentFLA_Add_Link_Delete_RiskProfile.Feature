Feature: Add Delete Risk Profile and Manage Client Actions

  Scenario Outline: Verify that Level 2 user Overrides the FLA and add risk profile and linking to Pensions Later delete Risk Profile and Unlock Plan with new Risk Profile
    Given user is on cashflow login page
    When User is on Login page and Login as <Username> <Password>
    And User successfully logged into application
    Then Enable Override Parent Group Assumptions when level 2 user login
    Then User Add new risk profile <RiskProfileName> <GrossReturn> <Interest> <Dividends> <Growth> <Fund_Platform> <FinancialPlanning>
    Then User Create client with single HeadofHousehold as <HoHName> <HoHKnowas> <DoB> <TaxResidency> <Gender>
    And User Provide the Client Name as <ClientName>
    And I navigate to pensions
    Then I Add pensions from pensions page
    Then I add pension description <PensionDescription>
    Then I select policy structure is Defined Contribution
    Then I select policy status <DCType>
    Then I enter pension fund value <TotalFundValue> <DrawdownValue> <OriginalCrystallisedAmount>
    And I select returns <RiskProfileName> <GrossReturn>
    And I Add DC Pension and Verify the Pension <PensionDescription>
    Then User Navigate to FLA page
    And User delete the Automation Risk Profile <RiskProfileName>
    Then User Navigate to client list and Search for Recent Client <ClientName>
    And Unlock the client plan once user get client locked screen using new Risk profile from list <NewRiskProfile>
    Then Navigate to plan outputs and verify graphs loading
    Then Delete Automation Client
    And I logout from application
    Examples:
      | Username  | Password  | RiskProfileName        | GrossReturn | Interest | Dividends | Growth | Fund_Platform | FinancialPlanning | HoHName        | HoHKnowas | DoB        | TaxResidency | Gender | ClientName                             | PensionDescription | DCType       | TotalFundValue | DrawdownValue | OriginalCrystallisedAmount | NewRiskProfile |
      | Fla_Test1 | Fla_Test1 | Automation_RiskProfile | 5.6         | 29.5     | 30.2      | 40.3   | 2.2           | 1.7               | AutomationHOH1 | QA        | 01/01/1990 | England      | Male   | Automation Add Delete FLA Risk Profile | Automated_Pension  | Occupational | 45000          | 4000          | 5000                       | High           |