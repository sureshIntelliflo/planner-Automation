# coding=utf-8
"""Exports comparing feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('features\ExportsComparing.feature', 'Verify the exports scenario comparing functionality from plan outputs')
def test_verify_the_exports_scenario_comparing_functionality_from_plan_outputs():
    """Verify the exports scenario comparing functionality from plan outputs."""


@given('user logged into application with email as "FLa_Test2" and password as "Suresh@2021"')
def user_logged_into_application_with_email_as_fla_test2_and_password_as_suresh2021():
    """user logged into application with email as "FLa_Test2" and password as "Suresh@2021"."""
    raise NotImplementedError


@when('User in cashflow home page')
def user_in_cashflow_home_page():
    """User in cashflow home page."""
    raise NotImplementedError


@when('user logged in and I add client with details name as "Automated Exports flow", KnowAs "QA Automation", DOB "01/01/1990",Tax residency "England", gender as "Male" and Create client with case name as "AutomatedQA_ExportsFlow"')
def user_logged_in_and_i_add_client_with_details_name_as_automated_exports_flow_knowas_qa_automation_dob_01011990tax_residency_england_gender_as_male_and_create_client_with_case_name_as_automatedqa_exportsflow():
    """user logged in and I add client with details name as "Automated Exports flow", KnowAs "QA Automation", DOB "01/01/1990",Tax residency "England", gender as "Male" and Create client with case name as "AutomatedQA_ExportsFlow"."""
    raise NotImplementedError


@then('I Add Protections and Verify the Protections <ProtectionDescription>')
def i_add_protections_and_verify_the_protections_protectiondescription():
    """I Add Protections and Verify the Protections <ProtectionDescription>."""
    raise NotImplementedError


@then('I Add protection benefit <IncomeDescription> <DeathInServiceMultiplier>')
def i_add_protection_benefit_incomedescription_deathinservicemultiplier():
    """I Add protection benefit <IncomeDescription> <DeathInServiceMultiplier>."""
    raise NotImplementedError


@then('I add Business Death options')
def i_add_business_death_options():
    """I add Business Death options."""
    raise NotImplementedError


@then('I add Business sale event <SaleEvent>')
def i_add_business_sale_event_saleevent():
    """I add Business sale event <SaleEvent>."""
    raise NotImplementedError


@then('I add Income type <IncomeType>')
def i_add_income_type_incometype():
    """I add Income type <IncomeType>."""
    raise NotImplementedError


@then('I add Investment Description <InvestmentDescription>')
def i_add_investment_description_investmentdescription():
    """I add Investment Description <InvestmentDescription>."""
    raise NotImplementedError


@then('I add Investment to Baseline scenario <InvestmentDescription>')
def i_add_investment_to_baseline_scenario_investmentdescription():
    """I add Investment to Baseline scenario <InvestmentDescription>."""
    raise NotImplementedError


@then('I add Loan details as <loantype> <OutstandingBalance> <InterestRate> <repaymentType>')
def i_add_loan_details_as_loantype_outstandingbalance_interestrate_repaymenttype():
    """I add Loan details as <loantype> <OutstandingBalance> <InterestRate> <repaymentType>."""
    raise NotImplementedError


@then('I add business details <BusinessType> <BusinessValue> <AnnualIncreasepercentage> <BaseCostforCGT> <ValuationBasis>')
def i_add_business_details_businesstype_businessvalue_annualincreasepercentage_basecostforcgt_valuationbasis():
    """I add business details <BusinessType> <BusinessValue> <AnnualIncreasepercentage> <BaseCostforCGT> <ValuationBasis>."""
    raise NotImplementedError


@then('I add business dividends <DividendFrequency> <DividendAmount> <IncreasePerstart> <PeriodSetby>')
def i_add_business_dividends_dividendfrequency_dividendamount_increaseperstart_periodsetby():
    """I add business dividends <DividendFrequency> <DividendAmount> <IncreasePerstart> <PeriodSetby>."""
    raise NotImplementedError


@then('I add expense expenditure with details as <EssentialAmount> <DiscretionaryAmount>')
def i_add_expense_expenditure_with_details_as_essentialamount_discretionaryamount():
    """I add expense expenditure with details as <EssentialAmount> <DiscretionaryAmount>."""
    raise NotImplementedError


@then('I add expenses description as <ExpensesDescription>')
def i_add_expenses_description_as_expensesdescription():
    """I add expenses description as <ExpensesDescription>."""
    raise NotImplementedError


@then('I add income amount <IncomeAmount>')
def i_add_income_amount_incomeamount():
    """I add income amount <IncomeAmount>."""
    raise NotImplementedError


@then('I add income and verify added income <IncomeDescription>')
def i_add_income_and_verify_added_income_incomedescription():
    """I add income and verify added income <IncomeDescription>."""
    raise NotImplementedError


@then('I add income current or future type <CurrentFutureIncome>')
def i_add_income_current_or_future_type_currentfutureincome():
    """I add income current or future type <CurrentFutureIncome>."""
    raise NotImplementedError


@then('I add income description <IncomeDescription>')
def i_add_income_description_incomedescription():
    """I add income description <IncomeDescription>."""
    raise NotImplementedError


@then('I add investment returns as <AttitudetoRisk> <GrossReturn> <Interest> <Dividends> <Growth>')
def i_add_investment_returns_as_attitudetorisk_grossreturn_interest_dividends_growth():
    """I add investment returns as <AttitudetoRisk> <GrossReturn> <Interest> <Dividends> <Growth>."""
    raise NotImplementedError


@then('I add investment value as <CurrentValue>')
def i_add_investment_value_as_currentvalue():
    """I add investment value as <CurrentValue>."""
    raise NotImplementedError


@then('I add new Protections <ProtectionDescription>')
def i_add_new_protections_protectiondescription():
    """I add new Protections <ProtectionDescription>."""
    raise NotImplementedError


@then('I add new business with <BusinessDescription>')
def i_add_new_business_with_businessdescription():
    """I add new business with <BusinessDescription>."""
    raise NotImplementedError


@then('I add new expenses with type as <ExpenseCategory>')
def i_add_new_expenses_with_type_as_expensecategory():
    """I add new expenses with type as <ExpenseCategory>."""
    raise NotImplementedError


@then('I add new income from income Page')
def i_add_new_income_from_income_page():
    """I add new income from income Page."""
    raise NotImplementedError


@then('I add new loan with <LoanDescription>')
def i_add_new_loan_with_loandescription():
    """I add new loan with <LoanDescription>."""
    raise NotImplementedError


@then('I create new scenario <ScenarioName> <ScenarioDescription>')
def i_create_new_scenario_scenarioname_scenariodescription():
    """I create new scenario <ScenarioName> <ScenarioDescription>."""
    raise NotImplementedError


@then('I download the Comparison exports with default selections with baseline vs scenario <ScenarioName>')
def i_download_the_comparison_exports_with_default_selections_with_baseline_vs_scenario_scenarioname():
    """I download the Comparison exports with default selections with baseline vs scenario <ScenarioName>."""
    raise NotImplementedError


@then('I logout from application')
def i_logout_from_application():
    """I logout from application."""
    raise NotImplementedError


@then('I navigate to Expense page')
def i_navigate_to_expense_page():
    """I navigate to Expense page."""
    raise NotImplementedError


@then('I navigate to Income page')
def i_navigate_to_income_page():
    """I navigate to Income page."""
    raise NotImplementedError


@then('I navigate to Loan page')
def i_navigate_to_loan_page():
    """I navigate to Loan page."""
    raise NotImplementedError


@then('I navigate to investments page')
def i_navigate_to_investments_page():
    """I navigate to investments page."""
    raise NotImplementedError


@then('I navigate to plan outputs and select Exports')
def i_navigate_to_plan_outputs_and_select_exports():
    """I navigate to plan outputs and select Exports."""
    raise NotImplementedError


@then('I navigate to protections')
def i_navigate_to_protections():
    """I navigate to protections."""
    raise NotImplementedError


@then('I save Business and verify <BusinessDescription>')
def i_save_business_and_verify_businessdescription():
    """I save Business and verify <BusinessDescription>."""
    raise NotImplementedError


@then('I save Loan and verify loan <LoanDescription>')
def i_save_loan_and_verify_loan_loandescription():
    """I save Loan and verify loan <LoanDescription>."""
    raise NotImplementedError


@then('I save expense and Verify the expense <ExpensesDescription>')
def i_save_expense_and_verify_the_expense_expensesdescription():
    """I save expense and Verify the expense <ExpensesDescription>."""
    raise NotImplementedError


@then('I select investment as Pre existing <Investment>')
def i_select_investment_as_pre_existing_investment():
    """I select investment as Pre existing <Investment>."""
    raise NotImplementedError


@then('I select the Type of Protection <ProtectionsType>')
def i_select_the_type_of_protection_protectionstype():
    """I select the Type of Protection <ProtectionsType>."""
    raise NotImplementedError


@then('i add investment type as <InvestmentType>')
def i_add_investment_type_as_investmenttype():
    """i add investment type as <InvestmentType>."""
    raise NotImplementedError


@then('i navigate to business page')
def i_navigate_to_business_page():
    """i navigate to business page."""
    raise NotImplementedError

