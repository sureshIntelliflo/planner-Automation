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
@scenario('../features/IncomeDCPension.feature', 'Verify the income and DC Pensions Linking')
def test_verify_the_income_and_dC_pesnions_linking():
    """Verify the income and DC pesnions Linking."""

