# coding=utf-8
"""Two Head of households login feature tests."""
import time

import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when, parsers,
)

from Pages.Common import CommonFunctions
from Pages.Login_cashflow import CashflowLogin
from Pages.Properties import Properties


@pytest.mark.usefixtures("browser")
@scenario('../features/Property_2HoH.feature', 'Verify the add property with switches enabled and exclude property in scenario with all switches enabled')
def test_verify_two_hoh_login_feature():
    """Verify Two HOH login feature."""


@when('User is on Login page and Login as <Username> <Password>')
def user_is_on_login_page_and_login_as_username_password(browser, Username, Password):
    """User is on Login page and Login as <Username> <Password>."""
    page_login = CashflowLogin(browser)
    page_login.CallUserLogin(Username, Password)

@when('User successfully logged into application')
def user_successfully_logged_into_application(browser):
    """User successfully logged into application."""
    page_login = CashflowLogin(browser)
    page_login.VerifyUserLogingsuccessful()

@then('User Create client with single HeadofHousehold as <HoHName> <HoHKnowas> <DoB> <TaxResidency> <Gender>')
def user_create_client_with_single_headofhousehold_as_hohname_hohknowas_dob_taxresidency_gender(browser, HoHName, HoHKnowas, DoB, TaxResidency, Gender):
    """User Create client with single HeadofHousehold as <HoHName> <HoHKnowas> <DoB> <TaxResidency> <Gender>."""
    page_login = CashflowLogin(browser)
    page_login.AddSingleHOHclient(HoHName, HoHKnowas, DoB, TaxResidency, Gender)


@then('User Provide the Client Name as <ClientName>')
def user_provide_the_client_name_as_clientname(browser, ClientName):
    """User Provide the Client Name as <ClientName>."""
    page_login = CashflowLogin(browser)
    page_login.ClientName(ClientName)
    page_common = CommonFunctions(browser)
    page_common.DeleteClient()


@then('User Add second HoH details as <HohName_2> <HoHKnowas_2> <DoB_2> <relation> <SecondGender>')
def user_add_second_hoh_details_as_hohname_2_hohknowas_2_dob_2_relation_secondgender(browser, HohName_2, HoHKnowas_2, DoB_2, SecondGender, relation):
    """User Add second HoH details as <HohName_2> <HoHKnowas_2> <DoB_2> <relation> <SecondGender>."""
    page_login = CashflowLogin(browser)
    page_login.AddSecondHoH(HohName_2, HoHKnowas_2, DoB_2, SecondGender, relation)


@then('I Add Property <PropertyDescription>')
def i_add_property_propertydescription(browser):
    """I Add Property <PropertyDescription>."""
    pages_properties = Properties(browser)
    pages_properties.i_add_property_plan_from_property_page()


@then('I Enable Rental with <Rental>, <RentalExpense>')
def i_enable_rental_with_rental_rentalexpense():
    """I Enable Rental with <Rental>, <RentalExpense>."""
    raise NotImplementedError


@then('I Provide Property Value as <CurrentValue>')
def i_provide_property_value_as_currentvalue():
    """I Provide Property Value as <CurrentValue>."""
    raise NotImplementedError


@then('I add property from property page')
def i_add_property_from_property_page():
    """I add property from property page."""
    raise NotImplementedError


@then('I create new scenario <ScenarioName> <ScenarioDescription>')
def i_create_new_scenario_scenarioname_scenariodescription():
    """I create new scenario <ScenarioName> <ScenarioDescription>."""
    raise NotImplementedError


@then('I enable Mortgages with <MortagageDescription>, <ReplaymentType>, <MortagageValue>, <InterestRate>, <MortgageStartEvent>, <MortgageCeaseEvent>')
def i_enable_mortgages_with_mortagagedescription_replaymenttype_mortagagevalue_interestrate_mortgagestartevent_mortgageceaseevent():
    """I enable Mortgages with <MortagageDescription>, <ReplaymentType>, <MortagageValue>, <InterestRate>, <MortgageStartEvent>, <MortgageCeaseEvent>."""
    raise NotImplementedError


@then('I enable Renovation with <RenovationCost>, <IncreasedtoPropertyValue> <RenovationEvent>')
def i_enable_renovation_with_renovationcost_increasedtopropertyvalue_renovationevent():
    """I enable Renovation with <RenovationCost>, <IncreasedtoPropertyValue> <RenovationEvent>."""
    raise NotImplementedError


@then('I enable Sale Event with sale event as forever with Sale Expense % <SaleExpense>')
def i_enable_sale_event_with_sale_event_as_forever_with_sale_expense__saleexpense():
    """I enable Sale Event with sale event as forever with Sale Expense % <SaleExpense>."""
    raise NotImplementedError


@then('I exclude property with all switches ON')
def i_exclude_property_with_all_switches_on():
    """I exclude property with all switches ON."""
    raise NotImplementedError


@then('I logout from application')
def i_logout_from_application():
    """I logout from application."""
    raise NotImplementedError


@then('I navigate to property page')
def i_navigate_to_property_page():
    """I navigate to property page."""
    raise NotImplementedError


@then('I navigate to the recently added Property details')
def i_navigate_to_the_recently_added_property_details():
    """I navigate to the recently added Property details."""
    raise NotImplementedError


@then('I provide <PropertyDescription>')
def i_provide_propertydescription():
    """I provide <PropertyDescription>."""
    raise NotImplementedError


@then('I provide property details as <PreExisting>')
def i_provide_property_details_as_preexisting():
    """I provide property details as <PreExisting>."""
    raise NotImplementedError


@then('I provide the base cost for CGT as <BaseCostCGT>')
def i_provide_the_base_cost_for_cgt_as_basecostcgt():
    """I provide the base cost for CGT as <BaseCostCGT>."""
    raise NotImplementedError


@then('I save Property <PropertyDescription>')
def i_save_property_propertydescription():
    """I save Property <PropertyDescription>."""
    raise NotImplementedError


@then('I verify the scenario is excluded')
def i_verify_the_scenario_is_excluded():
    """I verify the scenario is excluded."""
    raise NotImplementedError


@then('User Add second HoH details as <HohName_2> <HoHKnowas_2> <DoB_2> <relation> <SecondGender>')
def user_add_second_hoh_details_as_hohname_2_hohknowas_2_dob_2_relation_secondgender():
    """User Add second HoH details as <HohName_2> <HoHKnowas_2> <DoB_2> <relation> <SecondGender>."""
    raise NotImplementedError


@then('User Create client with single HeadofHousehold as <HoHName> <HoHKnowas> <DoB> <TaxResidency> <Gender>')
def user_create_client_with_single_headofhousehold_as_hohname_hohknowas_dob_taxresidency_gender():
    """User Create client with single HeadofHousehold as <HoHName> <HoHKnowas> <DoB> <TaxResidency> <Gender>."""
    raise NotImplementedError


@then('User Provide the Client Name as <ClientName>')
def user_provide_the_client_name_as_clientname():
    """User Provide the Client Name as <ClientName>."""
    raise NotImplementedError

