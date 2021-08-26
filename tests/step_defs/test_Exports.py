# coding=utf-8
"""Exports feature tests."""
import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from Pages.Business import Business
from Pages.Common import CommonFunctions
from Pages.Expenses import Expenses
from Pages.Exports import Exports
from Pages.Investment import investments
from Pages.Loans import Loans
from Pages.Login_cashflow import CashflowLogin


@pytest.mark.usefixtures("browser")
@scenario('../features/Exports.feature', 'Verify the exports functionality from plan outputs')
def test_verify_the_exports_functionality_from_plan_outputs():
    """Verify the exports functionality from plan outputs."""

@when('User in cashflow home page')
def user_in_cashflow_home_page(browser):
    """User in cashflow home page."""
    Investments = investments(browser)
    Investments.Verify_user_in_home_page()

@then('I add Investment Description <InvestmentDescription>')
def i_add_investment_description_investmentdescription(browser, InvestmentDescription):
    """I add Investment Description <InvestmentDescription>."""
    Investments = investments(browser)
    Investments.AddInvestments(InvestmentDescription)

@then('I add Investment to Baseline scenario <InvestmentDescription>')
def i_add_investment_to_baseline_scenario_investmentdescription(browser, InvestmentDescription):
    """I add Investment to Baseline scenario <InvestmentDescription>."""
    Investments = investments(browser)
    Investments.Investmentadd(InvestmentDescription)

@then('I add investment returns as <AttitudetoRisk> <GrossReturn> <Interest> <Dividends> <Growth>')
def i_add_investment_returns_as_attitudetorisk_grossreturn_interest_dividends_growth(browser, AttitudetoRisk, GrossReturn, Interest, Dividends, Growth):
    """I add investment returns as <AttitudetoRisk> <GrossReturn> <Interest> <Dividends> <Growth>."""
    Investments = investments(browser)
    Investments.returns(AttitudetoRisk, GrossReturn, Interest, Dividends, Growth)

@then('I add investment value as <CurrentValue>')
def i_add_investment_value_as_currentvalue(browser, CurrentValue):
    """I add investment value as <CurrentValue>."""
    Investments = investments(browser)
    Investments.currentvalue(CurrentValue)

@then('I navigate to investments page')
def i_navigate_to_investments_page(browser):
    """I navigate to investments page."""
    Investments = investments(browser)
    Investments.NavigatetoInvestment()

@then('I select investment as Pre existing <Investment>')
def i_select_investment_as_pre_existing_investment(browser, Investment):
    """I select investment as Pre existing <Investment>."""
    Investments = investments(browser)
    Investments.select_preexisting(Investment)

@then('i add investment type as <InvestmentType>')
def i_add_investment_type_as_investmenttype(browser, InvestmentType):
    """i add investment type as <InvestmentType>."""
    Investments = investments(browser)
    Investments.investmentType(InvestmentType)

@then('i navigate to business page')
def i_navigate_to_business_page(browser):
    """i navigate to business page."""
    page_business = Business(browser)
    page_business.NavigatetoBusiness()

@then('I add Business Death options')
def i_add_business_death_options(browser):
    """I add Business Death options."""
    page_business = Business(browser)
    page_business.DeathOptions()

@then('I add Business sale event <SaleEvent>')
def i_add_business_sale_event_saleevent(browser, SaleEvent):
    """I add Business sale event <SaleEvent>."""
    page_business = Business(browser)
    page_business.BusinessSaleEvent(SaleEvent)

@then('I add business details <BusinessType> <BusinessValue> <AnnualIncreasepercentage> <BaseCostforCGT> <ValuationBasis>')
def i_add_business_details_businesstype_businessvalue_annualincreasepercentage_basecostforcgt_valuationbasis(browser, BusinessType, BusinessValue, AnnualIncreasepercentage, BaseCostforCGT, ValuationBasis):
    """I add business details <BusinessType> <BusinessValue> <AnnualIncreasepercentage> <BaseCostforCGT> <ValuationBasis>."""
    page_business = Business(browser)
    page_business.BusinessDetail(BusinessType, BusinessValue, AnnualIncreasepercentage, BaseCostforCGT, ValuationBasis)

@then('I add business dividends <DividendFrequency> <DividendAmount> <IncreasePerstart> <PeriodSetby>')
def i_add_business_dividends_dividendfrequency_periodsetby_startevent(browser, DividendFrequency, DividendAmount, IncreasePerstart, PeriodSetby):
    """I add business dividends <DividendFrequency> <PeriodSetby> <StartEvent>."""
    page_business = Business(browser)
    page_business.BusinessDividends(DividendFrequency, DividendAmount, IncreasePerstart, PeriodSetby)

