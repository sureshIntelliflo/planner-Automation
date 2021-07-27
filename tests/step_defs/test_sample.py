# coding=utf-8
"""Income and DB pensions feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('features\IncomeDBPensions.feature', 'Verify the income and DB Pensions Linking')
def test_verify_the_income_and_db_pensions_linking():
    """Verify the income and DB Pensions Linking."""


@given('user logged into application with email as "spped_12499" and password as "Suresh@2021"')
def user_logged_into_application_with_email_as_spped_12499_and_password_as_suresh2021():
    """user logged into application with email as "spped_12499" and password as "Suresh@2021"."""
    raise NotImplementedError


@when('User in cashflow home page')
def user_in_cashflow_home_page():
    """User in cashflow home page."""
    raise NotImplementedError


@when('user logged in and I add client with details name as "IncomePensionlinked", KnowAs "QA Automation", DOB "01/01/1990",Tax residency "England", gender as "Male" and Create client with case name as "AutomatedQA_IncomePension"')
def user_logged_in_and_i_add_client_with_details_name_as_incomepensionlinked_knowas_qa_automation_dob_01011990tax_residency_england_gender_as_male_and_create_client_with_case_name_as_automatedqa_incomepension():
    """user logged in and I add client with details name as "IncomePensionlinked", KnowAs "QA Automation", DOB "01/01/1990",Tax residency "England", gender as "Male" and Create client with case name as "AutomatedQA_IncomePension"."""
    raise NotImplementedError


@then('I Add pensions from pensions page')
def i_add_pensions_from_pensions_page():
    """I Add pensions from pensions page."""
    raise NotImplementedError


@then('I add Income type <IncomeType>')
def i_add_income_type_incometype():
    """I add Income type <IncomeType>."""
    raise NotImplementedError


@then('I add Pension and verify added pensions <PensionDescription>z')
def i_add_pension_and_verify_added_pensions_pensiondescriptionz():
    """I add Pension and verify added pensions <PensionDescription>z."""
    raise NotImplementedError


@then('I add benefit basis <Benefitstype>')
def i_add_benefit_basis_benefitstype():
    """I add benefit basis <Benefitstype>."""
    raise NotImplementedError


@then('I add benefit income <BenefitIncome> and benefit lump sum <LumpSum>')
def i_add_benefit_income_benefitincome_and_benefit_lump_sum_lumpsum():
    """I add benefit income <BenefitIncome> and benefit lump sum <LumpSum>."""
    raise NotImplementedError


@then('I add contributions with income linking <IncomeDescription> with gross contributions <GrossContributions> pension basis <PensionBasis>')
def i_add_contributions_with_income_linking_incomedescription_with_gross_contributions_grosscontributions_pension_basis_pensionbasis():
    """I add contributions with income linking <IncomeDescription> with gross contributions <GrossContributions> pension basis <PensionBasis>."""
    raise NotImplementedError


@then('I add death options with spouse income after death and death lump sum <SpouseIncomeAfterDeath> <LumpSumOptions> <ServiceMultiplier>')
def i_add_death_options_with_spouse_income_after_death_and_death_lump_sum_spouseincomeafterdeath_lumpsumoptions_servicemultiplier():
    """I add death options with spouse income after death and death lump sum <SpouseIncomeAfterDeath> <LumpSumOptions> <ServiceMultiplier>."""
    raise NotImplementedError


@then('I add income amount <IncomeAmount>')
def i_add_income_amount_incomeamount():
    """I add income amount <IncomeAmount>."""
    raise NotImplementedError


@then('I add income and verify added income <IncomeDescription>')
def i_add_income_and_verify_added_income_incomedescription():
    """I add income and verify added income <IncomeDescription>."""
    raise NotImplementedError


@then('I add income current or future type <CurrentFutureIncome>')
def i_add_income_current_or_future_type_currentfutureincome():
    """I add income current or future type <CurrentFutureIncome>."""
    raise NotImplementedError


@then('I add income description <IncomeDescription>')
def i_add_income_description_incomedescription():
    """I add income description <IncomeDescription>."""
    raise NotImplementedError


@then('I add new income from income Page')
def i_add_new_income_from_income_page():
    """I add new income from income Page."""
    raise NotImplementedError


@then('I add pension description <PensionDescription>')
def i_add_pension_description_pensiondescription():
    """I add pension description <PensionDescription>."""
    raise NotImplementedError


@then('I enable adjust lifetime allowance')
def i_enable_adjust_lifetime_allowance():
    """I enable adjust lifetime allowance."""
    raise NotImplementedError


@then('I navigate to Income page')
def i_navigate_to_income_page():
    """I navigate to Income page."""
    raise NotImplementedError


@then('I navigate to pensions')
def i_navigate_to_pensions():
    """I navigate to pensions."""
    raise NotImplementedError


@then('I select policy status <pensionstype>')
def i_select_policy_status_pensionstype():
    """I select policy status <pensionstype>."""
    raise NotImplementedError


@then('I select policy structure is Defined Benefit')
def i_select_policy_structure_is_defined_benefit():
    """I select policy structure is Defined Benefit."""
    raise NotImplementedError

