# coding=utf-8
"""DC Annuity in Payment feature tests."""
import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from Pages.Common import CommonFunctions
from Pages.Login_cashflow import CashflowLogin
from Pages.Pensions import Pensions
from Pages.tables import Tables

@pytest.mark.usefixtures("browser")
@scenario('../features/DCAnnuityinPayment.feature', 'Verify the DC Annuity in payment pensions')
def test_verify_the_dc_annuity_in_payment_pensions():
    """Verify the DC Annuity in payment pensions."""


@when('I navigate to pensions')
def i_navigate_to_pensions(browser):
    """I navigate to pensions."""
    page_Pension = Pensions(browser)
    page_Pension.Navigatetopensions()


@when('User in cashflow home page')
def user_in_cashflow_home_page(browser):
    """User in cashflow home page."""
    page_Pension = Pensions(browser)
    page_Pension.verifyuserhomepage()

@then('I Add DC Pension and Verify the Pension <PensionDescription>')
def i_add_dc_pension_and_verify_the_pension_pensiondescription(browser, PensionDescription):
    """I Add DC Pension and Verify the Pension <PensionDescription>."""
    page_Pension = Pensions(browser)
    page_Pension.AddPension()
    page_Pension.VerifyPension(PensionDescription)
    page_tables = Tables(browser)
    page_tables.NavigatetoTables()
    page_common = CommonFunctions(browser)
    page_common.DeleteClient()

@then('I Add pensions from pensions page')
def i_add_pensions_from_pensions_page(browser):
    """I Add pensions from pensions page."""
    page_Pension = Pensions(browser)
    page_Pension.AddNewPensions()


@then('I add pension description <PensionDescription>')
def i_add_pension_description_pensiondescription(browser, PensionDescription):
    """I add pension description <PensionDescription>."""
    page_Pension = Pensions(browser)
    page_Pension.AddPensionDescription(PensionDescription)


@then('I enable the Inherited pension and select <InheritedpensionType>')
def i_enable_the_inherited_pension_and_select_inheritedpensiontype(browser, InheritedpensionType):
    """I enable the Inherited pension and select <InheritedpensionType>."""
    page_Pension = Pensions(browser)
    page_Pension.inheritedtax(InheritedpensionType)


@then('I enter pension fund value <Income_as_Amount> <Rate_of_Increase> <AnnuityCeaseEvent>')
def i_enter_pension_fund_value_income_as_amount_rate_of_increase_annuityceaseevent(browser, Income_as_Amount, Rate_of_Increase, AnnuityCeaseEvent):
    """I enter pension fund value <Income_as_Amount> <Rate_of_Increase> <AnnuityCeaseEvent>."""
    page_Pension = Pensions(browser)
    page_Pension.AnnuityFundValue(Income_as_Amount, Rate_of_Increase, AnnuityCeaseEvent)


@then('I select policy status <DCType>')
def i_select_policy_status_dctype(browser, DCType):
    """I select policy status <DCType>."""
    page_Pension = Pensions(browser)
    page_Pension.PolicyType(DCType)


@then('I select policy structure is Defined Contribution')
def i_select_policy_structure_is_defined_contribution(browser):
    """I select policy structure is Defined Contribution."""
    page_Pension = Pensions(browser)
    page_Pension.SelectDCpensions()


@then('I logout from application')
def i_logout_from_application(browser):
    """I logout from application."""
    logout =  CashflowLogin(browser)
    logout.logoutfromClientpage()