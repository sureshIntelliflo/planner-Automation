Feature: Wizards - Capacity of Loss Wizard

  @functional
  Scenario Outline: Verify the Capacity of Loss Wizard functionality from Wizards
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
    And I add investment returns as <AttitudetoRisk> <GrossReturn> <Interest> <Dividends> <Growth>
    Then I add Investment to Baseline scenario <InvestmentDescription>
    #Then i navigate to business page
    #And I add new business with <BusinessDescription>
   # Then I add business details <BusinessType> <BusinessValue> <AnnualIncreasepercentage> <BaseCostforCGT> <ValuationBasis>
    #Then I add Business sale event <SaleEvent>
    #Then I add business dividends <DividendFrequency> <DividendAmount> <IncreasePerstart> <PeriodSetby>
    #And I add Business Death options
    #Then I save Business and verify <BusinessDescription>
    #And I navigate to Loan page
    #Then I add new loan with <LoanDescription>
    #Then I add Loan details as <loantype> <OutstandingBalance> <InterestRate> <repaymentType>
    #Then I save Loan and verify loan <LoanDescription>
    #And I navigate to Expense page
    #Then I add new expenses with type as <ExpenseCategory>
    #Then I add expenses description as <ExpensesDescription>
    #Then I add expense expenditure with details as <EssentialAmount> <DiscretionaryAmount>
    #Then I save expense and Verify the expense <ExpensesDescription>
    Then I run the Capacity of Loss Report with  <FinancialGoal> <Goaltype> <TargetYear> <MarketCrashPlan> <CrashYear> <UserDefinedMaxLoss>
    And I verify the wizards results
    Then I export the  wizards results
    Then I logout from application
    Examples:
      | Username  | Password  | HoHName    | HoHKnowas | DoB        | TaxResidency | Gender | ClientName                  | InvestmentDescription | InvestmentType      | Investment   | CurrentValue | AttitudetoRisk | GrossReturn | Interest | Dividends | Growth | FinancialGoal | Goaltype     | TargetYear | MarketCrashPlan | CrashYear | UserDefinedMaxLoss |
      | Fla_Test1 | Fla_Test1 | Automation | QA        | 01/01/1990 | England      | Male   | Automation Capacity of Loss | Automated_investment  | ISA Stocks & Shares | Pre-Existing | 300000       | High           | 11          | 30       | 40        | 30     | 50000         | At Any Point | 2035       | Specific Year   | 2035      | 2                  |
