# coding=utf-8
"""Income and DC pensions feature tests."""
import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from Pages.Income import Income
from Pages.Pensions import Pensions


@pytest.mark.usefixtures("browser")
@scenario('../features/IncomeDBPensions.feature', 'Verify the income and DB Pensions Linking')
def test_verify_the_income_and_db_pesnions_linking():
    """Verify the income and DB pesnions Linking."""


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

@then('I add Pension and verify added pensions <PensionDescription>z')
def i_add_pension_and_verify_added_pensions_pensiondescriptionz(browser, PensionDescription):
    """I add Pension and verify added pensions <PensionDescription>z."""
    page_Pension = Pensions(browser)
    page_Pension.AddPension(PensionDescription)


@then('I add benefit basis <Benefitstype>')
def i_add_benefit_basis_benefitstype(browser, Benefitstype):
    """I add benefit basis <Benefitstype>."""
    page_Pension = Pensions(browser)
    page_Pension.BenefitBasis(Benefitstype)

@then('I add benefit income <BenefitIncome> and benefit lump sum <LumpSum>')
def i_add_benefit_income_benefitincome_and_benefit_lump_sum_lumpsum(browser, BenefitIncome, LumpSum):
    """I add benefit income <BenefitIncome> and benefit lump sum <LumpSum>."""
    page_Pension = Pensions(browser)
    page_Pension.BenefitStatementValues(BenefitIncome, LumpSum)

@then('I add contributions with income linking <IncomeDescription> with gross contributions <GrossContributions> pension basis <PensionBasis>')
def i_add_contributions_with_income_linking_incomedescription_with_gross_contributions_grosscontributions_pension_basis_pensionbasis(browser, IncomeDescription, GrossContributions, PensionBasis):
    """I add contributions with income linking <IncomeDescription> with gross contributions <GrossContributions> pension basis <PensionBasis>."""
    page_Pension = Pensions(browser)
    page_Pension.BenefitContributions(IncomeDescription, GrossContributions, PensionBasis)

@then('I add death options with spouse income after death and death lump sum <LumpSumOptions> <ServiceMultiplier>')
def i_add_death_options_with_spouse_income_after_death_and_death_lump_sum_spouseincomeafterdeath_lumpsumoptions_servicemultiplier(browser, LumpSumOptions, ServiceMultiplier):
    """I add death options with spouse income after death and death lump sum <SpouseIncomeAfterDeath> <LumpSumOptions> <ServiceMultiplier>."""
    page_Pension = Pensions(browser)
    page_Pension.BenefitDeathOptions(LumpSumOptions, ServiceMultiplier)

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

@then('I add pension description <PensionDescription>')
def i_add_pension_description_pensiondescription(browser, PensionDescription):
    """I add pension description <PensionDescription>."""
    page_Pension = Pensions(browser)
    page_Pension.AddPensionDescription(PensionDescription)


@then('I enable adjust lifetime allowance')
def i_enable_adjust_lifetime_allowance(browser):
    """I enable adjust lifetime allowance."""
    page_Pension = Pensions(browser)
    page_Pension.AdjustLifetimeAllowance()


@then('I navigate to Income page')
def i_navigate_to_income_page(browser):
    """I navigate to Income page."""
    page_income = Income(browser)
    page_income.NavigatetoIncome()

@then('I navigate to pensions')
def i_navigate_to_pensions(browser):
    """I navigate to pensions."""
    page_Pension = Pensions(browser)
    page_Pension.Navigatetopensions()


@then('I select policy status <pensionstype>')
def i_select_policy_status_pensionstype(browser, pensionstype):
    """I select policy status <pensionstype>."""
    page_Pension = Pensions(browser)
    page_Pension.policyStatus(pensionstype)

@then('I select policy structure is Defined Benefit')
def i_select_policy_structure_policystructure(browser):
    """I select policy structure <PolicyStructure>."""
    page_Pension = Pensions(browser)
    page_Pension.AddPensionPolicyStructure()
