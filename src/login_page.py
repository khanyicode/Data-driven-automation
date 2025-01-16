from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=0.5,
                                ignored_exceptions=[StaleElementReferenceException])
        
        # Updated locators with multiple strategies
        self.username_field = (By.CSS_SELECTOR, "#username")
        self.password_field = (By.CSS_SELECTOR, "#password")
        self.submit_button = (By.CSS_SELECTOR, "button#submit")
        self.error_message = (By.CSS_SELECTOR, "#error")
        self.success_message = (By.CSS_SELECTOR, ".post-title")
        self.logout_button = (By.LINK_TEXT, "Log out")

    def wait_and_find_element(self, locator):
        """Utility method to wait for and find an element with better error handling"""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            # Try refreshing the page once if element not found
            self.driver.refresh()
            return self.wait.until(EC.presence_of_element_located(locator))

    def enter_username(self, username):
        element = self.wait_and_find_element(self.username_field)
        element.clear()
        time.sleep(0.5)  # Small delay after clear
        element.send_keys(username)
        
    def enter_password(self, password):
        element = self.wait_and_find_element(self.password_field)
        element.clear()
        time.sleep(0.5)  # Small delay after clear
        element.send_keys(password)
        
    def click_submit(self):
        element = self.wait.until(EC.element_to_be_clickable(self.submit_button))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)  # Small delay before click
        element.click()
        time.sleep(1)  # Wait for form submission
        
    def get_error_message(self):
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.error_message))
            return element.text
        except TimeoutException:
            return None
        
    def is_login_successful(self):
        try:
            # First check for success message
            success_element = self.wait.until(
                EC.presence_of_element_located(self.success_message)
            )
            return "Logged In Successfully" in success_element.text
        except TimeoutException:
            try:
                # Alternative check for logout button
                self.wait.until(EC.presence_of_element_located(self.logout_button))
                return True
            except TimeoutException:
                return False

    def reset_session(self):
        """Reset the session by navigating back to login page"""
        try:
            self.driver.delete_all_cookies()
            self.driver.get("https://practicetestautomation.com/practice-test-login/")
            self.wait.until(EC.presence_of_element_located(self.username_field))
            time.sleep(1)  # Allow page to fully load
        except Exception as e:
            print(f"Error during reset: {str(e)}")
            self.driver.refresh()
