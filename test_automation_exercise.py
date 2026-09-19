import time
import pytest
from pages.automation_exercise_page import AutomationExercisePage

@pytest.fixture
def unique_email():
    return f"test_user_{int(time.time())}@example.com"

def test_full_user_registration(driver, unique_email):
    app = AutomationExercisePage(driver)
    app.open()
    app.take_step_screenshot("01_registration_page_opened")
    
    app.initiate_signup("Automation Tester", unique_email)
    app.take_step_screenshot("02_signup_initiated")
    
    app.complete_registration(
        password="PassWord123!",
        fname="John",
        lname="Doe",
        addr="123 Test Street",
        state="Punjab",
        city="Mohali",
        zip_code="160055",
        mobile="9876543210"
    )
    app.take_step_screenshot("03_registration_submitted")
    
    assert driver.find_element(*app.account_created_heading).is_displayed()
    app.take_step_screenshot("04_account_creation_verified")

@pytest.mark.parametrize("email, password, expected_result", [
    ("invalid_user_999@domain.com", "Password123!", "error"),
    ("test_user@example.com", "WrongPassword", "error"),
    ("", "PassWord123!", "native_validation"),
    ("test_user@example.com", "", "native_validation"),
])
def test_login_boundary_conditions(driver, email, password, expected_result):
    app = AutomationExercisePage(driver)
    app.open()
    app.login(email, password)
    
    clean_label = f"login_boundary_{email or 'empty_email'}_{password or 'empty_pass'}"
    app.take_step_screenshot(clean_label)
    
    if expected_result == "error":
        assert driver.find_element(*app.login_error_msg).is_displayed()
    elif expected_result == "native_validation":
        email_input = driver.find_element(*app.login_email)
        pass_input = driver.find_element(*app.login_password)
        
        is_invalid = (
            email_input.get_attribute("validationMessage") != "" or 
            pass_input.get_attribute("validationMessage") != ""
        )
        assert is_invalid, "Expected browser HTML5 validation popup for empty input field"

def test_duplicate_email_registration(driver):
    app = AutomationExercisePage(driver)
    app.open()
    app.initiate_signup("Duplicate User", "sharmasuhati544@gmail.com")
    app.take_step_screenshot("duplicate_signup_attempted")
    
    assert driver.find_element(*app.signup_error_msg).is_displayed()