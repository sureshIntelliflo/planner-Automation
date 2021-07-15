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
@scenario('../features/InvestmentPropertyLinking.feature', 'Link investment to property in mortgage offset')
def test_add_investments_and_exclude_in_a_scenario():
    """Add investments and exclude in a scenario."""


@when('User in cashflow home page')
def user_in_cashflow_home_page(browser):
    """User in cashflow home page."""
    Investments = investments(browser)
    Investments.Verify_user_in_home_page()

@then('I navigate to investments page')
def i_navigate_to_investments_page(browser):
    """I navigate to investments page."""
    Investments = investments(browser)
    Investments.NavigatetoInvestment()

@then('I add Investment Description <InvestmentDescription>')
def i_add_investment_description_investmentdescription(browser, InvestmentDescription):
    """I add Investment Description <InvestmentDescription>."""
    Investments = investments(browser)
    Investments.AddInvestments(InvestmentDescription)

@then('i add investment type as <InvestmentType>')
def i_add_investment_type_as_investmenttype(browser, InvestmentType):
    """i add investment type as <InvestmentType>."""
    Investments = investments(browser)
    Investments.investmentType(InvestmentType)

@then('I select investment as Pre existing <Investment>')
def i_select_investment_as_pre_existing_investment(browser, Investment):
    """I select investment as Pre existing <Investment>."""
    Investments = investments(browser)
    Investments.select_preexisting(Investment)


@then('I add investment value as <CurrentValue>')
def i_add_investment_value_as_currentvalue(browser, CurrentValue):
    """I add investment value as <CurrentValue>."""
    Investments = investments(browser)
    Investments.currentvalue(CurrentValue)

@then('I add investment returns as <Returns>')
def i_add_investment_returns_as_returns(browser, Returns):
    """I add investment returns as <Returns>."""
    Investments = investments(browser)
    Investments.investmentreturn(Returns)


@then('I add Investment to Baseline scenario <InvestmentDescription>')
def i_add_investment_to_baseline_scenario_investmentdescription(browser, InvestmentDescription):
    """I add Investment to Baseline scenario <InvestmentDescription>."""
    Investments = investments(browser)
    Investments.Investmentadd(InvestmentDescription)
    Investments.verifyInvestments(InvestmentDescription)

@then('I navigate to Property')
def i_navigate_to_property(browser):
    """I navigate to Property."""
    propertypage = Properties(browser)
    propertypage.i_add_property_plan_from_property_page()

@then('I add property with <PropertyDescription>')
def i_add_property_with_propertydescription(browser, PropertyDescription):
    """I add property with <PropertyDescription>."""
    propertypage = Properties(browser)
    propertypage.i_provide_propertydescription(PropertyDescription)


@then('I Provide Property Value as <CurrentValue>')
def i_provide_property_value_as_currentvalue(browser, CurrentValue):
    """I Provide Property Value as <CurrentValue>."""
    propertypage = Properties(browser)
    propertypage.currentvalue(CurrentValue)

@then('I enable Mortgages with <MortagageDescription>, <ReplaymentType>, <MortagageValue>, <InterestRate>, <MortgageStartEvent>, <MortgageCeaseEvent>')
def i_enable_mortgages_with_mortagagedescription_replaymenttype_mortagagevalue_interestrate_mortgagestartevent_mortgageceaseevent(browser, MortagageDescription, ReplaymentType, MortagageValue, InterestRate, MortgageStartEvent, MortgageCeaseEvent):
    """I enable Mortgages with <MortagageDescription>, <ReplaymentType>, <MortagageValue>, <InterestRate>, <MortgageStartEvent>, <MortgageCeaseEvent>."""
    pages_properties = Properties(browser)
    pages_properties.Mortgage_linking(MortagageDescription, ReplaymentType, MortagageValue, InterestRate, MortgageStartEvent, MortgageCeaseEvent)

@then('I enable mortgage offset with Linked Current Account <InvestmentDescription> and Offset Options <OffsetOptions>')
def i_enable_mortgage_offset_with_linked_current_account_investmentdescription_and_offset_options_offsetoptions(browser, InvestmentDescription, OffsetOptions):
    """I enable mortgage offset with Linked Current Account <InvestmentDescription> and Offset Options <OffsetOptions>."""
    pages_properties = Properties(browser)
    pages_properties.MortgageOffet(InvestmentDescription, OffsetOptions)


@then('I provide property details as <PropertyTyep>')
def i_provide_property_details_as_propertytyep(browser, PropertyTyep):
    """I provide property details as <PropertyTyep>."""
    pages_properties = Properties(browser)
    pages_properties.select_preexisting(PropertyTyep)


@then('I provide the base cost for CGT as <BaseCostCGT>')
def i_provide_the_base_cost_for_cgt_as_basecostcgt(browser, BaseCostCGT):
    """I provide the base cost for CGT as <BaseCostCGT>."""
    pages_properties = Properties(browser)
    pages_properties.basecostCGTvalue(BaseCostCGT)

@then('I logout from application')
def i_logout_from_application(browser):
    """I logout from application."""
    logout =  CashflowLogin(browser)
    logout.logout()

@then('i save Mortgage and Propery')
def i_save_mortgage_and_propery(browser, PropertyDescription):
    """i save Mortgage and Propery."""
    pages_properties = Properties(browser)
    pages_properties.AddMortgage()
    pages_properties.addpropery(PropertyDescription)

