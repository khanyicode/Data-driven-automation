# test_login.py

import csv
from selenium import webdriver
import logging

from constants import BASE_URL, LOG_FORMAT
from login_page import LoginPage  # Import LoginPage class

# Logging configuration
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

def load_test_data(file_path):
    """Load test data from a CSV file."""
    test_data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            test_data.append(row)
    return test_data

def main():
    driver = webdriver.Chrome()  # or webdriver.Firefox()

    try:
        driver.get(BASE_URL)

        login_page = LoginPage(driver)

        # Load test data from CSV
        test_cases = load_test_data('data/test_cases.csv')

        for case in test_cases:
            username = case['username']
            password = case['password']

            logging.info(f"Running test with username: {username} and password: {password}")
            login_page.enter_username(username)
            login_page.enter_password(password)
            login_page.click_submit()

            if username == "student" and password == "Password123":
                if login_page.is_login_successful():
                    logging.info("Test Passed: Logged In Successfully")
                else:
                    logging.error("Test Failed: Login was not successful")
            else:
                error_message = login_page.get_error_message()
                if "invalid" in error_message.lower():
                    logging.info("Test Passed: Correct error message displayed")
                else:
                    logging.error("Test Failed: Incorrect error message")

    finally:
        driver.quit()  # Close the browser

if __name__ == "__main__":
    main()
