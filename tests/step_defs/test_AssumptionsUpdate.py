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

from Pages.Assumptions import Assumptions
from Pages.Common import CommonFunctions
from Pages.Login_cashflow import CashflowLogin
from Pages.tables import Tables


@pytest.mark.usefixtures("browser")
@scenario('../Features/AssumptionsUpdate.feature', 'Verify the Assumptions update and Verify assumptions')
def test_verify_the_assumptions_update_and_verify_assumptions():
    """Verify the Assumptions update and Verify assumptions."""


@then('I logout from application')
def i_logout_from_application(browser):
    """I logout from application."""
    logout = CashflowLogin(browser)
    logout.logoutfromClientpage()


@then('User Navigate to Assumptions page')
def user_navigate_to_assumptions_page(browser):
    """User Navigate to Assumptions page."""
    page_assumptions = Assumptions(browser)
    page_assumptions.NavigatetoAssumptions()
    page_assumptions.NavigatetoAssumptionsDetails()


@then('User Update property inflation <NewPropertyInflation>')
def user_update_property_inflation_newpropertyinflation(browser, NewPropertyInflation):
    """User Update property inflation <NewPropertyInflation>."""
    page_assumptions = Assumptions(browser)
    page_assumptions.Update_Property_Assumptions(NewPropertyInflation)


@then('User save assumptions')
def user_save_assumptions(browser):
    """User save assumptions."""
    page_assumptions = Assumptions(browser)
    page_assumptions.SaveAssumptions()

@then('User update Tax Residency <NewTaxResidency>')
def user_update_tax_residency_newtaxresidency(browser, NewTaxResidency):
    """User update Tax Residency <NewTaxResidency>."""
    page_assumptions = Assumptions(browser)
    page_assumptions.UpdateTaxTaxResidency(NewTaxResidency)

@then('Verify the Assumptions Narrative <NewPropertyInflation>')
def verify_the_assumptions_narrative_newpropertyinflation(browser, NewPropertyInflation):
    """Verify the Assumptions Narrative <NewPropertyInflation>."""
    page_assumptions = Assumptions(browser)
    page_assumptions.VerifyPropertyAssumption(NewPropertyInflation)
    page_tables = Tables(browser)
    page_tables.NavigatetoTables()
    page_common = CommonFunctions(browser)
    page_common.DeleteClient()


@then('user enable the Override Returns <FirstYearofOverride> <GrossReturn> <RepeatFrequency>')
def user_enable_the_override_returns_firstyearofoverride_grossreturn_repeatfrequency(browser, FirstYearofOverride, GrossReturn, RepeatFrequency):
    """user enable the Override Returns <FirstYearofOverride> <GrossReturn> <RepeatFrequency>."""
    page_assumptions = Assumptions(browser)
    page_assumptions.UpdateOverrideReturns(FirstYearofOverride, GrossReturn, RepeatFrequency)

