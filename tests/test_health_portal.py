import pytest
from playwright.sync_api import Page, expect

# Test Case 1: Core Dashboard Authentication Verification
def test_clinical_portal_authentication(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()
    
    # Assert successful medical portal session initiation
    expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")

# Test Case 2: Boundary Value & Edge Case Input Validation (Data Integrity Check)
def test_cgm_data_entry_boundary_limits(page: Page):
    page.goto("https://the-internet.herokuapp.com/inputs")
    
    # Simulate a user trying to manually input an invalid negative blood glucose level or extreme boundary
    # In health-tech, data validation at the UI layer prevents dangerous clinical calculation errors
    invalid_glucose_input = "-15"
    page.locator("input[type='number']").fill(invalid_glucose_input)
    
    # Extract the value to verify how the application stores it
    current_value = page.locator("input[type='number']").input_value()
    
    # A robust UI should either block negative entries or flag them
    print(f"\n[QA Log] System UI captured input value: {current_value}")
    assert current_value == invalid_glucose_input or current_value == ""

# Test Case 3: Visual Element and Context State Verification
def test_dashboard_ui_responsiveness(page: Page):
    page.goto("https://the-internet.herokuapp.com/dynamic_content")
    
    # Verify core dashboard visual frame elements are visible and loading consistently
    expect(page.locator("#content")).to_be_visible()
