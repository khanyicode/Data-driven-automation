# login_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from constants import (
    USERNAME_FIELD,
    PASSWORD_FIELD,
    SUBMIT_BUTTON,
    SUCCESS_MESSAGE_CLASS,
    ERROR_MESSAGE_CLASS,
    WAIT_TIME,
)

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, WAIT_TIME)

    def enter_username(self, username):
        """Enter username in the username field"""
        try:
            username_element = self.wait.until(
                EC.presence_of_element_located((By.ID, USERNAME_FIELD))
            )
            username_element.clear()
            username_element.send_keys(username)
            logging.info(f"Entered username: {username}")
            return True
        except Exception as e:
            logging.error(f"Error entering username: {str(e)}")
            return False
            
    def enter_password(self, password):
        """Enter password in the password field"""
        try:
            password_element = self.wait.until(
                EC.presence_of_element_located((By.ID, PASSWORD_FIELD))
            )
            password_element.clear()
            password_element.send_keys(password)
            logging.info("Entered password")
            return True
        except Exception as e:
            logging.error(f"Error entering password: {str(e)}")
            return False
            
    def click_submit(self):
        """Click the submit button"""
        try:
            submit_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, SUBMIT_BUTTON))
            )
            submit_button.click()
            logging.info("Clicked submit button")
            return True
        except Exception as e:
            logging.error(f"Error clicking submit button: {str(e)}")
            return False
            
    def is_login_successful(self):
        """Check if login was successful"""
        try:
            success_element = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, SUCCESS_MESSAGE_CLASS))
            )
            return "Congratulations" in success_element.text or "successfully logged in" in success_element.text
        except Exception:
            return False
            
    def get_error_message(self):
        """Get error message if login failed"""
        try:
            error_element = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, ERROR_MESSAGE_CLASS))
            )
            return error_element.text
        except Exception:
            return "No error message found"

    def get_current_url(self):
        """Get the current URL of the page"""
        return self.driver.current_url
