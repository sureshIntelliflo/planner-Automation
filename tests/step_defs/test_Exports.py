# coding=utf-8
"""Add investments feature tests."""
import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from Pages.Business import Business
from Pages.Investment import investments
from Pages.Login_cashflow import CashflowLogin


@pytest.mark.usefixtures("browser")
@scenario('../features/Investments.feature', 'Add investments and exclude in a scenario')
def test_add_investments_and_exclude_in_a_scenario():
    """Add investments and exclude in a scenario."""


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
