# coding=utf-8
"""Two Head of households login feature tests."""
import time

import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when, parsers,
)

from Pages.Common import CommonFunctions
from Pages.FLA import FLA
from Pages.Investment import investments
from Pages.Login_cashflow import CashflowLogin
from Pages.Pensions import Pensions
from Pages.tables import Tables


@pytest.mark.usefixtures("browser")
@scenario('../features/OverideParentFLA_Add_Link_Delete_RiskProfile.feature',
          'Verify that Level 2 user Overrides the FLA and add risk profile and linking to Pensions Later delete Risk Profile and Unlock Plan with new Risk Profile')
def test_verify_that_level_2_user_overrides_the_fla_and_add_risk_profile_and_linking_to_pensions_later_delete_risk_profile_and_unlock_plan_with_new_risk_profile():
    """Verify that Level 2 user Overrides the FLA and add risk profile and linking to Pensions Later delete Risk Profile and Unlock Plan with new Risk Profile."""


@when('User is on Login page and Login as <Username> <Password>')
def user_is_on_login_page_and_login_as_username_password(browser,Username, Password):
    """User is on Login page and Login as <Username> <Password>."""
    page_login = CashflowLogin(browser)
    page_login.CallUserLogin(Username, Password)


@when('User successfully logged into application')
def user_successfully_logged_into_application(browser):
    """User successfully logged into application."""
    page_login = CashflowLogin(browser)
    page_login.VerifyUserLogingsuccessful()


@then('Delete Automation Client')
def delete_automation_client(browser):
    """Delete Automation Client."""
    page_common = CommonFunctions(browser)
    page_common.DeleteClient()


@then('Enable Override Parent Group Assumptions when level 2 user login')
def enable_override_parent_group_assumptions_when_level_2_user_login(browser):
    """Enable Override Parent Group Assumptions when level 2 user login."""
    page_fla = FLA(browser)
    page_fla.NavigatetoFLA()
    page_fla.GldAction()


@then('I Add DC Pension and Verify the Pension <PensionDescription>')
def i_add_dc_pension_and_verify_the_pension_pensiondescription(browser, PensionDescription):
    """I Add DC Pension and Verify the Pension <PensionDescription>."""
    page_Pension = Pensions(browser)
    page_Pension.AddPension()
    page_Pension.VerifyPension(PensionDescription)


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


@then('I enter pension fund value <TotalFundValue> <DrawdownValue> <OriginalCrystallisedAmount>')
def i_enter_pension_fund_value_totalfundvalue_drawdownvalue_originalcrystallisedamount(browser, TotalFundValue, DrawdownValue, OriginalCrystallisedAmount):
    """I enter pension fund value <TotalFundValue> <DrawdownValue> <OriginalCrystallisedAmount>."""
    page_Pension = Pensions(browser)
    page_Pension.DCPensionFund(TotalFundValue, DrawdownValue, OriginalCrystallisedAmount)


@then('I logout from application')
def i_logout_from_application(browser):
    """I logout from application."""

    logout = CashflowLogin(browser)
    logout.logoutfromClientpage()


@then('I navigate to pensions')
def i_navigate_to_pensions(browser):
    """I navigate to pensions."""
    page_Pension = Pensions(browser)
    page_Pension.Navigatetopensions()


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


@then('I select returns <RiskProfileName> <GrossReturn>')
def i_select_returns_riskprofilename_grossreturn(browser, RiskProfileName, GrossReturn):
    """I select returns <RiskProfileName> <GrossReturn>."""
    page_Pension = Pensions(browser)
    page_Pension.Return(RiskProfileName, GrossReturn)


@then('Navigate to plan outputs and verify graphs loading')
def navigate_to_plan_outputs_and_verify_graphs_loading(browser):
    """Navigate to plan outputs and verify graphs loading."""

    page_tables = Tables(browser)
    page_tables.NavigatetoTables()




@then('Unlock the client plan once user get client locked screen using new Risk profile from list <NewRiskProfile>')
def unlock_the_client_plan_once_user_get_client_locked_screen_using_new_risk_profile_from_list_newriskprofile(browser, NewRiskProfile):
    """Unlock the client plan once user get client locked screen using new Risk profile from list <NewRiskProfile>."""
    page_fla = FLA(browser)
    page_fla.UnlockPlan(NewRiskProfile)


@then(
    'User Add new risk profile <RiskProfileName> <GrossReturn> <Interest> <Dividends> <Growth> <Fund_Platform> <FinancialPlanning>')
def user_add_new_risk_profile_riskprofilename_grossreturn_interest_dividends_growth_fund_platform_financialplanning(browser, RiskProfileName, GrossReturn, Interest, Dividends, Growth, Fund_Platform, FinancialPlanning):
    """User Add new risk profile <RiskProfileName> <GrossReturn> <Interest> <Dividends> <Growth> <Fund_Platform> <FinancialPlanning>."""
    page_fla = FLA(browser)
    page_fla.DeleteRiskprofile_ifdisplayed(RiskProfileName)
    page_fla.AddRiskProfile(RiskProfileName, GrossReturn, Interest, Dividends, Growth, Fund_Platform, FinancialPlanning)
    page_fla.navigatetoClientpage()


@then('User Create client with single HeadofHousehold as <HoHName> <HoHKnowas> <DoB> <TaxResidency> <Gender>')
def user_create_client_with_single_headofhousehold_as_hohname_hohknowas_dob_taxresidency_gender(browser, HoHName, HoHKnowas, DoB, TaxResidency, Gender):
    """User Create client with single HeadofHousehold as <HoHName> <HoHKnowas> <DoB> <TaxResidency> <Gender>."""
    page_login = CashflowLogin(browser)
    page_login.AddSingleHOHclient(HoHName, HoHKnowas, DoB, TaxResidency, Gender)


@then('User Navigate to FLA page')
def user_navigate_to_fla_page(browser):
    """User Navigate to FLA page."""
    page_common = CommonFunctions(browser)
    page_common.NavigatetoClientsPage()
    page_fla = FLA(browser)
    page_fla.NavigatetoFLA()


@then('User Navigate to client list and Search for Recent Client <ClientName>')
def user_navigate_to_client_list_and_search_for_recent_client_clientname(browser, ClientName):
    """User Navigate to client list and Search for Recent Client <ClientName>."""
    page_fla = FLA(browser)
    page_fla.navigatetoClientpage()
    page_commons = CommonFunctions(browser)
    page_commons.clientSerach(ClientName)


@then('User Provide the Client Name as <ClientName>')
def user_provide_the_client_name_as_clientname(browser, ClientName):
    """User Provide the Client Name as <ClientName>."""
    page_login = CashflowLogin(browser)
    page_login.ClientName(ClientName)


@then('User delete the Automation Risk Profile <RiskProfileName>')
def user_delete_the_automation_risk_profile_name(browser, RiskProfileName):
    """User delete the Automation Risk Profile <Name>."""
    page_fla = FLA(browser)
    page_fla.DeleteRiskprofile_ifdisplayed(RiskProfileName)
