from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class AutomationExercisePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://automationexercise.com/login"

        self.signup_name = (By.XPATH, "//input[@data-qa='signup-name']")
        self.signup_email = (By.XPATH, "//input[@data-qa='signup-email']")
        self.signup_button = (By.XPATH, "//button[@data-qa='signup-button']")
        self.signup_error_msg = (By.XPATH, "//p[contains(text(),'Email Address already exist!')]")

        self.gender_male = (By.ID, "id_gender1")
        self.password_input = (By.ID, "password")
        self.days_select = (By.ID, "days")
        self.months_select = (By.ID, "months")
        self.years_select = (By.ID, "years")
        self.first_name = (By.ID, "first_name")
        self.last_name = (By.ID, "last_name")
        self.address = (By.ID, "address1")
        self.state = (By.ID, "state")
        self.city = (By.ID, "city")
        self.zipcode = (By.ID, "zipcode")
        self.mobile_number = (By.ID, "mobile_number")
        self.create_account_btn = (By.XPATH, "//button[@data-qa='create-account']")
        self.account_created_heading = (By.XPATH, "//b[contains(text(),'Account Created!')]")

        self.login_email = (By.XPATH, "//input[@data-qa='login-email']")
        self.login_password = (By.XPATH, "//input[@data-qa='login-password']")
        self.login_button = (By.XPATH, "//button[@data-qa='login-button']")
        self.login_error_msg = (By.XPATH, "//p[contains(text(),'Your email or password is incorrect!')]")

    def open(self):
        self.driver.get(self.url)

    def initiate_signup(self, name, email):
        self.driver.find_element(*self.signup_name).clear()
        self.driver.find_element(*self.signup_name).send_keys(name)
        self.driver.find_element(*self.signup_email).clear()
        self.driver.find_element(*self.signup_email).send_keys(email)
        self.driver.find_element(*self.signup_button).click()

    def complete_registration(self, password, fname, lname, addr, state, city, zip_code, mobile):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.gender_male)).click()
        self.driver.find_element(*self.password_input).send_keys(password)
        
        Select(self.driver.find_element(*self.days_select)).select_by_value("1")
        Select(self.driver.find_element(*self.months_select)).select_by_value("1")
        Select(self.driver.find_element(*self.years_select)).select_by_value("2000")

        self.driver.find_element(*self.first_name).send_keys(fname)
        self.driver.find_element(*self.last_name).send_keys(lname)
        self.driver.find_element(*self.address).send_keys(addr)
        self.driver.find_element(*self.state).send_keys(state)
        self.driver.find_element(*self.city).send_keys(city)
        self.driver.find_element(*self.zipcode).send_keys(zip_code)
        self.driver.find_element(*self.mobile_number).send_keys(mobile)
        self.driver.find_element(*self.create_account_btn).click()

    def login(self, email, password):
        self.driver.find_element(*self.login_email).clear()
        self.driver.find_element(*self.login_email).send_keys(email)
        self.driver.find_element(*self.login_password).clear()
        self.driver.find_element(*self.login_password).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def take_step_screenshot(self, step_name):
        """Automatically saves a custom step screenshot inside screenshots/STEPS/"""
        base_dir = Path(__file__).resolve().parent.parent
        steps_dir = base_dir / "screenshots" / "STEPS"
        steps_dir.mkdir(parents=True, exist_ok=True)
        
        file_path = steps_dir / f"{step_name}.png"
        self.driver.save_screenshot(str(file_path))
        print(f"\n[Screenshot Saved]: {file_path}")