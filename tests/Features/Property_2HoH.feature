Feature: Verify the Joint Property

  @functional
  Scenario Outline: Verify the Joint Property with Mortgage
    Given user is on cashflow login page
    When User is on Login page and Login as <Username> <Password>
    And User successfully logged into application
    Then User Create client with single HeadofHousehold as <HoHName> <HoHKnowas> <DoB> <TaxResidency> <Gender>
    And User Add second HoH details as <HohName_2> <HoHKnowas_2> <DoB_2> <relation> <SecondGender>
    And User Provide the Client Name as <ClientName>
    Then I add property from property page
    And I provide <PropertyDescription>
    And I provide property details as <PreExisting>
    And I Provide Property Value as <CurrentValue>
    And I provide the base cost for CGT as <BaseCostCGT>
    Then I enable Sale Event with sale event as forever with Sale Expense % <SaleExpense>
    Then I enable Mortgages with <MortagageDescription>, <ReplaymentType>, <MortagageValue>, <InterestRate>, <MortgageStartEvent>, <MortgageCeaseEvent>
    Then I Enable Rental with <Rental>, <RentalExpense>
    Then I enable Renovation with <RenovationCost>, <IncreasedtoPropertyValue> <RenovationEvent>
    Then I Add Property <PropertyDescription>
    Then I navigate to property page
    Then I create new scenario <ScenarioName> <ScenarioDescription>
    Then I navigate to the recently added Property details
    And I exclude property with all switches ON
    Then I save Property <PropertyDescription>
    Then I verify the scenario is excluded
    And I logout from application

    Examples:
      | Username  | Password    | HoHName        | HoHKnowas | DoB        | TaxResidency | Gender | HohName_2      | HoHKnowas_2 | DoB_2      | SecondGender | relation | ClientName               | PropertyDescription | PreExisting  | CurrentValue | BaseCostCGT | SaleExpense | MortagageDescription | ReplaymentType | MortagageValue | InterestRate | MortgageStartEvent | MortgageCeaseEvent | Rental | RentalExpense | RenovationCost | IncreasedtoPropertyValue | RenovationEvent | ScenarioName     | ScenarioDescription       |
      | Fla_Test1 | Suresh#2021 | AutomationHOH1 | QA        | 01/01/1990 | England      | Male   | AutomationHOH1 | QA2         | 01/01/1991 | Married      | Female   | Automation Join Property | AutomatedProperty1  | Pre Existing | 200000       | 25000       | 25          | Automated_Mortage    | Interest Only  | 300000         | 22           | Property Purchase  | Pre-Existing       | 35000  | 12500         | 42000          | 32000                    | Pre-Existing    | PropertyScenario | Automatedscenario testing |




