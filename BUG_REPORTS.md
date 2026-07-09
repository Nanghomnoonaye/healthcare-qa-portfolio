# Defect Log

Sample defect reports produced while building the test suite. Each entry uses a
standard bug-ticket format (steps, expected, actual, severity) so they can be
dropped straight into Jira, Linear, or a GitHub Issue.

> Application under test: `https://the-internet.herokuapp.com` (public practice
> site). Findings are framed against how a **validated clinical/fintech** field
> *should* behave.

---

## BUG-001 — Numeric field accepts negative "glucose" values

| Field | Detail |
|-------|--------|
| **ID** | BUG-001 |
| **Severity** | High |
| **Priority** | P2 |
| **Component** | Data entry / numeric input |
| **Status** | Open |

**Steps to reproduce**
1. Go to `/inputs`.
2. Click the number field.
3. Enter `-15`.

**Expected**
A clinical reading field (e.g. blood glucose) should reject or flag physically
impossible negative values before they are stored or calculated on.

**Actual**
The field silently accepts and retains `-15`; no error, no flag.

**Impact**
Invalid values can propagate into downstream clinical calculations, producing
dangerous or nonsensical results.

**Covered by test:** `tests/test_data_integrity.py::test_negative_values_are_accepted_without_validation`

---

## BUG-002 — Numeric field accepts implausibly large readings

| Field | Detail |
|-------|--------|
| **ID** | BUG-002 |
| **Severity** | Medium |
| **Priority** | P3 |
| **Component** | Data entry / numeric input |
| **Status** | Open |

**Steps to reproduce**
1. Go to `/inputs`.
2. Enter `999999`.

**Expected**
Out-of-range readings should be constrained by a sensible max (e.g. a plausible
clinical upper bound) or flagged for review.

**Actual**
The field accepts `999999` with no upper-bound check.

**Covered by test:** `tests/test_data_integrity.py::test_implausibly_large_value_is_accepted`

---

## How I would prioritise these

BUG-001 is High/P2: a negative clinical value is both plausible to fumble into
and genuinely unsafe downstream. BUG-002 is Medium: less likely, and often
caught by later processing — but still worth a UI-level guard as defense in
depth.
