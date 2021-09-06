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
CASHFLOW_SYS_IE_02 = "https://planning.sys-ie-02.intelliflo.systems/dashboard/clients"
@pytest.mark.usefixtures("browser")
@scenario('../Features/Login.feature', 'login to cashflow with valid credentials')
@scenario('../Features/Login.feature', 'User successful Logout from cashflow')


def test_login_to_cashflow_with_valid_credentials():
    """login to cashflow with valid credentials."""


@when(parsers.cfparse('user enters email as "{Email_Address}" and password as "{Password}"'))
def user_enters_email_as_sureshpeddarapuintelliflocom_and_password_as_suresh2021(browser, Email_Address, Password):
    """user enters email as "suresh.peddarapu@intelliflo.com" and password as "Suresh@2021"."""
    browser.find_element_by_css_selector('#username').send_keys(Email_Address)
    browser.find_element_by_css_selector('#password').send_keys(Password)


@when('user clicks on login')
def user_clicks_on_login(browser):
    """user clicks on "login"."""
    browser.find_element_by_xpath("//button[@class='btn btn-primary']").click()
    time.sleep(10)



@then(parsers.cfparse('user sees page title as "{pagetitle}"'))
def user_sees_page_title_as_intelliflo_planner(browser , pagetitle):
    """user sees page title as "intelliflo planner"."""
    assert pagetitle == browser.title


@then('user click on logout')
def user_click_on_logout(browser):
    """user click on logout."""
    browser.find_element_by_link_text("Logout").click()

@then(parsers.cfparse('User sees logout page title as "{SignedOut}"'))
def user_sees_logout_page(browser, SignedOut):
    """"User signed out from the application"""
    assert SignedOut == browser.title



@then(parsers.cfparse('User sees logout page title as "{Validation}"'))
def user_sees_logout_page_title_as_signed_out(browser, Validation):
    assert Validation == browser.find_element_by_xpath("//div[@cla  ss='alert alert-danger']").gettext()