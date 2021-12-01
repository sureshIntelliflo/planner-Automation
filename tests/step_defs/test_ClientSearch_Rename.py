# coding=utf-8
"""Features\ClientSearch_Rename.feature feature tests."""
import time

import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when, parsers,
)
from selenium.webdriver.common.keys import Keys

from Pages.Common import CommonFunctions
from Pages.Login_cashflow import CashflowLogin

CASHFLOW_SYS_IE_02 = "https://planning.sys-ie-02.intelliflo.systems/dashboard/clients"


@pytest.mark.usefixtures("browser")
@scenario('../Features/ClientSearch_Rename.feature', 'Search for existing client and Update Client')
def test_search_for_existing_client_and_update_client():
    """Search for existing client and Update Client."""

@then('Navigate to Clients page')
def navigate_to_clients_page(browser):
    """Navigate to Clients page."""
    commons_page = CommonFunctions(browser)
    commons_page.NavigatetoClientsPage()


@then('I change the client name to new name <NewClientName>')
def i_change_the_client_name_to_new_name_newclientname(browser, NewClientName):
    """I change the client name to new name <NewClientName>."""
    time.sleep(1)
    clientelement = browser.find_element_by_id("caseName")
    clientelement.send_keys(Keys.CONTROL)
    clientelement.send_keys(Keys.DOWN + "a")
    clientelement.send_keys(Keys.DELETE)
    clientelement.send_keys(NewClientName)

@then('I goto Client Settings')
def i_goto_client_settings(browser):
    """I goto Client Settings."""
    browser.find_element_by_xpath("//button//span[text()='Client Settings']").click()


@then('I logout from application')
def i_logout_from_application(browser):
    """I logout from application."""
    logout = CashflowLogin(browser)
    logout.logoutfromClientpage()

@then('I search for Client <Clientname>')
def i_search_for_client_clientname(browser, Clientname):
    """I search for Client <Clientname>."""
    browser.find_element_by_xpath(" //input[@placeholder='Search...' and @type='text']").send_keys(Clientname)
    browser.find_element_by_xpath("//button//span[@aria-label='search']").click()
    time.sleep(1)

@then('I select the Client from search results <Clientname>')
def i_select_the_client_from_search_results_clientname(browser, Clientname):
    """I select the Client from search results <Clientname>."""
    results = browser.find_elements_by_xpath("//*[@id='i4c-application-ui']//div[@class='my-5']//span[@class='block text-lg truncate']")
    for resultslist in results:
        if Clientname in resultslist.text:
            resultslist.click()
            break
    time.sleep(1)

@then('I update the client changes')
def i_update_the_client_changes(browser):
    """I update the client changes."""
    browser.find_element_by_xpath("//button//span[text()='Update Client']").click()
    browser.find_element_by_xpath("//button[@aria-label='Close']").click()

@then('I verify client name on Cashflow')
def i_verify_client_name_on_cashflow_newclientname(browser):
    """I verify client name on Cashflow <NewClientName>."""
    toastmessage = browser.find_element_by_xpath("//span[normalize-space()='Your changes have been saved']")
    if toastmessage.is_displayed():
        assert toastmessage.text == "Your changes have been saved"


@then('I delete the created Client')
def i_delete_the_created_client(browser):
    """I delete the created Client."""
    commons_page = CommonFunctions(browser)
    commons_page.DeleteClient()
