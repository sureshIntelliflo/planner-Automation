# coding=utf-8
"""Investment and Properties linking feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('features\InvestmentPropertyLinking.feature', 'Link investment to property in mortgage offset')
def test_link_investment_to_property_in_mortgage_offset():
    """Link investment to property in mortgage offset."""


@given('user logged into application with email as "spped_12499" and password as "Suresh@2021"')
def user_logged_into_application_with_email_as_spped_12499_and_password_as_suresh2021():
    """user logged into application with email as "spped_12499" and password as "Suresh@2021"."""
    raise NotImplementedError


@when('User in cashflow home page')
def user_in_cashflow_home_page():
    """User in cashflow home page."""
    raise NotImplementedError


@when('user logged in and I add client with details name as "Investment property linked", KnowAs "QA Automation", DOB "01/01/1990",Tax residency "England", gender as "Male" and Create client with case name as "AutomatedQA_InvestmentProperty"')
def user_logged_in_and_i_add_client_with_details_name_as_investment_property_linked_knowas_qa_automation_dob_01011990tax_residency_england_gender_as_male_and_create_client_with_case_name_as_automatedqa_investmentproperty():
    """user logged in and I add client with details name as "Investment property linked", KnowAs "QA Automation", DOB "01/01/1990",Tax residency "England", gender as "Male" and Create client with case name as "AutomatedQA_InvestmentProperty"."""
    raise NotImplementedError


@then('I Provide Property Value as <CurrentValue>')
def i_provide_property_value_as_currentvalue():
    """I Provide Property Value as <CurrentValue>."""
    raise NotImplementedError


@then('I add Investment Description <InvestmentDescription>')
def i_add_investment_description_investmentdescription():
    """I add Investment Description <InvestmentDescription>."""
    raise NotImplementedError


@then('I add Investment to Baseline scenario <InvestmentDescription>')
def i_add_investment_to_baseline_scenario_investmentdescription():
    """I add Investment to Baseline scenario <InvestmentDescription>."""
    raise NotImplementedError


@then('I add investment returns as <Returns>')
def i_add_investment_returns_as_returns():
    """I add investment returns as <Returns>."""
    raise NotImplementedError


@then('I add investment value as <CurrentValue>')
def i_add_investment_value_as_currentvalue():
    """I add investment value as <CurrentValue>."""
    raise NotImplementedError


@then('I add property with <PropertyDescription>')
def i_add_property_with_propertydescription():
    """I add property with <PropertyDescription>."""
    raise NotImplementedError


@then('I enable Mortgages with <MortagageDescription>, <ReplaymentType>, <MortagageValue>, <InterestRate>, <MortgageStartEvent>, <MortgageCeaseEvent>')
def i_enable_mortgages_with_mortagagedescription_replaymenttype_mortagagevalue_interestrate_mortgagestartevent_mortgageceaseevent():
    """I enable Mortgages with <MortagageDescription>, <ReplaymentType>, <MortagageValue>, <InterestRate>, <MortgageStartEvent>, <MortgageCeaseEvent>."""
    raise NotImplementedError


@then('I enable mortgage offset with Linked Current Account <InvestmentDescription> and Offset Options <OffsetOptions>')
def i_enable_mortgage_offset_with_linked_current_account_investmentdescription_and_offset_options_offsetoptions():
    """I enable mortgage offset with Linked Current Account <InvestmentDescription> and Offset Options <OffsetOptions>."""
    raise NotImplementedError


@then('I navigate to Property')
def i_navigate_to_property():
    """I navigate to Property."""
    raise NotImplementedError


@then('I navigate to investments page')
def i_navigate_to_investments_page():
    """I navigate to investments page."""
    raise NotImplementedError


@then('I navigate to tables')
def i_navigate_to_tables():
    """I navigate to tables."""
    raise NotImplementedError


@then('I provide property details as <PropertyTyep>')
def i_provide_property_details_as_propertytyep():
    """I provide property details as <PropertyTyep>."""
    raise NotImplementedError


@then('I provide the base cost for CGT as <BaseCostCGT>')
def i_provide_the_base_cost_for_cgt_as_basecostcgt():
    """I provide the base cost for CGT as <BaseCostCGT>."""
    raise NotImplementedError


@then('I select investment as Pre existing <Investment>')
def i_select_investment_as_pre_existing_investment():
    """I select investment as Pre existing <Investment>."""
    raise NotImplementedError


@then('i add investment type as <InvestmentType>')
def i_add_investment_type_as_investmenttype():
    """i add investment type as <InvestmentType>."""
    raise NotImplementedError


@then('i save Mortgage and Propery')
def i_save_mortgage_and_propery():
    """i save Mortgage and Propery."""
    raise NotImplementedError

