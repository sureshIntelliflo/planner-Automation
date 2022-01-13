Feature: Add new risk profile and link to plan

  Scenario Outline: Verify that Level 2 user Overrides the FLA and add risk profile and linking to investments
    Given user is on cashflow login page
    When User is on Login page and Login as <Username> <Password>
    And User successfully logged into application
    Then Enable Override Parent Group Assumptions when level 2 user login
    Then User Add new risk profile <RiskProfileName> <GrossReturn> <Interest> <Dividends> <Growth> <Fund_Platform> <FinancialPlanning>
    Then User Create client with single HeadofHousehold as <HoHName> <HoHKnowas> <DoB> <TaxResidency> <Gender>
    And User Add second HoH details as <HohName_2> <HoHKnowas_2> <DoB_2> <relation> <SecondGender>
    And User Provide the Client Name as <ClientName>
    Then I navigate to investments page
    And I add Investment Description <InvestmentDescription>
    And i add investment type as <InvestmentType>
    And I select investment as Pre existing <Investment>
    And I add investment value as <CurrentValue>
    And I add investment returns as <AttitudetoRisk>
    Then I add Investment to Baseline scenario <InvestmentDescription>
    Then I verify the investment in scenario <InvestmentDescription>
    And User Navigate to FLA page and Disable the child override FLA and use parent risk profiles assumptions
    Then User navigate to client list then select recent client and unlock the client with Parent Risk profile <ParentRiskprofile> <ClientName>
    #Then I re-verify the investment plan is using parent Risk profile returns selected or not <InvestmentDescription> <ParentRiskprofile>
    And I logout from application

    Examples:
      | Username  | Password  | RiskProfileName        | GrossReturn | Interest | Dividends | Growth | Fund_Platform | FinancialPlanning | HoHName        | HoHKnowas | DoB        | TaxResidency | Gender | HohName_2      | HoHKnowas_2 | DoB_2      | relation | SecondGender | ClientName                  | InvestmentDescription | InvestmentType      | Investment   | CurrentValue | AttitudetoRisk         | ParentRiskprofile |
      | Fla_Test1 | Fla_Test1 | Automation_RiskProfile | 5.6         | 29.5     | 30.2      | 40.3   | 2.2           | 1.7               | AutomationHOH1 | QA        | 01/01/1990 | England      | Male   | AutomationHOH1 | QA2         | 01/01/1991 | Married  | Female       | Automation FLA Risk Profile | Automated_Investment  | ISA Stocks & Shares | Pre-Existing | 300000       | Automation_RiskProfile | High              |

