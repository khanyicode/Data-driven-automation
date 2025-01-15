# constants.py

# Website URL
BASE_URL = "https://practicetestautomation.com/practice-test-login/"

# Browser settings
BROWSER_TYPE = "chrome"  # or "firefox"
WAIT_TIME = 10  # seconds to wait for elements

# Test data
VALID_USERNAME = "student"
VALID_PASSWORD = "Password123"
INVALID_USERNAME = "incorrectUser"
INVALID_PASSWORD = "incorrectPassword"

# Web element IDs and classes
USERNAME_FIELD = "username"
PASSWORD_FIELD = "password"
SUBMIT_BUTTON = "submit"
SUCCESS_MESSAGE_CLASS = "post-title"
ERROR_MESSAGE_CLASS = "error"

# Logging configuration
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
