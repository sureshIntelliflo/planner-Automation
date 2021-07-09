Feature: Add investments

  Scenario Outline: Add investments and exclude in a scenario
    Given user logged into application with email as "spped_12499" and password as "Suresh@2021"
    When user logged in and I add client with details name as "Investment property linked", KnowAs "QA Automation", DOB "01/01/1990",Tax residency "England", gender as "Male" and Create client with case name as "AutomatedQA_InvestmentProperty"
    When User in cashflow home page
    Then I navigate to investments page
    And I add Investment Description <InvestmentDescription>
    And i add investment type as <InvestmentType>
    And I select investment as Pre existing <Investment>
    And I add investment value as <CurrentValue>
    And I add investment returns as <Returns>
    Then I add Investment to Baseline scenario <InvestmentDescription>
    And I navigate to Property
    And I add property with <PropertyDescription>
    And I provide property details as <PropertyTyep>
    And I Provide Property Value as <CurrentValue>
    And I provide the base cost for CGT as <BaseCostCGT>
    Then I enable Mortgages with <MortagageDescription>, <ReplaymentType>, <MortagageValue>, <InterestRate>, <MortgageStartEvent>, <MortgageCeaseEvent>
    And I enable mortgage offset with Linked Current Account <InvestmentDescription> and Offset Options <OffsetOptions>
    And i save Mortgage and Propery
    Then I navigate to tables
    Examples:
      | InvestmentDescription        | InvestmentType         | Investment   | CurrentValue | Returns | PropertyDescription          | PropertyTyep | CurrentValue | BaseCostCGT | MortagageDescription | ReplaymentType | MortagageValue | InterestRate | MortgageStartEvent | MortgageCeaseEvent |
      | Automated_InvestmentProperty | Offset Current Account | Pre-Existing | 300000       | 9.8     | Automated_PropertyInvestment | Pre-Existing | 300000       | 20000       | Automated_Mortage    | Interest Only  | 300000         | 22           | Property Purchase  | Pre-Existing       |
