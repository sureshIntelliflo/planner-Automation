Feature:  UNit trust and ISA stocks & shares linking

  Scenario Outline: Verify the Unit trust and ISA stocks & shares linked investment is excluded
    Given user logged into application with email as "FLa_Test2" and password as "Suresh@2021"
    When user logged in and I add client with details name as "Automated User investment", KnowAs "QA Automation", DOB "01/01/1990",Tax residency "England", gender as "Male" and Create client with case name as "AutomatedQA_investment"
    When User in cashflow home page
    Then I navigate to investments page
    And I add Investment Description <InvestmentDescription1>
    And i add investment type as <InvestmentType1>
    And I select investment as Pre existing <Investment1>
    And I add investment value as <CurrentValue1>
    And I add investment returns as <AttitudetoRisk1> <GrossReturn1> <Interest1> <Dividends1> <Growth1>
    Then I add Investment to Baseline scenario <InvestmentDescription1>
    Examples:
      | InvestmentDescription1 | InvestmentType1 | Investment1  | CurrentValue1 | AttitudetoRisk1 | GrossReturn1 | Interest1 | Dividends1 | Growth1 |
      | Automated_UnitTrust    | Unit Trust/OEIC | Pre-Existing | 1000000       | High            | 11           | 30        | 30         | 40      |