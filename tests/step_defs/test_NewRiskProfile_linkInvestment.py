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
from Pages.tables import Tables


@pytest.mark.usefixtures("browser")
@scenario('../features/NewRiskProfile_linkInvestment.feature',
          'Verify that Level 2 user Overrides the FLA and add risk profile and linking to investments')
def test_verify_that_level_2_user_overrides_the_fla_and_add_risk_profile_and_linking_to_investments():
    """Verify that Level 2 user Overrides the FLA and add risk profile and linking to investments."""


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
def user_create_client_with_single_headofhousehold_as_hohname_hohknowas_dob_taxresidency_gender(browser, HoHName,
                                                                                                HoHKnowas, DoB,
                                                                                                TaxResidency, Gender):
    """User Create client with single HeadofHousehold as <HoHName> <HoHKnowas> <DoB> <TaxResidency> <Gender>."""
    page_login = CashflowLogin(browser)
    page_login.AddSingleHOHclient(HoHName, HoHKnowas, DoB, TaxResidency, Gender)


@then('User Provide the Client Name as <ClientName>')
def user_provide_the_client_name_as_clientname(browser, ClientName):
    """User Provide the Client Name as <ClientName>."""
    page_login = CashflowLogin(browser)
    page_login.ClientName(ClientName)


@then('User Add second HoH details as <HohName_2> <HoHKnowas_2> <DoB_2> <relation> <SecondGender>')
def user_add_second_hoh_details_as_hohname_2_hohknowas_2_dob_2_relation_secondgender(browser, HohName_2, HoHKnowas_2,
                                                                                     DoB_2, relation, SecondGender):
    """User Add second HoH details as <HohName_2> <HoHKnowas_2> <DoB_2> <relation> <SecondGender>."""
    page_login = CashflowLogin(browser)
    page_login.AddSecondHoH(HohName_2, HoHKnowas_2, DoB_2, relation, SecondGender)


@then('Enable Override Parent Group Assumptions when level 2 user login')
def enable_override_parent_group_assumptions_when_level_2_user_login(browser):
    """Enable Override Parent Group Assumptions when level 2 user login."""
    page_fla = FLA(browser)
    page_fla.NavigatetoFLA()
    page_fla.GldAction()


@then('I add Investment Description <InvestmentDescription>')
def i_add_investment_description_investmentdescription(browser, InvestmentDescription):
    """I add Investment Description <InvestmentDescription>."""
    Investments = investments(browser)
    Investments.AddInvestments(InvestmentDescription)


@then('I add Investment to Baseline scenario <InvestmentDescription>')
def i_add_investment_to_baseline_scenario_investmentdescription(browser, InvestmentDescription):
    """I add Investment to Baseline scenario <InvestmentDescription>."""
    Investments = investments(browser)
    Investments.Investmentadd(InvestmentDescription)


@then('I add investment returns as <AttitudetoRisk>')
def i_add_investment_returns_as_attitudetorisk(browser, AttitudetoRisk):
    """I add investment returns as <AttitudetoRisk>."""
    Investments = investments(browser)
    Investments.GLDReturns(AttitudetoRisk)


@then('I add investment value as <CurrentValue>')
def i_add_investment_value_as_currentvalue(browser, CurrentValue):
    """I add investment value as <CurrentValue>."""
    Investments = investments(browser)
    Investments.currentvalue(CurrentValue)


@then('I verify the investment in scenario <InvestmentDescription>')
def i_verify_the_investment_in_scenario_investmentdescription(browser, InvestmentDescription):
    """I verify the investment in scenario <InvestmentDescription>."""
    Investments = investments(browser)
    Investments.verifyinvestmentinclude(InvestmentDescription)


@then(
    'User Add new risk profile <RiskProfileName> <GrossReturn> <Interest> <Dividends> <Growth> <Fund_Platform> <FinancialPlanning>')
def user_add_new_risk_profile_name_grossreturn_interest_dividends_growth_fund_platform_financialplanning(browser, RiskProfileName,
                                                                                                         GrossReturn,
                                                                                                         Interest,
                                                                                                         Dividends,
                                                                                                         Growth,
                                                                                                         Fund_Platform,
                                                                                                         FinancialPlanning):
    """User Add new risk profile <Name> <GrossReturn> <Interest> <Dividends> <Growth> <Fund_Platform> <FinancialPlanning>."""
    page_fla = FLA(browser)
    page_fla.DeleteRiskprofile_ifdisplayed(RiskProfileName)
    page_fla.AddRiskProfile(RiskProfileName, GrossReturn, Interest, Dividends, Growth, Fund_Platform, FinancialPlanning)
    page_fla.navigatetoClientpage()


@then('I navigate to investments page')
def i_navigate_to_investments_page(browser):
    """I navigate to investments page."""
    Investments = investments(browser)
    Investments.NavigatetoInvestment()


@then('I select investment as Pre existing <Investment>')
def i_select_investment_as_pre_existing_investment(browser, Investment):
    """I select investment as Pre existing <Investment>."""
    Investments = investments(browser)
    Investments.select_preexisting(Investment)


@then('i add investment type as <InvestmentType>')
def i_add_investment_type_as_investmenttype(browser, InvestmentType):
    """i add investment type as <InvestmentType>."""
    Investments = investments(browser)
    Investments.investmentType(InvestmentType)


@then('I logout from application')
def i_logout_from_application(browser):
    """I logout from application."""
    page_tables = Tables(browser)
    page_tables.NavigatetoTables()
    page_common = CommonFunctions(browser)
    page_common.DeleteClient()
    logout = CashflowLogin(browser)
    logout.logoutfromClientpage()


@then('I re-verify the investment plan is using parent Risk profile returns selected or not <InvestmentDescription> <ParentRiskprofile>')
def i_reverify_the_investment_plan_is_using_parent_risk_profile_returns_selected_or_not_investmentdescription_parentriskprofile(browser, InvestmentDescription, ParentRiskprofile):
    """I re-verify the investment plan is using parent Risk profile returns selected or not <InvestmentDescription> <ParentRiskprofile>."""
    Investments = investments(browser)
    Investments.NavigatetoInvestment()
    investments.Navigate_Investment_details(InvestmentDescription)
    investments.Verify_RiskProfile_Investment(ParentRiskprofile)
    investments.saveInvestment()



@then('User Navigate to FLA page and Disable the child override FLA and use parent risk profiles assumptions')
def user_navigate_to_fla_page_and_disable_the_child_override_fla_and_use_parent_risk_profiles_assumptions(browser):
    """User Navigate to FLA page and Disable the child override FLA and use parent risk profiles assumptions."""
    page_fla = FLA(browser)
    page_fla.NavigatetoFLApage_disableGLD()


@then(
    'User navigate to client list then select recent client and unlock the client with Parent Risk profile <ParentRiskprofile> <ClientName>')
def user_navigate_to_client_list_then_select_recent_client_and_unlock_the_client_with_parent_risk_profile_parentriskprofile_clientname(browser, ClientName, ParentRiskprofile):
    """User navigate to client list then select recent client and unlock the client with Parent Risk profile <ParentRiskprofile> <ClientName>."""
    page_fla = FLA(browser)
    page_fla.navigatetoClientpage()
    page_commons = CommonFunctions(browser)
    page_commons.clientSerach(ClientName)
    page_fla.UnlockPlan(ParentRiskprofile)