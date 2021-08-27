# coding=utf-8
"""Two HoH Client creation for cashflow"""
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

CASHFLOW_SYS_IE_02 = "https://planning.sys-ie-02.intelliflo.systems/dashboard/clients"


@pytest.mark.usefixtures("browser")
@scenario('../Features/AddTwoHoH.feature', 'Two HoH Client creation for cashflow')
def test_two_hoh_client_creation_for_cashflow():
    """Two HoH Client creation for cashflow."""


@given('user is on cashflow login page')
def user_is_on_cashflow_login_page(browser):
    """user is on cashflow login page."""
    browser.maximize_window()
    browser.get(CASHFLOW_SYS_IE_02)
    browser.implicitly_wait(20)


@when(parsers.cfparse('user enters email as "{Email_Address}" and password as "{Password}"'))
def user_enters_email_as_sureshpeddarapuintelliflocom_and_password_as_suresh2021(browser, Email_Address, Password):
    """user enters email as "suresh.peddarapu@intelliflo.com" and password as "Suresh@2021"."""
    browser.find_element_by_css_selector('#username').send_keys(Email_Address)
    browser.find_element_by_css_selector('#password').send_keys(Password)


@when('user clicks on login')
def user_clicks_on_login(browser):
    """user clicks on "login"."""
    browser.find_element_by_xpath("//button[@class='btn btn-primary']").click()
    time.sleep(5)


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


@then('I add First HoH name <Firstname>')
def i_add_first_hoh_name_firstname(browser, Firstname):
    """I add First HoH name <Firstname>."""
    browser.find_element_by_id("fullName").clear()
    browser.find_element_by_id("fullName").send_keys(Firstname)


@then('I add First HohH knowas <FirstknownAS>')
def i_add_first_hohh_knowas_firstknownas(browser, FirstknownAS):
    """I add First HohH knowas <FirstknownAS>."""
    browser.find_element_by_id("knownAs").clear()
    browser.find_element_by_id("knownAs").send_keys(FirstknownAS)


@then('I select First HoH Badge colour')
def i_select_first_hoh_badge_colour(browser):
    """I select First HoH Badge colour."""
    browser.find_element_by_xpath("(//*[@class='flex items-center'])[1]").click()
    browser.find_element_by_xpath(
        "//*[@class='rc-virtual-list-holder-inner']/child::div//div[contains(text(),'Red')]").click()


@then('I select First HoH DOB <FirstDoB>')
def i_select_first_hoh_dob_firstdob(browser, FirstDoB):
    """I select First HoH DOB <FirstDoB>."""
    browser.find_element_by_id("dateOfBirth").send_keys(FirstDoB)


@then('I select First HoH Tax Residency <FirstTaxResidency>')
def i_select_first_hoh_tax_residency_firsttaxresidency(browser, FirstTaxResidency):
    """I select First HoH Tax Residency <FirstTaxResidency>."""
    browser.find_element_by_xpath("//span[@title='England']").click()
    elements = browser.find_elements_by_xpath(
        "//*[@id='taxResidence_list']/following::div//*[@class='ant-select-item-option-content']")
    for element in elements:
        if FirstTaxResidency == element.text:
            element.click()
        else:
            print("no Tax residency found")


@then('I select First HoH Gender <FirstGender>')
def i_select_first_hoh_gender_firstgender(browser, FirstGender):
    """I select First HoH Gender <FirstGender>."""
    browser.find_element_by_id("gender").click()
    Genderlist = browser.find_elements_by_xpath("//*[@id='gender_list']/following::div[@aria-selected='false']")

    for list in Genderlist:
        element3 = list.get_attribute("title")
        if element3 == FirstGender:
            list.click()


@then('I click on Add partner/cohabitant button')
def i_click_on_add_partnercohabitant_button(browser):
    """I click on Add partner/cohabitant button."""
    browser.find_element_by_xpath("//span[text()= 'Add partner/cohabitant']").click()


@then('I add Second HoH name <Secondname>')
def i_add_second_hoh_name_secondname(browser, Secondname):
    """I add Second HoH name <Secondname>."""
    browser.find_element_by_id("fullName").clear()
    browser.find_element_by_id("fullName").send_keys(Secondname)


@then('I add Second HohH knowas <SecondknownAS>')
def i_add_second_hohh_knowas_secondknownas(browser, FirstknownAS):
    """I add Second HohH knowas <SecondknownAS>."""
    browser.find_element_by_id("knownAs").clear()
    browser.find_element_by_id("knownAs").send_keys(FirstknownAS)


@then('I select Second HoH Badge colour')
def i_select_second_hoh_badge_colour(browser):
    """I select Second HoH Badge colour."""
    browser.find_element_by_xpath("(//*[@class='flex items-center'])[1]").click()
    time.sleep(1)
    browser.find_element_by_xpath(
        "//*[@class='rc-virtual-list-holder-inner']/child::div//div[contains(text(),'Blue')]").click()


@then('I select Second HoH DOB <SecondDoB>')
def i_select_second_hoh_dob_seconddob(browser, FirstDoB):
    """I select Second HoH DOB <SecondDoB>."""
    browser.find_element_by_id("dateOfBirth").send_keys(FirstDoB)


@then('I select Second HoH Gender <SecondGender>')
def i_select_second_hoh_gender_secondgender(browser, SecondGender):
    """I select Second HoH Gender <SecondGender>."""
    browser.find_element_by_id("gender").click()
    Genderlist = browser.find_elements_by_xpath("//*[@id='gender_list']/following::div[@aria-selected='false']")

    for list in Genderlist:
        element3 = list.get_attribute("title")
        if element3 == SecondGender:
            list.click()


@then('I select relationship between two HoH <relation>')
def i_select_relationship_between_two_hoh_relation(browser, relation):
    """I select relationship between two HoH <relation>."""
    browser.find_element_by_id("relationship").click()
    Relationlist = browser.find_elements_by_xpath("//*[@id='relationship_list']/following::div[@aria-selected='false']")

    for list in Relationlist:
        element3 = list.get_attribute("title")
        if element3 == relation:
            list.click()


@then('I click on add person button')
def i_click_on_add_person_button(browser):
    """I click on add person button."""
    browser.find_element_by_xpath("//button/span[text()= 'Add Person']").click()


@then('I Provide case name for <ClientName>')
def i_provide_case_name_for_clientname(browser, ClientName):
    """I Provide case name for <ClientName>."""
    time.sleep(1)
    browser.find_element_by_id("caseName").send_keys(ClientName)


@then('I create client')
def i_create_client(browser):
    """I create client."""
    time.sleep(1)
    browser.find_element_by_xpath("//button/span[text()= 'Create Client']").click()


@then('I verify Client <ClientName>')
def i_verify_client_clientname(browser, ClientName):
    """I verify Client <ClientName>."""
    browser.find_element_by_xpath("//button//span[text()='Client Settings']").click()
    clientelement = browser.find_element_by_id("caseName")
    assert ClientName == clientelement.get_attribute("value")
    browser.find_element_by_xpath("//button[@aria-label='Close']").click()
    time.sleep(2)


@then('I logout from application')
def i_logout_from_application(browser):
    """I logout from application."""
    page_common = CommonFunctions(browser)
    page_common.DeleteClient()
    logout = CashflowLogin(browser)
    logout.logoutfromClientpage()
