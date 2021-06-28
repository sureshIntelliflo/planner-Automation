Feature: Verify the Property

  Scenario: User Login
    Given user logged into application with email as "spped_12501" and password as "Suresh@2021"
    When user logged in and I add client with details name as "Automated User", KnowAs "QA Automation", DOB "01/01/1990",Tax residency "England", gender as "Male" and Create client with case name as "AutomatedQA_AddProperty"

  Scenario Outline: Adding property
    When User in cashflow home page
    Then I add property from property page
    And I provide <PropertyDescription>
    And I provide property details as <PreExisting>
    And I Provide Property Value as <CurrentValue>
    And I provide the base cost for CGT as <BaseCostCGT>
    Examples:
      | PropertyDescription | PreExisting | CurrentValue | BaseCostCGT |

  Scenario Outline: Sale event to property
    Then I enable Sale Event with sale event as <Retire> with Sale Expense % <SaleExpense%>
    Examples:
      | Retire | SaleExpense% |

  Scenario Outline: mortgage to property
    Then I enable Mortgages with <MortagageDescription>, <ReplaymentType>, <MortagageValue>, <InterestRate>, <MortgageStartEvent>, <MortgageCeaseEvent>
    Examples:
      | MortagageDescription | ReplaymentType | MortagageValue | InterestRate | MortgageStartEvent | MortgageCeaseEvent |

  Scenario Outline: Rent to property
    Then I Enable Rental with <Rental>, <RentalExpense>
    And I check allnow mortage interest offset
    Examples:
      | Rental | RentalExpense |

  Scenario Outline: Renovation to property
    Then I enable Renovation with <RenovationCost>, <IncreasedtoPropertyValue>
    And I select Renovation event <RenovationEvent>
    Then I save Property
    Examples:
      | RenovationCost | IncreasedtoPropertyValue | RenovationEvent |
