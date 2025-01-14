
# Website URL
BASE_URL = "https://practicetestautomation.com/practice-test-login/"

# Browser settings
BROWSER_TYPE = "chrome"  # or "firefox"
WAIT_TIME = 10  # seconds to wait for elements

# Test data
VALID_USERNAME = "student"
VALID_PASSWORD = "Password123"

# Web element IDs
USERNAME_FIELD = "username"
PASSWORD_FIELD = "password"
SUBMIT_BUTTON = "submit"
SUCCESS_MESSAGE = "post-title"

# Directory paths
LOGS_DIR = "logs"
SCREENSHOTS_DIR = "screenshots"
RESULTS_DIR = "results"
DATA_DIR = "data"

# File paths
TEST_DATA_FILE = "data/test_cases.csv"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

# Test result messages
SUCCESS_MESSAGE_TEXT = "Logged In Successfully"
ERROR_MESSAGE_CLASS = "error"