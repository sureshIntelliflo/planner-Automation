# coding=utf-8
"""Verify the Property feature tests."""
import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from Pages.Common import CommonFunctions
from Pages.Login_cashflow import CashflowLogin
from Pages.Properties import Properties
from Pages.tables import Tables


@pytest.mark.usefixtures("browser")
@scenario('../features/Property.feature', 'Verify the add property with switches enabled and exclude property in scenario with all switches enabled')
def test_verify_the_add_property_with_switches_enabled_and_exclude_property_in_scenario_with_all_switches_enabled():
    """Verify the add property with switches enabled and exclude property in scenario with all switches enabled."""

@when('User in cashflow home page')
def user_in_cashflow_home_page(browser):
    """User in cashflow home page."""
    pages_properties = Properties(browser)
    pages_properties.Verify_user_in_home_page()

@then('I add property from property page')
def i_add_property_from_property_page(browser):
    """I add property from property page."""
    pages_properties = Properties(browser)
    pages_properties.NavigatetoPropertyPage()

@then('I provide <PropertyDescription>')
def i_provide_propertydescription(browser, PropertyDescription):
    """I provide <PropertyDescription>."""
    pages_properties = Properties(browser)
    pages_properties.i_provide_propertydescription(PropertyDescription)

@then('I provide property details as <PreExisting>')
def i_provide_property_details_as_preexisting(browser, PreExisting):
    """I provide property details as <PreExisting>."""
    pages_properties = Properties(browser)
    pages_properties.select_preexisting(PreExisting)

@then('I Provide Property Value as <CurrentValue>')
def i_provide_property_value_as_currentvalue(browser, CurrentValue):
    """I Provide Property Value as <CurrentValue>."""
    pages_properties = Properties(browser)
    pages_properties.PropertyValue(CurrentValue)

@then('I provide the base cost for CGT as <BaseCostCGT>')
def i_provide_the_base_cost_for_cgt_as_basecostcgt(browser, BaseCostCGT):
    """I provide the base cost for CGT as <BaseCostCGT>."""
    pages_properties = Properties(browser)
    pages_properties.basecostCGTvalue(BaseCostCGT)

@then('I enable Sale Event with sale event as forever with Sale Expense % <SaleExpense>')
def i_enable_sale_event_with_sale_event_as_retire_with_sale_expense__saleexpense(browser, SaleExpense):
    """I enable Sale Event with sale event as <Retire> with Sale Expense % <SaleExpense%>."""
    pages_properties = Properties(browser)
    pages_properties.Saleevent(SaleExpense)


@then('I Enable Rental with <Rental>, <RentalExpense>')
def i_enable_rental_with_rental_rentalexpense(browser, Rental,RentalExpense):
    """I Enable Rental with <Rental>, <RentalExpense>."""
    pages_properties = Properties(browser)
    pages_properties.rental(Rental, RentalExpense)


@then('I enable Mortgages with <MortagageDescription>, <ReplaymentType>, <MortagageValue>, <InterestRate>, <MortgageStartEvent>, <MortgageCeaseEvent>')
def i_enable_mortgages_with_mortagagedescription_replaymenttype_mortagagevalue_interestrate_mortgagestartevent_mortgageceaseevent(browser, MortagageDescription, ReplaymentType, MortagageValue, InterestRate, MortgageStartEvent, MortgageCeaseEvent):
    """I enable Mortgages with <MortagageDescription>, <ReplaymentType>, <MortagageValue>, <InterestRate>, <MortgageStartEvent>, <MortgageCeaseEvent>."""
    pages_properties = Properties(browser)
    pages_properties.mortage(MortagageDescription, ReplaymentType, MortagageValue, InterestRate, MortgageStartEvent, MortgageCeaseEvent)


@then('I enable Renovation with <RenovationCost>, <IncreasedtoPropertyValue> <RenovationEvent>')
def i_enable_renovation_with_renovationcost_increasedtopropertyvalue(browser, RenovationCost, IncreasedtoPropertyValue, RenovationEvent):
    """I enable Renovation with <RenovationCost>, <IncreasedtoPropertyValue>."""
    pages_properties = Properties(browser)
    pages_properties.renovation(RenovationCost, IncreasedtoPropertyValue, RenovationEvent)



@then('I Add Property <PropertyDescription>')
def i_save_property(browser, PropertyDescription):
    """I save Property."""
    pages_properties = Properties(browser)
    pages_properties.addpropery(PropertyDescription)

@then('I logout from application')
def i_logout_from_application(browser):
    """I logout from application."""
    logout = CashflowLogin(browser)
    logout.logoutfromClientpage()


@when('user Search for existing client <Existingclient>')
def user_search_for_existing_client_existingclient(browser, Existingclient):
    """user Search for existing client <Existingclient>."""
    page_properties = Properties(browser)
    page_properties.searchclient(Existingclient)

@then('I navigate to property page')
def i_navigate_to_property_page(browser):
    """I navigate to property page."""
    page_properties = Properties(browser)
    page_properties.navigaetoPropertypage()

@then('I create new scenario <ScenarioName> <ScenarioDescription>')
def i_create_new_scenario_scenarioname_scenariodescription(browser, ScenarioName, ScenarioDescription):
    """I create new scenario <scenarioname> <scenarioDescription>."""
    page_properties = Properties(browser)
    page_properties.createscenario(ScenarioName, ScenarioDescription)

@then('I navigate to the recently added Property details <PropertyDescription>')
def i_navigate_to_the_recently_added_property_details(browser, PropertyDescription):
    """I navigate to the recently added Property details."""
    page_properties = Properties(browser)
    page_properties.navigatetonarrativedetails(PropertyDescription)

@then('I exclude property with all switches ON')
def i_exclude_property_with_all_switches_on(browser):
    """I exclude property with all switches ON."""
    page_properties = Properties(browser)
    page_properties.excludeplanwithallSwitchesON()

@then('I save Property <PropertyDescription>')
def i_save_property(browser, PropertyDescription):
    """I save Property."""
    pages_properties = Properties(browser)
    pages_properties.savepropery(PropertyDescription)

@then('I verify the scenario is excluded')
def i_verify_the_scenario_is_excluded(browser):
    """I verify the scenario is excluded."""
    page_properties = Properties(browser)
    page_properties.excludedscenario()
    page_tables = Tables(browser)
    page_tables.NavigatetoTables()
    page_common = CommonFunctions(browser)
    page_common.DeleteClient()