@then('I add new business with <BusinessDescription>')
def i_add_new_business_with_businessdescription(browser, BusinessDescription):
    """I add new business with <BusinessDescription>."""
    page_business = Business(browser)
    page_business.AddNewBusiness(BusinessDescription)

@then('I save Business and verify <BusinessDescription>')
def i_save_business_and_verify_businessdescription(browser, BusinessDescription):
    """I save Business and verify <BusinessDescription>."""
    page_business = Business(browser)
    page_business.AddBusiness()
    page_business.VerifyBusiness(BusinessDescription)

@then('i navigate to business page')
def i_navigate_to_business_page(browser):
    """i navigate to business page."""
    page_business = Business(browser)
    page_business.NavigatetoBusiness()

@then('I add Loan details as <loantype> <OutstandingBalance> <InterestRate> <repaymentType>')
def i_add_loan_details_as_loantype_outstandingbalance_interestrate_repaymenttype(browser, loantype, OutstandingBalance, InterestRate, repaymentType):
    """I add Loan details as <loantype> <OutstandingBalance> <InterestRate> <repaymentType>."""
    page_loans = Loans(browser)
    page_loans.LoanDetails(loantype, OutstandingBalance, InterestRate, repaymentType)

@then('I add new loan with <LoanDescription>')
def i_add_new_loan_with_loandescription(browser, LoanDescription):
    """I add new loan with <LoanDescription>."""
    page_loans = Loans(browser)
    page_loans.AddnewLoan(LoanDescription)

@then('I navigate to Loan page')
def i_navigate_to_loan_page(browser):
    """I navigate to Loan page."""
    page_loans = Loans(browser)
    page_loans.NavigatetoBusiness()

@then('I save Loan and verify loan <LoanDescription>')
def i_save_loan_and_verify_loan_loandescription(browser, LoanDescription):
    """I save Loan and verify loan <LoanDescription>."""
    page_loans = Loans(browser)
    page_loans.addloan()
    page_loans.Verifyloan(LoanDescription)



@then('I add expense expenditure with details as <EssentialAmount> <DiscretionaryAmount>')
def i_add_expense_expenditure_with_details_as_essentialamount_discretionaryamount(browser, EssentialAmount, DiscretionaryAmount):
    """I add expense expenditure with details as <EssentialAmount> <DiscretionaryAmount>."""
    page_expenses = Expenses(browser)
    page_expenses.AddExpensesExpenditure(EssentialAmount, DiscretionaryAmount)

@then('I add expenses description as <ExpensesDescription>')
def i_add_expenses_description_as_expensesdescription(browser, ExpensesDescription):
    """I add expenses description as <ExpensesDescription>."""
    page_expenses = Expenses(browser)
    page_expenses.AddExpensesdescription(ExpensesDescription)

@then('I add new expenses with type as <ExpenseCategory>')
def i_add_new_expenses_with_type_as_expensecategory(browser, ExpenseCategory):
    """I add new expenses with type as <ExpenseCategory>."""
    page_expenses = Expenses(browser)
    page_expenses.AddnewExpense(ExpenseCategory)

@then('I navigate to Expense page')
def i_navigate_to_expense_page(browser):
    """I navigate to Expense page."""
    page_expenses = Expenses(browser)
    page_expenses.NavigatetoExpenses()

@then('I save expense and Verify the expense <ExpensesDescription>')
def i_save_expense_and_verify_the_expense_expensesdescription(browser, ExpensesDescription):
    """I save expense and Verify the expense <ExpensesDescription>."""
    page_expenses = Expenses(browser)
    page_expenses.SaveExpenses()
    page_expenses.VerifyExpenses(ExpensesDescription)


@then('I navigate to plan outputs and select Exports')
def i_navigate_to_plan_outputs_and_select_exports(browser):
    """I navigate to plan outputs and select Exports."""
    page_export = Exports(browser)
    page_export.NavigatetoExports()

@then('I download the exports with detault selections')
def i_download_the_exports_with_detault_selections(browser):
    """I download the exports with detault selections."""
    page_export = Exports(browser)
    page_export.Exportdownload()
    page_common = CommonFunctions(browser)
    page_common.DeleteClient()

@then('I logout from application')
def i_logout_from_application(browser):
    """I logout from application."""
    logout =  CashflowLogin(browser)
    logout.logoutfromClientpage()
