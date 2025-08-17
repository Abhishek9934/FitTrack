import streamlit as st
from utils.data_manager import DataManager
from utils.sheets_manager import SheetsManager

class HybridManager:
    """
    Hybrid data manager that uses Google Sheets when available,
    falls back to CSV files when not connected
    """
    
    def __init__(self):
        self.sheets_manager = SheetsManager()
        self.csv_manager = DataManager()
        self.use_sheets = self.sheets_manager.is_connected()
        
        if self.use_sheets:
            st.success("Connected to Google Sheets for data storage")
        else:
            st.info("Using local CSV files for data storage")
    
    def is_using_sheets(self):
        """Check if currently using Google Sheets"""
        return self.use_sheets
    
    def save_body_metrics(self, data):
        """Save body metrics data"""
        if self.use_sheets:
            return self.sheets_manager.save_body_metrics(data)
        else:
            return self.csv_manager.save_body_metrics(data)
    
    def save_workout_data(self, data):
        """Save workout data"""
        if self.use_sheets:
            return self.sheets_manager.save_workout_data(data)
        else:
            return self.csv_manager.save_workout_data(data)
    
    def save_diet_data(self, data):
        """Save diet data"""
        if self.use_sheets:
            return self.sheets_manager.save_diet_data(data)
        else:
            return self.csv_manager.save_diet_data(data)
    
    def load_body_metrics(self):
        """Load body metrics data"""
        if self.use_sheets:
            return self.sheets_manager.load_body_metrics()
        else:
            return self.csv_manager.load_body_metrics()
    
    def load_workout_data(self):
        """Load workout data"""
        if self.use_sheets:
            return self.sheets_manager.load_workout_data()
        else:
            return self.csv_manager.load_workout_data()
    
    def load_diet_data(self):
        """Load diet data"""
        if self.use_sheets:
            return self.sheets_manager.load_diet_data()
        else:
            return self.csv_manager.load_diet_data()
    
    def reset_all_data(self):
        """Reset all data"""
        if self.use_sheets:
            return self.sheets_manager.reset_all_data()
        else:
            return self.csv_manager.reset_all_data()
    
    def get_storage_info(self):
        """Get information about current storage system"""
        if self.use_sheets:
            sheets_info = self.sheets_manager.get_spreadsheet_info()
            if sheets_info:
                return {
                    'storage_type': 'Google Sheets',
                    'location': sheets_info['url'],
                    'title': sheets_info['title'],
                    'worksheets': sheets_info['worksheets']
                }
            else:
                return {'storage_type': 'Google Sheets', 'status': 'Connection failed'}
        else:
            csv_info = self.csv_manager.get_data_file_info()
            return {
                'storage_type': 'Local CSV Files',
                'location': csv_info['data_directory'],
                'files': csv_info['files']
            }