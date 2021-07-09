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


@pytest.mark.usefixtures("browser")
@scenario('../features/Investments.feature', 'Add investments and exclude in a scenario')
def test_add_investments_and_exclude_in_a_scenario():
    """Add investments and exclude in a scenario."""


@when('User in cashflow home page')
def user_in_cashflow_home_page(browser):
    """User in cashflow home page."""
    Investments = investments(browser)
    Investments.Verify_user_in_home_page()


@then('I navigate to investments page')
def i_add_investment_from_investments_page(browser):
    """I add investment from investments page."""
    Investments = investments(browser)
    Investments.NavigatetoInvestment()


@then('I add Investment Description <InvestmentDescription>')
def i_add_investment_description_investmentdescription(browser, InvestmentDescription):
    """I add Investment Description <InvestmentDescription>."""
    Investments = investments(browser)
    Investments.AddInvestments(InvestmentDescription)


@then('I add Investment to Baseline scenario <InvestmentDescription>')
def i_add_investment_to_baseline_scenario(browser, InvestmentDescription):
    """I add Investment to Baseline scenario."""
    Investments = investments(browser)
    Investments.Investmentadd(InvestmentDescription)


@then('I add investment returns as <AttitudetoRisk> <GrossReturn> <Interest> <Dividends> <Growth>')
def i_add_investment_returns_as_attitudetorisk_grossreturn_interest_dividends_growth(browser, AttitudetoRisk,
                                                                                     GrossReturn, Interest, Dividends,
                                                                                     Growth):
    """I add investment returns as <AttitudetoRisk> <GrossReturn> <Interest> <Dividends> <Growth>."""
    Investments = investments(browser)
    Investments.returns(AttitudetoRisk, GrossReturn, Interest, Dividends, Growth)


@then('I add investment value as <CurrentValue>')
def i_add_investment_value_as_currentvalue(browser, CurrentValue):
    """I add investment value as <CurrentValue>."""
    Investments = investments(browser)
    Investments.currentvalue(CurrentValue)


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


@then('I exclude from the Baseline scenario <InvestmentDescription>')
def i_exclude_from_the_baseline_scenario_investmentdescription(browser, InvestmentDescription):
    """I exclude from the Baseline scenario <InvestmentDescription>."""
    Investments = investments(browser)
    Investments.excludefrombaseline(InvestmentDescription)
    Investments.saveInvestment()


@then('I verify invesment is excluded from baseline scenario <InvestmentDescription>')
def i_verify_invesment_is_excluded_from_baseline_scenario(browser, InvestmentDescription):
    """I verify invesment is excluded from baseline scenario."""
    Investments = investments(browser)
    Investments.verifyinvestmentexclude(InvestmentDescription)


@then('I create new scenario <ScenarioName> <ScenarioDescription>')
def i_create_new_scenario_scenarioname_scenariodescription(browser, ScenarioName, ScenarioDescription):
    """I create new scenario <ScenarioName> <ScenarioDescription>."""
    Investments = investments(browser)
    Investments.createscenario(ScenarioName, ScenarioDescription)


@then('I make plan include in scenario <InvestmentDescription>')
def i_make_plan_include_in_scenario_investmentdescription(browser, InvestmentDescription):
    """I make plan include in scenario <InvestmentDescription>."""
    Investments = investments(browser)
    Investments.excludeplantoinclude(InvestmentDescription)


@then('I add contributions <contributionstype> <contributionamount>')
def i_add_contributions_contributionstype_contributionamount(browser, contributionstype, contributionamount):
    """I add contributions <contributionstype> <contributionamount>."""
    Investments = investments(browser)
    Investments.Investmentcontributions(contributionstype, contributionamount)


@then('I add withdrawals custom <WithdrawalAmount>')
def i_add_withdrawals_custom_withdrawalamount(browser, WithdrawalAmount):
    """I add withdrawals custom <WithdrawalAmount>."""
    Investments = investments(browser)
    Investments.withdrowls_custom(WithdrawalAmount)


@then('I add withdrawals sell whole investments')
def i_add_withdrawals_sell_whole_investments(browser):
    """I add withdrawals sell whole investments."""
    Investments = investments(browser)
    Investments.withdrawals_sell_whole_investment()


@then('I add specific charges')
def i_add_specific_charges(browser):
    """I add specific charges."""
    Investments = investments(browser)
    Investments.specificcharge()


@then('I enable death options')
def i_enable_death_options(browser):
    """I enable death options."""
    Investments = investments(browser)
    Investments.deathoptions()


@then('I save Investments')
def i_save_investments(browser):
    """I save Investments."""
    Investments = investments(browser)
    Investments.saveInvestment()

@then('I verify the investment in scenario <InvestmentDescription>')
def i_verify_the_investment_in_scenario(browser, InvestmentDescription):
    """I verify the investment in scenario."""
    Investments = investments(browser)
    Investments.verifyinvestmentinclude(InvestmentDescription)

@then('I logout from application')
def i_logout_from_application(browser):
    """I logout from application."""
    logout =  CashflowLogin(browser)
    logout.logout()