Feature: Add investments

  Scenario Outline: Add investments and exclude in a scenario
    Given user logged into application with email as "spped_12499" and password as "Suresh@2021"
    When user logged in and I add client with details name as "Automated User investment", KnowAs "QA Automation", DOB "01/01/1990",Tax residency "England", gender as "Male" and Create client with case name as "AutomatedQA_investment"
    When User in cashflow home page
    Then I navigate to investments page
    And I add Investment Description <InvestmentDescription>
    And i add investment type as <InvestmentType>
    And I select investment as Pre existing <Investment>
    And I add investment value as <CurrentValue>
    And I add investment returns as <AttitudetoRisk> <GrossReturn> <Interest> <Dividends> <Growth>
    Then I add Investment to Baseline scenario <InvestmentDescription>
    And I exclude from the Baseline scenario <InvestmentDescription>
    And I verify invesment is excluded from baseline scenario <InvestmentDescription>
    Then I create new scenario <ScenarioName> <ScenarioDescription>
    Then I make plan include in scenario <InvestmentDescription>
    Then I add contributions <contributionstype> <contributionamount>
    Then I add withdrawals custom <WithdrawalAmount>
    Then I add withdrawals sell whole investments
    Then I add specific charges
    Then I enable death options
    And I save Investments
    Then I verify the investment in scenario <InvestmentDescription>
    And I logout from application
    Examples:
      | InvestmentDescription | InvestmentType      | Investment   | CurrentValue | AttitudetoRisk | GrossReturn | Interest | Dividends | Growth | ScenarioName       | ScenarioDescription           | contributionstype | contributionamount | WithdrawalAmount |
      | Automated_Investment  | ISA Stocks & Shares | Pre-Existing | 300000       | High           | 11          | 30       | 40        | 30     | investmentScenario | Tests performed by automation | Custom            | 30000              | 4500             |
