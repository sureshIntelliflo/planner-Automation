Feature:  Income and DC Pension

  Scenario: Verify the DC Pension and Income linking
    Given user logged into application with email as "spped_12499" and password as "Suresh@2021"
    When user logged in and I add client with details name as "IncomePensionlinked", KnowAs "QA Automation", DOB "01/01/1990",Tax residency "England", gender as "Male" and Create client with case name as "AutomatedQA_IncomePension"
    When User in cashflow home page


