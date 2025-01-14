# src/test_data_manager.py

import pandas as pd
import os
from datetime import datetime
from constants import DATA_DIR, RESULTS_DIR

class TestDataManager:
    @staticmethod
    def create_test_data():
        """Create initial test data CSV file"""
        test_data = [
            # username, password, expected_result, test_case
            ['student', 'Password123', 'success', 'Valid credentials'],
            ['incorrectUser', 'Password123', 'failure', 'Invalid username'],
            ['student', 'incorrectPassword', 'failure', 'Invalid password'],
            ['', 'Password123', 'failure', 'Empty username'],
            ['student', '', 'failure', 'Empty password'],
            ['admin', 'admin123', 'failure', 'Invalid credentials'],
        ]
        
        df = pd.DataFrame(test_data, columns=['username', 'password', 'expected_result', 'test_case'])
        
        # Create data directory if it doesn't exist
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
            
        # Save test data to CSV
        df.to_csv(f'{DATA_DIR}/test_cases.csv', index=False)
        return df

    @staticmethod
    def load_test_data():
        """Load test data from CSV file"""
        try:
            return pd.read_csv(f'{DATA_DIR}/test_cases.csv')
        except FileNotFoundError:
            return TestDataManager.create_test_data()

    @staticmethod
    def save_test_results(results):
        """Save test results to CSV file"""
        if not os.path.exists(RESULTS_DIR):
            os.makedirs(RESULTS_DIR)
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'{RESULTS_DIR}/test_results_{timestamp}.csv'
        
        df = pd.DataFrame(results)
        df.to_csv(filename, index=False)
        return filename