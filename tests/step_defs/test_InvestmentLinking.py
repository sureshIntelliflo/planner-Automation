# coding=utf-8
"""Add investments feature tests."""
import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from Pages.Investment import investments
from Pages.Login_cashflow import CashflowLogin
from Pages.Properties import Properties
from Pages.tables import Tables

@pytest.mark.usefixtures("browser")
@scenario('../features/InvestmentLinkingInvestment.feature', 'Verify the Unit trust and ISA stocks & shares linked investment is excluded')
def test_add_investments_and_exclude_in_a_scenario():
    """Add investments and exclude in a scenario."""

@when('User in cashflow home page')
def user_in_cashflow_home_page(browser):
    """User in cashflow home page."""
    pages_Investment = investments(browser)
    pages_Investment.Verify_user_in_home_page()


@then('I add Investment Description <InvestmentDescription1>')
def i_add_investment_description_investmentdescription1(browser, InvestmentDescription1):
    """I add Investment Description <InvestmentDescription1>."""
    pages_Investment = investments(browser)
    pages_Investment.AddInvestments(InvestmentDescription1)

@then('I navigate to investments page')
def i_navigate_to_investments_page(browser):
    """I navigate to investments page."""
    pages_Investment = investments(browser)
    pages_Investment.NavigatetoInvestment()


@then('I select investment as Pre existing <Investment1>')
def i_select_investment_as_pre_existing_investment1(browser, Investment1):
    """I select investment as Pre existing <Investment1>."""
    pages_Investment = investments(browser)
    pages_Investment.select_preexisting(Investment1)


@then('i add investment type as <InvestmentType1>')
def i_add_investment_type_as_investmenttype1(browser, InvestmentType1):
    """i add investment type as <InvestmentType1>."""
    pages_Investment = investments(browser)
    pages_Investment.investmentType(InvestmentType1)


@then('I add Investment to Baseline scenario <InvestmentDescription1>')
def i_add_investment_to_baseline_scenario_investmentdescription1(browser, InvestmentDescription1):
    """I add Investment to Baseline scenario <InvestmentDescription1>."""
    pages_Investment = investments(browser)
    pages_Investment.Investmentadd(InvestmentDescription1)
    pages_Investment.verifyInvestments(InvestmentDescription1)

@then('I add investment returns as <AttitudetoRisk1> <GrossReturn1> <Interest1> <Dividends1> <Growth1>')
def i_add_investment_returns_as_attitudetorisk1_grossreturn1_interest1_dividends1_growth1(browser, AttitudetoRisk1, GrossReturn1, Interest1, Dividends1, Growth1):
    """I add investment returns as <AttitudetoRisk1> <GrossReturn1> <Interest1> <Dividends1> <Growth1>."""
    pages_Investment = investments(browser)
    pages_Investment.returns(AttitudetoRisk1, GrossReturn1, Interest1, Dividends1, Growth1)

@then('I add investment value as <CurrentValue1>')
def i_add_investment_value_as_currentvalue1(browser, CurrentValue1):
    """I add investment value as <CurrentValue1>."""
    pages_Investment = investments(browser)
    pages_Investment.currentvalue(CurrentValue1)