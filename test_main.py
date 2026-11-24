
import pytest

from main import (
    units_cost,
    fixed_charge,
    total_bill,
    bill_category
)


def test_units_cost_100():
    assert units_cost(100) == 450


def test_units_cost_150():
    assert units_cost(150) == 750


def test_units_cost_250():
    assert units_cost(250) == 1425


def test_fixed_charge():
    assert fixed_charge() == 50


def test_total_bill():
    assert total_bill(150) == 800


def test_negative_units():
    with pytest.raises(ValueError):
        units_cost(-10)


def test_low_bill_category():
    assert bill_category(400) == "Low Bill"


def test_medium_bill_category():
    assert bill_category(800) == "Medium Bill"


def test_high_bill_category():
    assert bill_category(1500) == "High Bill"
