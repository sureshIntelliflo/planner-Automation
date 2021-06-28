# coding=utf-8
"""Verify the Property feature tests."""
import time

import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when, parsers,
)
CASHFLOW_SYS_IE_02 = "https://planning.sys-ie-02.intelliflo.systems/dashboard/clients"
@pytest.mark.usefixtures("browser")
@scenario('../Features/AddProperty.feature', 'User Login')
def test_user_login():
    """User Login."""


