# coding=utf-8
"""Income and Protections Linking feature tests."""
import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from Pages.Common import CommonFunctions
from Pages.Income import Income
from Pages.Login_cashflow import CashflowLogin
from Pages.Pensions import Pensions
from Pages.Protections import Protections
from Pages.tables import Tables


@pytest.mark.usefixtures("browser")
@scenario('../features/IncomeProtectionsLInking.feature', 'Verify the income and Death in service Protections linking')
def test_verify_the_income_and_death_in_service_protections_linking():
    """Verify the income and Death in service Protections linking."""


@when('User in cashflow home page')
def user_in_cashflow_home_page(browser):
    """User in cashflow home page."""
    page_income = Income(browser)
    page_income.verifyuserhomepage()

@then('I Add pensions from pensions page')
def i_add_pensions_from_pensions_page(browser):
    """I Add pensions from pensions page."""
    page_Pension = Pensions(browser)
    page_Pension.AddNewPensions()


@then('I add Income type <IncomeType>')
def i_add_income_type_incometype(browser,IncomeType):
    """I add Income type <IncomeType>."""
    page_income = Income(browser)
    page_income.AddIncomeType(IncomeType)

@then('I add income amount <IncomeAmount>')
def i_add_income_amount_incomeamount(browser, IncomeAmount):
    """I add income amount <IncomeAmount>."""
    page_income = Income(browser)
    page_income.AddIncomeAmount(IncomeAmount)


@then('I add income and verify added income <IncomeDescription>')
def i_add_income_and_verify_added_income_incomedescription(browser,IncomeDescription):
    """I add income and verify added income <IncomeDescription>."""
    page_income = Income(browser)
    page_income.Addincome(IncomeDescription)

@then('I add income current or future type <CurrentFutureIncome>')
def i_add_income_current_or_future_type_currentfutureincome(browser, CurrentFutureIncome):
    """I add income current or future type <CurrentFutureIncome>."""
    page_income = Income(browser)
    page_income.Current_Future_income(CurrentFutureIncome)


@then('I add income description <IncomeDescription>')
def i_add_income_description_incomedescription(browser, IncomeDescription):
    """I add income description <IncomeDescription>."""
    page_income = Income(browser)
    page_income.AddIncomeDescription(IncomeDescription)


@then('I add new income from income Page')
def i_add_new_income_from_income_page(browser):
    """I add new income from income Page."""
    page_income = Income(browser)
    page_income.AddNewIncome()


@then('I navigate to Income page')
def i_navigate_to_income_page(browser):
    """I navigate to Income page."""
    page_income = Income(browser)
    page_income.NavigatetoIncome()


@then('I Add Protections and Verify the Protections <ProtectionDescription>')
def i_add_protections_and_verify_the_protections_protectiondescription(browser, ProtectionDescription):
    """I Add Protections and Verify the Protections <ProtectionDescription>."""
    page_protection = Protections(browser)
    page_protection.AddProtections()
    page_protection.VerifyProtection(ProtectionDescription)
    page_tables = Tables(browser)
    page_tables.NavigatetoTables()
    page_common = CommonFunctions(browser)
    page_common.DeleteClient()


@then('I Add protection benefit <IncomeDescription> <DeathInServiceMultiplier>')
def i_add_protection_benefit_incomedescription_deathinservicemultiplier(browser, IncomeDescription, DeathInServiceMultiplier):
    """I Add protection benefit <IncomeDescription> <DeathInServiceMultiplier>."""
    page_protection = Protections(browser)
    page_protection.ProtectionBenefit(IncomeDescription, DeathInServiceMultiplier)

@then('I add new Protections <ProtectionDescription>')
def i_add_new_protections_protectiondescription(browser, ProtectionDescription):
    """I add new Protections <ProtectionDescription>."""
    page_protection = Protections(browser)
    page_protection.AddNewProtections(ProtectionDescription)

@then('I navigate to protections')
def i_navigate_to_protections(browser):
    """I navigate to protections."""
    page_protection = Protections(browser)
    page_protection.NavigatetoProtections()


@then('I select the Type of Protection <ProtectionsType>')
def i_select_the_type_of_protection_protectionstype(browser, ProtectionsType):
    """I select the Type of Protection <ProtectionsType>."""
    page_protection = Protections(browser)
    page_protection.SelectProtectionType(ProtectionsType)

@then('I logout from application')
def i_logout_from_application(browser):
    """I logout from application."""
    logout =  CashflowLogin(browser)
    logout.logoutfromClientpage()