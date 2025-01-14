
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging
import os
from datetime import datetime
from login_page import LoginPage
from test_data_manager import TestDataManager
from constants import (
    BASE_URL,
    LOGS_DIR,
    SCREENSHOTS_DIR,
    LOG_FORMAT
)

class LoginTest:
    def __init__(self):
        # Create necessary directories
        for directory in [LOGS_DIR, SCREENSHOTS_DIR]:
            if not os.path.exists(directory):
                os.makedirs(directory)
        
        # Setup logging
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logging.basicConfig(
            filename=f'{LOGS_DIR}/test_run_{timestamp}.log',
            level=logging.INFO,
            format=LOG_FORMAT
        )
        
        self.test_data_manager = TestDataManager()
        
    def setup_driver(self):
        """Initialize the Chrome WebDriver"""
        try:
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service)
            driver.maximize_window()
            return driver
        except Exception as e:
            logging.error(f"Failed to setup WebDriver: {str(e)}")
            raise
            
    def take_screenshot(self, driver, test_name):
        """Take screenshot on test failure"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{SCREENSHOTS_DIR}/failed_{test_name}_{timestamp}.png"
        driver.save_screenshot(filename)
        return filename
        
    def run_single_test(self, driver, test_case):
        """Run a single test case"""
        login_page = LoginPage(driver)
        
        # Navigate to the login page
        driver.get(BASE_URL)
        
        # Perform login steps
        username_entered = login_page.enter_username(str(test_case['username']))
        password_entered = login_page.enter_password(str(test_case['password']))
        submit_clicked = login_page.click_submit()
        
        if not all([username_entered, password_entered, submit_clicked]):
            return {
                'test_case': test_case['test_case'],
                'status': 'ERROR',
                'error': 'Failed to perform login steps'
            }
            
        # Check results
        actual_result = 'success' if login_page.is_login_successful() else 'failure'
        test_passed = actual_result == test_case['expected_result']
        
        result = {
            'test_case': test_case['test_case'],
            'username': test_case['username'],
            'expected_result': test_case['expected_result'],
            'actual_result': actual_result,
            'status': 'PASSED' if test_passed else 'FAILED'
        }
        
        # Take screenshot if test failed
        if not test_passed:
            screenshot = self.take_screenshot(driver, test_case['test_case'])
            result['screenshot'] = screenshot
            result['error_message'] = login_page.get_error_message()
            
        return result
        
    def run_tests(self):
        """Run all test cases"""
        logging.info("Starting test execution")
        results = []
        driver = None
        
        try:
            # Setup WebDriver
            driver = self.setup_driver()
            
            # Load test data
            test_cases = self.test_data_manager.load_test_data()
            
            # Execute each test case
            for _, test_case in test_cases.iterrows():
                logging.info(f"\nExecuting test case: {test_case['test_case']}")
                result = self.run_single_test(driver, test_case)
                results.append(result)
                logging.info(f"Test case {test_case['test_case']}: {result['status']}")
                
        except Exception as e:
            logging.error(f"Test execution error: {str(e)}")
            
        finally:
            if driver:
                driver.quit()
                
        # Save results
        results_file = self.test_data_manager.save_test_results(results)
        
        # Print summary
        self.print_summary(results)
        
        return results
        
    def print_summary(self, results):
        """Print test execution summary"""
        total = len(results)
        passed = sum(1 for r in results if r['status'] == 'PASSED')
        failed = sum(1 for r in results if r['status'] == 'FAILED')
        errors = sum(1 for r in results if r['status'] == 'ERROR')
        
        summary = f"""
        \nTest Execution Summary
        ---------------------
        Total Tests: {total}
        Passed: {passed}
        Failed: {failed}
        Errors: {errors}
        """
        
        print(summary)
        logging.info(summary)

if __name__ == "__main__":
    test = LoginTest()
    test.run_tests()