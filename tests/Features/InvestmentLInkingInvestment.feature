Feature:  UNit trust and ISA stocks & shares linking

  @functional
  Scenario Outline: Verify the Unit trust and ISA stocks & shares linked investment is excluded
    Given user is on cashflow login page
    When User is on Login page and Login as <Username> <Password>
    And User successfully logged into application
    Then User Create client with single HeadofHousehold as <HoHName> <HoHKnowas> <DoB> <TaxResidency> <Gender>
    And User Provide the Client Name as <ClientName>
    Then I navigate to investments page
    And I add Investment Description <InvestmentDescription1>
    And i add investment type as <InvestmentType1>
    And I select investment as Pre existing <Investment1>
    And I add investment value as <CurrentValue1>
    And I add investment returns as <AttitudetoRisk1> <GrossReturn1> <Interest1> <Dividends1> <Growth1>
    Then I add contributions <contributionamount>
    Then I add withdrawals custom <WithdrawalAmount>
    Then I add withdrawals sell whole investments
    Then I add specific charges
    Then I enable death options
    Then I add Investment to Baseline scenario <InvestmentDescription1>
    And I add new investment <InvestmentDescription2>
    And i add investment type as <InvestmentType2>
    And I select investment as Pre existing <Investment2>
    And I add investment value as <CurrentValue2>
    And I add investment returns as <AttitudetoRisk2> <GrossReturn2> <Interest2> <Dividends2> <Growth2>
    And I add contributions <contributionstype> <InvestmentDescription1>
    Then I add withdrawals custom <WithdrawalAmount>
    Then I add withdrawals sell whole investments
    Then I add specific charges
    Then I enable death options
    Then I add Investment to Baseline scenario <InvestmentDescription2>
    And I logout from application
    Examples:
      | Username  | Password  | HoHName    | HoHKnowas | DoB        | TaxResidency | Gender | ClientName                    | InvestmentDescription1 | InvestmentType1 | Investment1  | CurrentValue1 | AttitudetoRisk1 | GrossReturn1 | Interest1 | Dividends1 | Growth1 | InvestmentDescription2         | InvestmentType2     | Investment2  | CurrentValue2 | AttitudetoRisk2 | GrossReturn2 | Interest2 | Dividends2 | Growth2 | contributionamount | contributionstype | WithdrawalAmount |
      | Fla_Test1 | Fla_Test1 | Automation | QA        | 01/01/1990 | England      | Male   | Automation Investment linking | Automated_UnitTrust    | Unit Trust/OEIC | Pre-Existing | 1000000       | High            | 11           | 30        | 30         | 40      | Automated_ISA_stocks_and_share | ISA Stocks & Shares | Pre-Existing | 1200000       | High            | 10           | 30        | 30         | 40      | 2000               | Bed and ISA       | 4000             |