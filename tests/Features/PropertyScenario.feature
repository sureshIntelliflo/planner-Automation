Feature:  Scenario mode for property to exclude

  Scenario Outline: Scenario mode for property to exclude
    Given user logged into application with email as "spped_12499" and password as "Suresh@2021"
    When user Search for existing client <Existingclient>
    Then I navigate to property page
    Then I create new scenario <ScenarioName> <ScenarioDescription>
    Then I navigate to the Property details <PropertyDescription>
    And I exclude property with all switches ON
    Then I save Property <PropertyDescription>
    Then I verify the scenario is excluded
    And I logout from application
    Examples:
      | Existingclient          | ScenarioName     | ScenarioDescription       | PropertyDescription |
      | AutomatedQA_AddProperty | PropertyScenario | Automatedscenario testing | AutomatedProperty1  |