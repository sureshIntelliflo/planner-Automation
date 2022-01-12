# coding=utf-8
"""Add new risk profile and link to plan feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('features\NewRiskProfile_linkInvestment.feature', 'Verify that Level 2 user Overrides the FLA and add risk profile and linking to investments')
def test_verify_that_level_2_user_overrides_the_fla_and_add_risk_profile_and_linking_to_investments():
    """Verify that Level 2 user Overrides the FLA and add risk profile and linking to investments."""


@given('user is on cashflow login page')
def user_is_on_cashflow_login_page():
    """user is on cashflow login page."""
    raise NotImplementedError


@when('User is on Login page and Login as <Username> <Password>')
def user_is_on_login_page_and_login_as_username_password():
    """User is on Login page and Login as <Username> <Password>."""
    raise NotImplementedError


@when('User successfully logged into application')
def user_successfully_logged_into_application():
    """User successfully logged into application."""
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




