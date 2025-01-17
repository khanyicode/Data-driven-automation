# Data Driven Automation

## Overview
This is a Selenium-based test automation framework designed to validate login functionality of [Practice Test Automation](https://practicetestautomation.com/practice-test-login/) website The framework uses Python and implements the Page Object Model (POM) pattern to test various login scenarios on a practice website. A key feature of this framework is its data-driven testing approach, demonstrating real-world testing practices used by professional development teams.

## Features
- Automated login testing with multiple test cases
- Data-driven testing using CSV files for scalable test management
- Detailed logging with both console and file output
- Error handling and recovery
- Page Object Model implementation for better maintenance
- Chrome WebDriver support with configurable options

## Prerequisites
- Python 3.x
- Chrome browser
- ChromeDriver (compatible with your Chrome version)
- Required Python packages:
  - selenium
  - pytest

## Data-Driven Testing Approach
This framework implements data-driven testing, a practice widely used in professional development teams. Instead of hardcoding test data in the source code, the framework reads test scenarios from external CSV files. This approach offers several advantages:

- **Scalability**: Can handle hundreds or thousands of test cases without code modifications
- **Maintainability**: Test data can be updated without changing code
- **Collaboration**: Non-technical team members can contribute test cases
- **Flexibility**: Easy to add new test scenarios or modify existing ones


## Test Data Structure
The CSV file (`data/test_cases.csv`) contains test scenarios with the following structure:

Each row represents a unique test case, allowing for:
- Valid login attempts
- Invalid username scenarios
- Invalid password scenarios
- Empty field validations

## Installation
1. Clone the repository
2. Install required packages:
   ```bash
   pip install selenium
   ```
3. Ensure ChromeDriver is in your system PATH

## Configuration
Key configurations are stored in `constants.py`:
- `BASE_URL`: Target website URL
- `WAIT_TIME`: Default wait time for elements
- `BROWSER_TYPE`: Browser selection
- Test credentials and element locators

## Running Tests
Execute the test suite by running:
```bash
python3 src/test_login.py
```

## Logging
The framework provides comprehensive logging:
- Console output for real-time monitoring
- File logging in `test_execution.log`
- Test results with clear pass/fail indicators

## Error Handling
The framework includes:
- Automatic recovery from common failures
- Session reset between tests
- Detailed error logging
- Page load verification

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request





