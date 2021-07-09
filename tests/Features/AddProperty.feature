Feature: Verify the Property

  Scenario Outline: Add Property
    Given user logged into application with email as "spped_12499" and password as "Suresh@2021"
    When user logged in and I add client with details name as "Automated User Property", KnowAs "QA Automation", DOB "01/01/1990",Tax residency "England", gender as "Male" and Create client with case name as "AutomatedQA_AddProperty"
    When User in cashflow home page
    Then I add property from property page
    And I provide <PropertyDescription>
    And I provide property details as <PreExisting>
    And I Provide Property Value as <CurrentValue>
    And I provide the base cost for CGT as <BaseCostCGT>
    Then I enable Sale Event with sale event as forever with Sale Expense % <SaleExpense>
    Then I enable Mortgages with <MortagageDescription>, <ReplaymentType>, <MortagageValue>, <InterestRate>, <MortgageStartEvent>, <MortgageCeaseEvent>
    Then I Enable Rental with <Rental>, <RentalExpense>
    Then I enable Renovation with <RenovationCost>, <IncreasedtoPropertyValue> <RenovationEvent>
    Then I save Property <PropertyDescription>

    Examples:
      | PropertyDescription | PreExisting  | CurrentValue | BaseCostCGT | SaleExpense | MortagageDescription | ReplaymentType | MortagageValue | InterestRate | MortgageStartEvent | MortgageCeaseEvent | Rental | RentalExpense | RenovationCost | IncreasedtoPropertyValue | RenovationEvent |
      | AutomatedProperty1  | Pre Existing | 200000       | 25000       | 25          | Automated_Mortage    | Interest Only  | 300000         | 22           | Property Purchase  | Pre-Existing       | 35000  | 12500         | 42000          | 32000                    | Pre-Existing    |




