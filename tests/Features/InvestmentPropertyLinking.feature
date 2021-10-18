Feature: Investment and Properties linking

  @functional
  Scenario Outline: Link investment to property in mortgage offset
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
    And I add investment returns as <Returns>
    Then I add Investment to Baseline scenario <InvestmentDescription>
    And I navigate to Property
    And I add property with <PropertyDescription>
    And I provide property details as <PropertyTyep>
    And I Provide Property Value as <CurrentValue>
    And I provide the base cost for CGT as <BaseCostCGT>
    Then I enable Mortgages with <MortagageDescription>, <ReplaymentType>, <MortagageValue>, <InterestRate>, <MortgageStartEvent>, <MortgageCeaseEvent>
    And I enable mortgage offset with Linked Current Account <InvestmentDescription> and Offset Options <OffsetOptions>
    And i save Mortgage and Property <PropertyDescription>
    And I logout from application
    Examples:
      | Username  | Password    | HoHName    | HoHKnowas | DoB        | TaxResidency | Gender | ClientName                     | InvestmentDescription | InvestmentType         | Investment   | CurrentValue | Returns | PropertyDescription  | PropertyTyep | BaseCostCGT | MortagageDescription | ReplaymentType | MortagageValue | InterestRate | MortgageStartEvent | MortgageCeaseEvent | OffsetOptions                 |
      | Fla_Test1 | Suresh@2021 | Automation | QA        | 01/01/1990 | England      | Male   | Automation Investment property | A_PropertyInvestment  | Offset Current Account | Pre-Existing | 300000       | 9.8     | A_PropertyInvestment | Pre-Existing | 300000      | Automated_Mortage    | Interest Only  | 300000         | 22           | Property Purchase  | Pre-Existing       | Interest Only Reduce Payments |