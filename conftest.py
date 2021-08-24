import time

import pytest
from pytest_bdd import given, parsers, when
from selenium import webdriver

CASHFLOW_SYS_IE_02 = "https://planning.sys-ie-02.intelliflo.systems/login"
CASHFLOW_SYS_IE_06 = "https://planning.sys-ie-06.intelliflo.systems/login"

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
        browser = webdriver.Chrome()
        browser.implicitly_wait(10)
        failed_before = request.session.testsfailed
        yield browser
        if request.session.testsfailed != failed_before:
            test_name = request.node.name
            take_screenshot(browser, test_name)
        # yield browser
        browser.quit()
    elif 'firefox' in browsertype:
        options = webdriver.FirefoxOptions()
        browser = webdriver.Firefox(firefox_options=options)
        browser.maximize_window()
        browser.implicitly_wait(10)
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
    browser.get(CASHFLOW_SYS_IE_02)
    browser.implicitly_wait(10)
    """Entering the user login details"""
    browser.find_element_by_css_selector('#username').send_keys(Email_Address)
    browser.find_element_by_css_selector('#password').send_keys(Password)
    browser.find_element_by_xpath("//button[@class='btn btn-primary']").click()

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

    browser.find_element_by_xpath("//button//span[text()='Client Settings']").click()
    clientelement = browser.find_element_by_id("caseName")
    assert ClientName == clientelement.get_attribute("value")
    browser.find_element_by_xpath("//button[@aria-label='Close']").click()
    time.sleep(1)

