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


@pytest.mark.usefixtures("browser")
@scenario('../features/TwoHoHLogin.feature', 'Verify Two HOH login feature')
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