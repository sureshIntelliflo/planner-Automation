# coding=utf-8
"""Login feature tests."""
import time

import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when, parsers,
)

from Pages.Login_cashflow import CashflowLogin


@pytest.mark.usefixtures("browser")
@scenario('../Features/Login.feature', 'login to cashflow with valid credentials')
@scenario('../Features/Login.feature', 'User successful Logout from cashflow')
def test_login_to_cashflow_with_valid_credentials():
    """login to cashflow with valid credentials."""


@when(parsers.cfparse('user enters email as "{Email_Address}" and password as "{Password}"'))
def user_enters_email_as_sureshpeddarapuintelliflocom_and_password_as_suresh2021(browser, Email_Address, Password):
    """user enters email as "suresh.peddarapu@intelliflo.com" and password as "Suresh@2021"."""
    page_login = CashflowLogin(browser)
    page_login.enter_email(Email_Address)
    page_login.enter_password(Password)


@when('user clicks on login')
def user_clicks_on_login(browser):
    """user clicks on "login"."""
    page_login = CashflowLogin(browser)
    page_login.click_login()


@then(parsers.cfparse('user sees page title as "{pagetitle}"'))
def user_sees_page_title_as_intelliflo_planner(browser, pagetitle):
    """user sees page title as "intelliflo planner"."""
    page_login = CashflowLogin(browser)
    page_login.VerifyLoginpage(pagetitle)


@then('user click on logout')
def user_click_on_logout(browser):
    """user click on logout."""
    page_logout = CashflowLogin(browser)
    page_logout.SimpleLogout()


@then(parsers.cfparse('User sees logout page title as "{SignedOut}"'))
def user_sees_logout_page(browser, SignedOut):
    """"User signed out from the application"""
    page_logout = CashflowLogin(browser)
    page_logout.VerifyValidation(SignedOut)


@then(parsers.cfparse('User sees logout page title as "{Validation}"'))
def user_sees_logout_page_title_as_signed_out(browser, Validation):
    page_logout = CashflowLogin(browser)
    page_logout.logoutVerification(Validation)
