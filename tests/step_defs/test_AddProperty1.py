# coding=utf-8
"""Verify the Property feature tests."""
import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from selenium.webdriver import ActionChains

from Pages.Properties import Properties


@pytest.mark.usefixtures("browser")
@scenario('../features/AddProperty.feature', 'Adding property')
@scenario('../features/AddProperty.feature', 'Renovation to property')
@scenario('../features/AddProperty.feature', 'Rent to property')
@scenario('../features/AddProperty.feature', 'Sale event to property')
@scenario('../features/AddProperty.feature', 'User Login')
@scenario('../features/AddProperty.feature', 'mortgage to property')
def test_mortgage_to_property():
    """mortgage to property."""


@when('User in cashflow home page')
def user_in_cashflow_home_page(browser):
    """User in cashflow home page."""
    element = browser.find_element_by_xpath("//span[text()='Active Scenario']")
    if element.is_displayed():
        print("User is on home page")


@then('I add property from property page')
def i_add_property_from_property_page(browser):
    """I add property from property page."""
    pages_properties = Properties(browser)
    pages_properties.Navigate_to_properties_page()

@then('I provide <PropertyDescription>')
def i_provide_propertydescription(browser, PropertyDescription):
    """I provide <PropertyDescription>."""
    AddProperty =browser.find_element_by_xpath("//button//span[text()='Add Property']")
    if AddProperty.is_displayed():
        AddProperty.click()
    browser.find_element_by_id("name").send_keys(PropertyDescription)

@then('I provide property details as <PreExisting>')
def i_provide_property_details_as_preexisting(browser, PreExisting):
    """I provide property details as <PreExisting>."""
    propertydetails = browser.find_elements_by_xpath("//*[@id='isPreexisting']//input")
    for type in propertydetails:
        if type.text == PreExisting:
            type.click()


@then('I Enable Rental with <Rental>, <RentalExpense>')
def i_enable_rental_with_rental_rentalexpense():
    """I Enable Rental with <Rental>, <RentalExpense>."""
    raise NotImplementedError


@then('I Provide Property Value as <CurrentValue>')
def i_provide_property_value_as_currentvalue():
    """I Provide Property Value as <CurrentValue>."""
    raise NotImplementedError

@then('I check allnow mortage interest offset')
def i_check_allnow_mortage_interest_offset():
    """I check allnow mortage interest offset."""
    raise NotImplementedError


@then('I enable Mortgages with <MortagageDescription>, <ReplaymentType>, <MortagageValue>, <InterestRate>, <MortgageStartEvent>, <MortgageCeaseEvent>')
def i_enable_mortgages_with_mortagagedescription_replaymenttype_mortagagevalue_interestrate_mortgagestartevent_mortgageceaseevent():
    """I enable Mortgages with <MortagageDescription>, <ReplaymentType>, <MortagageValue>, <InterestRate>, <MortgageStartEvent>, <MortgageCeaseEvent>."""
    raise NotImplementedError


@then('I enable Renovation with <RenovationCost>, <IncreasedtoPropertyValue>')
def i_enable_renovation_with_renovationcost_increasedtopropertyvalue():
    """I enable Renovation with <RenovationCost>, <IncreasedtoPropertyValue>."""
    raise NotImplementedError


@then('I enable Sale Event with sale event as <Retire> with Sale Expense % <SaleExpense%>')
def i_enable_sale_event_with_sale_event_as_retire_with_sale_expense__saleexpense():
    """I enable Sale Event with sale event as <Retire> with Sale Expense % <SaleExpense%>."""
    raise NotImplementedError




@then('I provide the base cost for CGT as <BaseCostCGT>')
def i_provide_the_base_cost_for_cgt_as_basecostcgt():
    """I provide the base cost for CGT as <BaseCostCGT>."""
    raise NotImplementedError


@then('I save Property')
def i_save_property():
    """I save Property."""
    raise NotImplementedError


@then('I select Renovation event <RenovationEvent>')
def i_select_renovation_event_renovationevent():
    """I select Renovation event <RenovationEvent>."""
    raise NotImplementedError

