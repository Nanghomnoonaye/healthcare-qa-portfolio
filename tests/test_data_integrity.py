"""Data-integrity / boundary-value tests on a numeric input.

Models a clinical numeric field such as a CGM blood-glucose reading. The goal
is to document exactly how the UI layer handles out-of-range and edge values,
because unchecked values can flow into downstream clinical calculations.

NOTE: the demo application deliberately performs NO client-side validation, so
several of these tests assert (and thereby document) that invalid values are
accepted. Those gaps are written up as defect tickets in docs/BUG_REPORTS.md
(BUG-001 / BUG-002) — which is the real deliverable a QA engineer produces.
"""
import pytest


@pytest.mark.data_integrity
@pytest.mark.parametrize("value", ["-15", "-0.1", "-999"])
def test_negative_values_are_accepted_without_validation(inputs_page, value):
    """FINDING (BUG-001): negative 'glucose' values are stored, not blocked."""
    inputs_page.enter_value(value)
    assert inputs_page.current_value == value, (
        "Expected the field to retain the entered value; a validated clinical "
        "field should instead reject or flag it."
    )


@pytest.mark.data_integrity
def test_implausibly_large_value_is_accepted(inputs_page):
    """FINDING (BUG-002): extreme out-of-range readings are accepted."""
    inputs_page.enter_value("999999")
    assert inputs_page.current_value == "999999"


@pytest.mark.data_integrity
def test_decimal_precision_is_preserved(inputs_page):
    """A valid decimal reading is preserved exactly (no rounding/truncation)."""
    inputs_page.enter_value("5.6")
    assert inputs_page.current_value == "5.6"


@pytest.mark.data_integrity
def test_arrow_up_increments_from_empty(inputs_page):
    """Stepping up from an empty field yields the first step value (1)."""
    inputs_page.press_up_arrow(1)
    assert inputs_page.current_value == "1"


@pytest.mark.data_integrity
def test_arrow_up_increments_existing_value(inputs_page):
    """Stepping up increments a valid in-range reading by one."""
    inputs_page.enter_value("5")
    inputs_page.press_up_arrow(2)
    assert inputs_page.current_value == "7"


@pytest.mark.data_integrity
def test_non_numeric_characters_are_not_stored(inputs_page):
    """A number field must not retain alphabetic input."""
    inputs_page.type_value("abc")
    assert inputs_page.current_value == "", (
        "A type=number field should reject non-numeric characters."
    )
