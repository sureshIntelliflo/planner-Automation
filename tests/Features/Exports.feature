Feature: Exports

  Scenario Outline: Verify the exports functionality from plan outputs
    Given user logged into application with email as "FLa_Test2" and password as "Suresh@2021"
    When user logged in and I add client with details name as "Automated User investment", KnowAs "QA Automation", DOB "01/01/1990",Tax residency "England", gender as "Male" and Create client with case name as "AutomatedQA_investment"
    When User in cashflow home page
    Then I navigate to investments page
    And I add Investment Description <InvestmentDescription>
    And i add investment type as <InvestmentType>
    And I select investment as Pre existing <Investment>
    And I add investment value as <CurrentValue>
    And I add investment returns as <AttitudetoRisk> <GrossReturn> <Interest> <Dividends> <Growth>
    Then I add Investment to Baseline scenario <InvestmentDescription>
    Then i navigate to business page
