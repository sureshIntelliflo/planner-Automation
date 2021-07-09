import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from Pages.Login_cashflow import CashflowLogin
from Pages.Properties import Properties

@pytest.mark.usefixtures("browser")
@scenario('../features/PropertyScenario.feature', 'Scenario mode for property to exclude')
def test_scenario_mode_for_property_to_exclude():
    """Scenario mode for property to exclude."""

def Propertyscenariotest():
    """mortgage to property."""


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

@then('I navigate to the Property details <PropertyDescription>')
def i_navigate_to_the_property_details_propertydescription(browser, PropertyDescription):
    """I navigate to the Property details <PropertyDescription>."""
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

@then('I logout from application')
def i_logout_from_application(browser):
    """I logout from application."""
    Logout_app = CashflowLogin(browser)
    Logout_app.logout()