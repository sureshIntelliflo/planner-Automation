# coding=utf-8
"""Verify the Property feature tests."""
import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

@pytest.mark.usefixtures("browser")
@scenario('../Features/AddProperty.feature', 'User Login')
def test_user_login():
    """User Login."""



