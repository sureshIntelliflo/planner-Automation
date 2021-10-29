# coding=utf-8
"""Exports comparing feature tests."""
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
from Pages.Income import Income
from Pages.Investment import investments
from Pages.Loans import Loans
from Pages.Login_cashflow import CashflowLogin
from Pages.Properties import Properties
from Pages.Protections import Protections
from Pages.Wizards import Wizards


@pytest.mark.usefixtures("browser")
@scenario('../features/CapacityofLoss_Wizard.feature', 'Verify the Capacity of Loss Wizard functionality from Wizards')
def test_verify_the_exports_scenario_comparing_functionality_from_plan_outputs():
    """Verify the exports scenario comparing functionality from plan outputs."""

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


@then('I logout from application')
def i_logout_from_application(browser):
    """I logout from application."""
    logout =  CashflowLogin(browser)
    logout.logoutfromClientpage()


@then('I add Income type <IncomeType>')
def i_add_income_type_incometype(browser,IncomeType):
    """I add Income type <IncomeType>."""
    page_income = Income(browser)
    page_income.AddIncomeType(IncomeType)

@then('I add income amount <IncomeAmount>')
def i_add_income_amount_incomeamount(browser, IncomeAmount):
    """I add income amount <IncomeAmount>."""
    page_income = Income(browser)
    page_income.AddIncomeAmount(IncomeAmount)


@then('I add income and verify added income <IncomeDescription>')
def i_add_income_and_verify_added_income_incomedescription(browser,IncomeDescription):
    """I add income and verify added income <IncomeDescription>."""
    page_income = Income(browser)
    page_income.Addincome(IncomeDescription)

@then('I add income current or future type <CurrentFutureIncome>')
def i_add_income_current_or_future_type_currentfutureincome(browser, CurrentFutureIncome):
    """I add income current or future type <CurrentFutureIncome>."""
    page_income = Income(browser)
    page_income.Current_Future_income(CurrentFutureIncome)


@then('I add income description <IncomeDescription>')
def i_add_income_description_incomedescription(browser, IncomeDescription):
    """I add income description <IncomeDescription>."""
    page_income = Income(browser)
    page_income.AddIncomeDescription(IncomeDescription)


@then('I add new income from income Page')
def i_add_new_income_from_income_page(browser):
    """I add new income from income Page."""
    page_income = Income(browser)
    page_income.AddNewIncome()


@then('I navigate to Income page')
def i_navigate_to_income_page(browser):
    """I navigate to Income page."""
    page_income = Income(browser)
    page_income.NavigatetoIncome()


@then('I Add Protections and Verify the Protections <ProtectionDescription>')
def i_add_protections_and_verify_the_protections_protectiondescription(browser, ProtectionDescription):
    """I Add Protections and Verify the Protections <ProtectionDescription>."""
    page_protection = Protections(browser)
    page_protection.AddProtections()
    page_protection.VerifyProtection(ProtectionDescription)



@then('I Add protection benefit <IncomeDescription> <DeathInServiceMultiplier>')
def i_add_protection_benefit_incomedescription_deathinservicemultiplier(browser, IncomeDescription, DeathInServiceMultiplier):
    """I Add protection benefit <IncomeDescription> <DeathInServiceMultiplier>."""
    page_protection = Protections(browser)
    page_protection.ProtectionBenefit(IncomeDescription, DeathInServiceMultiplier)

@then('I add new Protections <ProtectionDescription>')
def i_add_new_protections_protectiondescription(browser, ProtectionDescription):
    """I add new Protections <ProtectionDescription>."""
    page_protection = Protections(browser)
    page_protection.AddNewProtections(ProtectionDescription)

@then('I navigate to protections')
def i_navigate_to_protections(browser):
    """I navigate to protections."""
    page_protection = Protections(browser)
    page_protection.NavigatetoProtections()


@then('I select the Type of Protection <ProtectionsType>')
def i_select_the_type_of_protection_protectionstype(browser, ProtectionsType):
    """I select the Type of Protection <ProtectionsType>."""
    page_protection = Protections(browser)
    page_protection.SelectProtectionType(ProtectionsType)

@then('I create new scenario <ScenarioName> <ScenarioDescription>')
def i_create_new_scenario_scenarioname_scenariodescription(browser, ScenarioName, ScenarioDescription):
    """I create new scenario <scenarioname> <scenarioDescription>."""
    page_properties = Properties(browser)
    page_properties.createscenario(ScenarioName, ScenarioDescription)

@then('I run the Capacity of Loss Report with  <FinancialGoal> <Goaltype> <TargetYear> <MarketCrashPlan> <CrashYear> <UserDefinedMaxLoss>')
def i_run_the_capacity_of_loss_report_with__financialgoal_goaltype_targetyear_marketcrashplan_crashyear_userdefinedmaxloss(browser, FinancialGoal, Goaltype, TargetYear, MarketCrashPlan, CrashYear, UserDefinedMaxLoss):
    """I run the Capacity of Loss Report with  <FinancialGoal> <Goaltype> <TargetYear> <MarketCrashPlan> <CrashYear> <UserDefinedMaxLoss>."""
    page_wizards = Wizards(browser)
    page_wizards.NavigatetoWizards()
    page_wizards.FinancialGoal(FinancialGoal, Goaltype, TargetYear)
    page_wizards.CapacityofLoss(MarketCrashPlan, CrashYear, UserDefinedMaxLoss)
    page_wizards.RunWizards()

@then('I export the  wizards results')
def i_export_the__wizards_results(browser):
    """I export the  wizards results."""
    page_wizards = Wizards(browser)
    page_wizards.ExportWizards()
    page_common = CommonFunctions(browser)
    page_common.DeleteClient()

@then('I verify the wizards results')
def i_verify_the_wizards_results(browser):
    """I verify the wizards results."""
    page_wizards = Wizards(browser)
    page_wizards.VerifyCapacityofLossWizard()

@then('I logout from application')
def i_logout_from_application(browser):
    """I logout from application."""
    logout =  CashflowLogin(browser)
    logout.logoutfromClientpage()
