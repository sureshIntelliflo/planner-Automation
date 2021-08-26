# coding=utf-8
"""Exports feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('features\Exports.feature', 'Verify the exports functionality from plan outputs')
def test_verify_the_exports_functionality_from_plan_outputs():
    """Verify the exports functionality from plan outputs."""


@given('user logged into application with email as "FLa_Test2" and password as "Suresh@2021"')
def user_logged_into_application_with_email_as_fla_test2_and_password_as_suresh2021():
    """user logged into application with email as "FLa_Test2" and password as "Suresh@2021"."""
    raise NotImplementedError


@when('User in cashflow home page')
def user_in_cashflow_home_page():
    """User in cashflow home page."""
    raise NotImplementedError


@when('user logged in and I add client with details name as "Automated User investment", KnowAs "QA Automation", DOB "01/01/1990",Tax residency "England", gender as "Male" and Create client with case name as "AutomatedQA_investment"')
def user_logged_in_and_i_add_client_with_details_name_as_automated_user_investment_knowas_qa_automation_dob_01011990tax_residency_england_gender_as_male_and_create_client_with_case_name_as_automatedqa_investment():
    """user logged in and I add client with details name as "Automated User investment", KnowAs "QA Automation", DOB "01/01/1990",Tax residency "England", gender as "Male" and Create client with case name as "AutomatedQA_investment"."""
    raise NotImplementedError


@then('I add Business Death options')
def i_add_business_death_options():
    """I add Business Death options."""
    raise NotImplementedError


@then('I add Business sale event <SaleEvent>')
def i_add_business_sale_event_saleevent():
    """I add Business sale event <SaleEvent>."""
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


@then('I add investment returns as <AttitudetoRisk> <GrossReturn> <Interest> <Dividends> <Growth>')
def i_add_investment_returns_as_attitudetorisk_grossreturn_interest_dividends_growth():
    """I add investment returns as <AttitudetoRisk> <GrossReturn> <Interest> <Dividends> <Growth>."""
    raise NotImplementedError


@then('I add investment value as <CurrentValue>')
def i_add_investment_value_as_currentvalue():
    """I add investment value as <CurrentValue>."""
    raise NotImplementedError


@then('I add new business with <BusinessDescription>')
def i_add_new_business_with_businessdescription():
    """I add new business with <BusinessDescription>."""
    raise NotImplementedError


@then('I add new expenses with type as <ExpenseCategory>')
def i_add_new_expenses_with_type_as_expensecategory():
    """I add new expenses with type as <ExpenseCategory>."""
    raise NotImplementedError


@then('I add new loan with <LoanDescription>')
def i_add_new_loan_with_loandescription():
    """I add new loan with <LoanDescription>."""
    raise NotImplementedError





@then('I navigate to Expense page')
def i_navigate_to_expense_page():
    """I navigate to Expense page."""
    raise NotImplementedError


@then('I navigate to Loan page')
def i_navigate_to_loan_page():
    """I navigate to Loan page."""
    raise NotImplementedError


@then('I navigate to investments page')
def i_navigate_to_investments_page():
    """I navigate to investments page."""
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


@then('i add investment type as <InvestmentType>')
def i_add_investment_type_as_investmenttype():
    """i add investment type as <InvestmentType>."""
    raise NotImplementedError


@then('i navigate to business page')
def i_navigate_to_business_page():
    """i navigate to business page."""
    raise NotImplementedError

