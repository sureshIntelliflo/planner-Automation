# coding=utf-8
"""Income and DC pensions feature tests."""
import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from Pages.Income import Income
from Pages.Pensions import Pensions


@pytest.mark.usefixtures("browser")
@scenario('../features/IncomeDCPension.feature', 'Verify the DC Pension and Income linking')
def test_verify_the_income_and_dC_pesnions_linking():
    """Verify the income and DC pesnions Linking."""

@when('User in cashflow home page')
def user_in_cashflow_home_page(browser):
    """User in cashflow home page."""
    page_income = Income(browser)
    page_income.verifyuserhomepage()


@then('I Add pensions from pensions page')
def i_add_pensions_from_pensions_page(browser):
    """I Add pensions from pensions page."""
    page_Pension = Pensions(browser)
    page_Pension.AddNewPensions()


@then('I add Income type <IncomeType>')
def i_add_income_type_incometype(browser, IncomeType):
    """I add Income type <IncomeType>."""
    page_income = Income(browser)
    page_income.AddIncomeType(IncomeType)


@then('I add income amount <IncomeAmount>')
def i_add_income_amount_incomeamount(browser, IncomeAmount):
    """I add income amount <IncomeAmount>."""
    page_income = Income(browser)
    page_income.AddIncomeAmount(IncomeAmount)


@then('I add income and verify added income <IncomeDescription>')
def i_add_income_and_verify_added_income_incomedescription(browser, IncomeDescription):
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


@then('I navigate to pensions')
def i_navigate_to_pensions(browser):
    """I navigate to pensions."""
    page_Pension = Pensions(browser)
    page_Pension.Navigatetopensions()


@then('I add pension description <PensionDescription>')
def i_add_pension_description_pensiondescription(browser, PensionDescription):
    """I add pension description <PensionDescription>."""
    page_Pension = Pensions(browser)
    page_Pension.AddPensionDescription(PensionDescription)

@then('I select policy structure is Defined Contribution')
def i_select_policy_structure_is_defined_contribution(browser):
    """I select policy structure is Defined Contribution."""
    page_Pension = Pensions(browser)
    page_Pension.SelectDCpensions()


@then('I enter pension fund value <TotalFundValue> <DrawdownValue> <OriginalCrystallisedAmount>')
def i_enter_pension_fund_value_totalfundvalue_drawdownvalue_originalcrystallisedamount(browser, TotalFundValue, DrawdownValue, OriginalCrystallisedAmount):
    """I enter pension fund value <TotalFundValue> <DrawdownValue> <OriginalCrystallisedAmount>."""
    page_Pension = Pensions(browser)
    page_Pension.DCPensionFund(TotalFundValue, DrawdownValue, OriginalCrystallisedAmount)

@then('I select policy status <DCType>')
def i_select_policy_status_dctype(browser, DCType):
    """I select policy status <DCType>."""
    page_Pension = Pensions(browser)
    page_Pension.PolicyType(DCType)

@then('I select returns <Risk> <GrossReturn>')
def i_select_returns_risk_grossreturn(browser, Risk, GrossReturn):
    """I select returns <Risk> <GrossReturn>."""
    page_Pension = Pensions(browser)
    page_Pension.Return(Risk, GrossReturn)
