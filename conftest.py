import datetime
import os
import time

import allure
import pytest
from allure_commons.types import AttachmentType
from pytest_bdd import given, parsers, when, then
from selenium import webdriver

from Pages.Login_cashflow import CashflowLogin

CASHFLOW_SYS_IE_02 = "https://planning.sys-ie-02.intelliflo.systems/"
CASHFLOW_SYS_IE_06 = "https://planning.sys-ie-06.intelliflo.systems/"
CASHFLOW_PROD = "https://planner.gb.intelliflo.net/login"

# Hooks
def pytest_bdd_step_error(step):
    print(f'Step Failed: {step}')


def pytest_addoption(parser):
    parser.addoption("-B", "--browsertype",
                     help="Browser type. Available values: chrome, firefox, edge, ie, saucelabs",
                     default="chrome")


def pytest_generate_tests(metafunc):
    if 'browsertype' in metafunc.fixturenames and metafunc.config.option.browsertype is not None:
        metafunc.parametrize("browsertype", [metafunc.config.option.browsertype])


@pytest.fixture
def browser(browsertype, request):
    """ Creates a webdriver browser instance """
    global browser
    if 'chrome' in browsertype:
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        prefs = {"profile.default_content_settings.popups": 0,
                 "download.default_directory":
                     r"C:\test-cashflow\Downloads\\",
                 "directory_upgrade": True}
        options.add_experimental_option("prefs", prefs)
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(20)
        failed_before = request.session.testsfailed
        yield browser
        if request.session.testsfailed != failed_before:
            test_name = request.node.name
            take_screenshot(browser, test_name)
            allure.attach(browser.get_screenshot_as_png(), test_name, attachment_type=AttachmentType.PNG)
        # yield browser
        browser.quit()
    elif 'firefox' in browsertype:
        options = webdriver.FirefoxOptions()
        options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
        browser = webdriver.Firefox(options=options, executable_path="C:/AutomationDrivers/geckodriver.exe")
        browser.maximize_window()
        browser.implicitly_wait(20)
        failed_before = request.session.testsfailed
        yield browser
        if request.session.testsfailed != failed_before:
            test_name = request.node.name
            take_screenshot(browser, test_name)
        browser.quit()
    elif 'ie' in browsertype:
        browser = webdriver.Ie()
        browser.maximize_window()
    elif 'edge' in browsertype:  # Edge is very slow and all steps will throw a timeout error.
        browser_instance = webdriver.Edge()
        browser_instance.maximize_window()


def take_screenshot(browser, test_name):
    # now = datetime.now()
    # dt_string = now.strftime("%b-%d-%Y")
    # time_string = now.strftime("%H-%M-%S")
    # parent_dir = "./"
    # path = os.path.join(parent_dir, dt_string)
    # os.makedirs(path, exist_ok=True)
    # screenshot_file_path = f"./ScreenshotsOnFailure/{dt_string}/{test_name}_{time_string}.png"
    # browser.save_screenshot(filename=screenshot_file_path)
    screenshots_dir = "ScreenshotsOnFailure/"
    screenshot_file_path = "{}/{}.png".format(screenshots_dir, test_name)
    browser.save_screenshot(
    screenshot_file_path
)


@given(parsers.cfparse('user logged into application with email as "{Email_Address}" and password as "{Password}"'))
def user_logged_into_application_with_email_as_spped_12501_and_password_as_suresh2021(browser, Email_Address, Password):
    """user logged into application with email as "spped_12501" and password as "Suresh@2021"."""
    """"Launching the application"""

    browser.maximize_window()
    browser.get(CASHFLOW_SYS_IE_06)
    browser.implicitly_wait(30)
    """Entering the user login details"""
    browser.find_element_by_css_selector('#username').send_keys(Email_Address)
    browser.find_element_by_css_selector('#password').send_keys(Password)
    browser.find_element_by_xpath("//button[@class='btn btn-primary']").click()
    time.sleep(3)


@when(parsers.cfparse('user logged in and I add client with details name as "{name}", KnowAs "{knownAS}", '
                      'DOB "{DoB}",Tax residency "{TaxResidency}", gender as "{Gender}" and Create client with case name as "{ClientName}"'))
def Add_client(browser, name, knownAS, DoB, TaxResidency, Gender, ClientName):
    """add client"."""
    element = browser.find_element_by_xpath("// button[ @ title = 'Create a new client']")
    if element.is_enabled():
        element.click()
    createclient = browser.find_element_by_xpath("//form/child::span[text()='Create Client']")
    if createclient.is_displayed():
        print("Create client page is displaying")
        browser.find_element_by_xpath("//button//span[text()= 'Add first head of household']").click()

    browser.find_element_by_id("fullName").clear()
    browser.find_element_by_id("fullName").send_keys(name)

    browser.find_element_by_id("knownAs").clear()
    browser.find_element_by_id("knownAs").send_keys(knownAS)

    browser.find_element_by_xpath("(//*[@class='flex items-center'])[1]").click()
    time.sleep(1)
    browser.find_element_by_xpath(
        "//*[@class='rc-virtual-list-holder-inner']/child::div//div[contains(text(),'Red')]").click()

    browser.find_element_by_id("dateOfBirth").send_keys(DoB)

    browser.find_element_by_xpath("//span[@title='England']").click()
    elements = browser.find_elements_by_xpath(
        "//*[@id='taxResidence_list']/following::div//*[@class='ant-select-item-option-content']")
    time.sleep(1)
    for element in elements:
        if TaxResidency == element.text:
            element.click()
            break
        else:
            print("no Tax residency found")
    browser.find_element_by_id("gender").click()
    Genderlist = browser.find_elements_by_xpath("//*[@id='gender_list']/following::div[@aria-selected='false']")

    for list in Genderlist:
        element3 = list.get_attribute("title")
        if element3 == Gender:
            list.click()
            break
    browser.find_element_by_xpath("//button/span[text()= 'Add Person']").click()

    browser.find_element_by_id("caseName").send_keys(ClientName)

    browser.find_element_by_xpath("//button/span[text()= 'Create Client']").click()
    time.sleep(3)
    browser.find_element_by_xpath("//button//span[text()='Client Settings']").click()
    clientelement = browser.find_element_by_id("caseName")
    assert ClientName == clientelement.get_attribute("value")
    browser.find_element_by_xpath("//button[@aria-label='Close']").click()
    time.sleep(1)


@given('user is on cashflow login page')
def user_is_on_cashflow_login_page(browser):
    """user is on cashflow login page."""
    browser.get(CASHFLOW_SYS_IE_06)
    browser.implicitly_wait(30)

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

@then('User Add second HoH details as <HohName_2> <HoHKnowas_2> <DoB_2> <relation> <SecondGender>')
def user_add_second_hoh_details_as_hohname_2_hohknowas_2_dob_2_relation_secondgender(browser, HohName_2, HoHKnowas_2, DoB_2, SecondGender, relation):
    """User Add second HoH details as <HohName_2> <HoHKnowas_2> <DoB_2> <relation> <SecondGender>."""
    page_login = CashflowLogin(browser)
    page_login.AddSecondHoH(HohName_2, HoHKnowas_2, DoB_2, SecondGender, relation)