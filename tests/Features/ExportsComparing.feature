Feature: Exports comparing

  @functional
  Scenario Outline: Verify the exports scenario comparing functionality from plan outputs
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
    And I create new scenario <ScenarioName> <ScenarioDescription>
    Then I navigate to Income page
    And I add new income from income Page
    And I add income description <IncomeDescription>
    And I add Income type <IncomeType>
    And I add income current or future type <CurrentFutureIncome>
    And I add income amount <IncomeAmount>
    Then I add income and verify added income <IncomeDescription>
    And I navigate to protections
    Then I add new Protections <ProtectionDescription>
    Then I select the Type of Protection <ProtectionsType>
    Then I Add protection benefit <IncomeDescription> <DeathInServiceMultiplier>
    And I Add Protections and Verify the Protections <ProtectionDescription>
    And I navigate to plan outputs and select Exports
    Then I download the Comparison exports with default selections with baseline vs scenario <ScenarioName>
    Then I logout from application
    Examples:
      | Username  | Password    | HoHName    | HoHKnowas | DoB        | TaxResidency | Gender | ClientName                 | InvestmentDescription | InvestmentType      | Investment   | CurrentValue | AttitudetoRisk | GrossReturn | Interest | Dividends | Growth | BusinessDescription | BusinessType | BusinessValue | AnnualIncreasepercentage | BaseCostforCGT | ValuationBasis  | SaleEvent | DividendFrequency | DividendAmount | IncreasePerstart | PeriodSetby | LoanDescription | loantype     | OutstandingBalance | InterestRate | repaymentType | ExpenseCategory | ExpensesDescription | EssentialAmount | DiscretionaryAmount | ScenarioName    | ScenarioDescription  | IncomeDescription | IncomeType | CurrentFutureIncome | IncomeAmount | ProtectionDescription | ProtectionsType  | DeathInServiceMultiplier |
      | Fla_Test1 | Suresh#2021 | Automation | QA        | 01/01/1990 | England      | Male   | Automation Exports Compare | Automated_investment  | ISA Stocks & Shares | Pre-Existing | 300000       | High           | 11          | 30       | 40        | 30     | Automated_Business  | Pre-Existing | 500000        | 12                       | 6000           | TRADING_COMPANY | Forever   | One Off           | 5000           | 12               | Events      | Automated_Loan  | Pre-Existing | 3000000            | 14.9         | Repayment     | Long Term Care  | Automated_Expense   | 50000           | 4212                | ExportsScenario | Verifing the exports | Automated_income  | Salary     | Current Income      | 450000       | Automated_Protection  | Death in Service | 2                        |
