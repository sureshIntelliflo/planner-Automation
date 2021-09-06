Feature: Exports

  @functional
  Scenario Outline: Verify the exports functionality from plan outputs
    Given user logged into application with email as "FLa_Test2" and password as "Suresh@2021"
    When user logged in and I add client with details name as "Automated Exports flow", KnowAs "QA Automation", DOB "01/01/1990",Tax residency "England", gender as "Male" and Create client with case name as "AutomatedQA_ExportsFlow"
    When User in cashflow home page
    Then I navigate to investments page
    And I add Investment Description <InvestmentDescription>
    And i add investment type as <InvestmentType>
    And I select investment as Pre existing <Investment>
    And I add investment value as <CurrentValue>
    And I add investment returns as <AttitudetoRisk> <GrossReturn> <Interest> <Dividends> <Growth>
    Then I add Investment to Baseline scenario <InvestmentDescription>
    Then i navigate to business page
    And I add new business with <BusinessDescription>
    Then I add business details <BusinessType> <BusinessValue> <AnnualIncreasepercentage> <BaseCostforCGT> <ValuationBasis>
    Then I add Business sale event <SaleEvent>
    Then I add business dividends <DividendFrequency> <DividendAmount> <IncreasePerstart> <PeriodSetby>
    And I add Business Death options
    Then I save Business and verify <BusinessDescription>
    And I navigate to Loan page
    Then I add new loan with <LoanDescription>
    Then I add Loan details as <loantype> <OutstandingBalance> <InterestRate> <repaymentType>
    Then I save Loan and verify loan <LoanDescription>
    And I navigate to Expense page
    Then I add new expenses with type as <ExpenseCategory>
    Then I add expenses description as <ExpensesDescription>
    Then I add expense expenditure with details as <EssentialAmount> <DiscretionaryAmount>
    Then I save expense and Verify the expense <ExpensesDescription>
    And I navigate to plan outputs and select Exports
    Then I download the exports with default selections
    Then I logout from application
    Examples:
      | InvestmentDescription | InvestmentType      | Investment   | CurrentValue | AttitudetoRisk | GrossReturn | Interest | Dividends | Growth | BusinessDescription | BusinessType | BusinessValue | AnnualIncreasepercentage | BaseCostforCGT | ValuationBasis  | SaleEvent | DividendFrequency | DividendAmount | IncreasePerstart | PeriodSetby | LoanDescription | loantype     | OutstandingBalance | InterestRate | repaymentType | ExpenseCategory | ExpensesDescription | EssentialAmount | DiscretionaryAmount |
      | Automated_investment  | ISA Stocks & Shares | Pre-Existing | 300000       | High           | 11          | 30       | 40        | 30     | Automated_Business  | Pre-Existing | 500000        | 12                       | 6000           | TRADING_COMPANY | Forever   | One Off           | 5000           | 12               | Events      | Automated_Loan  | Pre-Existing | 3000000            | 14.9         | Repayment     | Long Term Care  | Automated_Expense   | 50000           | 4212                |
