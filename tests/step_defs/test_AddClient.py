# coding=utf-8
"""features\AddClient.feature feature tests."""
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
@scenario('../features/AddClient.feature', 'Single HoH Client creation for cashflow')
def test_single_hoh_client_creation_for_cashflow():
    """Single HoH Client creation for cashflow."""


def test_login_to_cashflow_with_valid_credentials():
    """login to cashflow with valid credentials."""


@given('user is on cashflow login page')
def user_is_on_cashflow_login_page(browser):
    """user is on cashflow login page."""
    browser.get(CASHFLOW_SYS_IE_02)
    browser.implicitly_wait(10)


@when(parsers.cfparse('user enters email as "{Email_Address}" and password as "{Password}"'))
def user_enters_email_as_sureshpeddarapuintelliflocom_and_password_as_suresh2021(browser, Email_Address, Password):
    """user enters email as "suresh.peddarapu@intelliflo.com" and password as "Suresh@2021"."""
    browser.find_element_by_css_selector('#username').send_keys(Email_Address)
    browser.find_element_by_css_selector('#password').send_keys(Password)


@when('user clicks on login')
def user_clicks_on_login(browser):
    """user clicks on "login"."""
    browser.find_element_by_xpath("//button[@class='btn btn-primary']").click()
    time.sleep(1)


@when('user sees add client button perform click action')
def user_sees_add_client_button_perform_click_action(browser):
    """user sees add client button perform click action."""
    element = browser.find_element_by_xpath("// button[ @ title = 'Create a new client']")
    if element.is_enabled():
        element.click()


@then('User sees add create client page click on add first head of household button')
def user_sees_add_create_client_page_click_on_add_first_head_of_household_button(browser):
    """User click on add first head of household button."""
    createclient = browser.find_element_by_xpath("//form/child::span[text()='Create Client']")
    if createclient.is_displayed():
        print("Create client page is displaying")
        browser.find_element_by_xpath("//button//span[text()= 'Add first head of household']").click()



@then('I add HoH name <name>')
def i_add_hoh_name_name(browser, name):
    """I add HoH name <name>."""
    browser.find_element_by_id("fullName").clear()
    browser.find_element_by_id("fullName").send_keys(name)


@then('I add HohH knowas <knownAS>')
def i_add_hohh_knowas_knownas(browser, knownAS):
    """I add HohH knowas <knownAS>."""
    browser.find_element_by_id("knownAs").clear()
    browser.find_element_by_id("knownAs").send_keys(knownAS)




@then('I select HoH Badge colour')
def i_select_hoh_badge_colour_badge(browser):
    """I select HoH Badge colour <Badge>."""
    browser.find_element_by_xpath("(//*[@class='flex items-center'])[1]").click()
    browser.find_element_by_xpath("//*[@class='rc-virtual-list-holder-inner']/child::div//div[contains(text(),'Red')]").click()



@then('I select HoH DOB <DoB>')
def i_select_hoh_dob_dob(browser, DoB):
    """I select HoH DOB <DoB>."""
    browser.find_element_by_id("dateOfBirth").send_keys(DoB)



@then('I select HoH Tax Residency <TaxResidency>')
def i_select_hoh_tax_residency_taxresidency(browser, TaxResidency):
    """I select HoH Tax Residency <TaxResidency>."""
    browser.find_element_by_xpath("//span[@title='England']").click()
    elements = browser.find_elements_by_xpath("//*[@id='taxResidence_list']/following::div//*[@class='ant-select-item-option-content']")
    for element in elements:
        if TaxResidency == element.text:
            element.click()
        else:
            print("no Tax residency found")


@then('I select HoH Gender <Gender>')
def i_select_hoh_gender_gender(browser, Gender):
    """I select HoH Gender <Gender>."""
    browser.find_element_by_id("gender").click()
    Genderlist = browser.find_elements_by_xpath("//*[@id='gender_list']/following::div[@aria-selected='false']")

    for list in Genderlist:
        element3 = list.get_attribute("title")
        if element3 == Gender:
            list.click()


@then('I click on add person button')
def i_click_on_add_person_button(browser):
    """I click on add person button."""
    browser.find_element_by_xpath("//button/span[text()= 'Add Person']").click()




@then('I Provide case name for <ClientName>')
def i_provide_case_name_for_clientname(browser, ClientName):
    """I Provide case name for <ClientName>."""
    browser.find_element_by_id("caseName").send_keys(ClientName)


@then('I create client')
def i_create_client(browser):
    """I create client."""
    browser.find_element_by_xpath("//button/span[text()= 'Create Client']").click()


@then('I verify Client <ClientName>')
def i_verify_client_clientname(browser, ClientName):
    """I verify Client <ClientName>."""
    browser.find_element_by_xpath("//button//span[text()='Client Settings']").click()
    clientelement = browser.find_element_by_id("caseName")
    assert ClientName == clientelement.get_attribute("value")
    browser.find_element_by_xpath("//button[@aria-label='Close']").click()
    time.sleep(5)


@then('I logout from application')
def i_logout_from_application(browser):
    """I logout from application."""
    browser.find_element_by_xpath("//button[@class='ant-btn ant-btn-link HeaderLogo_logo__lmyp5 Button_plain__3UtWY']").click()
    browser.find_element_by_link_text("Logout").click()