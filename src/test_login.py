from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
import logging
import time
import csv
from constants import BASE_URL
from login_page import LoginPage

# Enhanced logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('test_execution.log')
    ]
)

def setup_driver():
    """Setup WebDriver with appropriate options"""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-popup-blocking')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    
    return webdriver.Chrome(options=chrome_options)

def load_test_data(file_path):
    """Load test data from CSV file"""
    test_cases = []
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Determine if this should be a successful login
                expected_success = (row['username'] == 'student' and row['password'] == 'Password123')
                test_cases.append({
                    'username': row['username'],
                    'password': row['password'],
                    'expected_success': expected_success,
                    'description': f"Testing with {row['username']}"
                })
        return test_cases
    except FileNotFoundError:
        logging.error(f"Test data file not found: {file_path}")
        return []

def main():
    driver = None
    try:
        driver = setup_driver()
        driver.set_page_load_timeout(30)
        
        driver.get(BASE_URL)
        logging.info(f"Navigated to {BASE_URL}")
        time.sleep(2)  # Wait for initial page load
        
        login_page = LoginPage(driver)
        
        # Load test cases from CSV
        test_cases = load_test_data('data/test_cases.csv')
        if not test_cases:
            logging.error("No test cases found in CSV. Exiting...")
            return
            
        for case in test_cases:
            try:
                logging.info(f"\n=== Testing {case['description']} ===")
                logging.info(f"Username: {case['username']}, Password: {case['password']}")
                
                # Ensure we're on the login page
                if "practice-test-login" not in driver.current_url:
                    driver.get(BASE_URL)
                    time.sleep(2)
                
                # Perform login actions
                login_page.enter_username(case['username'])
                login_page.enter_password(case['password'])
                login_page.click_submit()
                
                # Check results
                if case['expected_success']:
                    if login_page.is_login_successful():
                        logging.info("✅ Test Passed: Successfully logged in")
                    else:
                        logging.error("❌ Test Failed: Login should have succeeded but didn't")
                else:
                    error_message = login_page.get_error_message()
                    if error_message:
                        if "Your username is invalid" in error_message or "Your password is invalid" in error_message:
                            logging.info(f"✅ Test Passed: Correct error message: {error_message}")
                        else:
                            logging.error(f"❌ Test Failed: Unexpected error message: {error_message}")
                    else:
                        logging.error("❌ Test Failed: No error message displayed for invalid credentials")
                
                # Reset for next test
                login_page.reset_session()
                time.sleep(2)  # Wait between tests
                
            except Exception as e:
                logging.error(f"Error during test case execution: {str(e)}")
                # Try to recover for next test
                try:
                    driver.get(BASE_URL)
                    time.sleep(2)
                except:
                    pass
                continue
                
    except Exception as e:
        logging.error(f"Fatal error during test execution: {str(e)}")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    main()