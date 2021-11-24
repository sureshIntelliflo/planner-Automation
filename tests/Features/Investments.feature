Feature: Add investments

  @functional
  Scenario Outline: Add investments and exclude in a scenario
    Given user is on cashflow login page
    When User is on Login page and Login as <Username> <Password>
    And User successfully logged into application
    Then User Create client with single HeadofHousehold as <HoHName> <HoHKnowas> <DoB> <TaxResidency> <Gender>
    And User Provide the Client Name as <ClientName>
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
      | Username  | Password  | HoHName    | HoHKnowas | DoB        | TaxResidency | Gender | ClientName             | InvestmentDescription | InvestmentType      | Investment   | CurrentValue | AttitudetoRisk | GrossReturn | Interest | Dividends | Growth | ScenarioName       | ScenarioDescription           | contributionstype | contributionamount | WithdrawalAmount |
      | Fla_Test1 | Fla_Test1 | Automation | QA        | 01/01/1990 | England      | Male   | Automation Investments | Automated_Investment  | ISA Stocks & Shares | Pre-Existing | 300000       | High           | 11          | 30       | 40        | 30     | investmentScenario | Tests performed by automation | Custom            | 30000              | 4500             |
