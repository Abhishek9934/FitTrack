import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import json
from datetime import datetime, date
import os

class SheetsManager:
    def __init__(self):
        self.client = None
        self.spreadsheet = None
        self._connect()
    
    def _connect(self):
        """Connect to Google Sheets using service account credentials"""
        try:
            # Get credentials from Streamlit secrets
            if "google_sheets" in st.secrets:
                creds_dict = dict(st.secrets["google_sheets"])
                credentials = Credentials.from_service_account_info(
                    creds_dict,
                    scopes=[
                        "https://www.googleapis.com/auth/spreadsheets",
                        "https://www.googleapis.com/auth/drive"
                    ]
                )
                self.client = gspread.authorize(credentials)
                
                # Get or create spreadsheet
                spreadsheet_url = st.secrets.get("spreadsheet_url", "")
                if spreadsheet_url:
                    self.spreadsheet = self.client.open_by_url(spreadsheet_url)
                else:
                    # Create new spreadsheet
                    self.spreadsheet = self.client.create("Fitness Tracker Data")
                    st.info(f"Created new spreadsheet: {self.spreadsheet.url}")
                    
        except Exception as e:
            st.error(f"Failed to connect to Google Sheets: {str(e)}")
            self.client = None
            self.spreadsheet = None
    
    def is_connected(self):
        """Check if successfully connected to Google Sheets"""
        return self.client is not None and self.spreadsheet is not None
    
    def _get_or_create_worksheet(self, sheet_name, headers):
        """Get existing worksheet or create new one with headers"""
        try:
            worksheet = self.spreadsheet.worksheet(sheet_name)
        except gspread.WorksheetNotFound:
            worksheet = self.spreadsheet.add_worksheet(title=sheet_name, rows=1000, cols=len(headers))
            worksheet.append_row(headers)
        
        return worksheet
    
    def save_body_metrics(self, data):
        """Save body metrics data to Google Sheets"""
        if not self.is_connected():
            return False
        
        try:
            headers = ['date', 'week', 'weight', 'fat_percentage', 'muscle_mass', 
                      'chest', 'waist', 'hips', 'arms', 'thighs', 'notes']
            worksheet = self._get_or_create_worksheet('body_metrics', headers)
            
            # Convert data to list format
            row_data = [
                str(data.get('date', '')),
                str(data.get('week', '')),
                str(data.get('weight', '')),
                str(data.get('fat_percentage', '')),
                str(data.get('muscle_mass', '')),
                str(data.get('chest', '')),
                str(data.get('waist', '')),
                str(data.get('hips', '')),
                str(data.get('arms', '')),
                str(data.get('thighs', '')),
                str(data.get('notes', ''))
            ]
            
            worksheet.append_row(row_data)
            return True
            
        except Exception as e:
            st.error(f"Failed to save body metrics: {str(e)}")
            return False
    
    def save_workout_data(self, data):
        """Save workout data to Google Sheets"""
        if not self.is_connected():
            return False
        
        try:
            headers = ['date', 'week', 'day', 'workout_type', 'completed', 
                      'exercises_completed', 'total_exercises', 'duration_minutes', 
                      'intensity_rating', 'notes']
            worksheet = self._get_or_create_worksheet('workout_data', headers)
            
            row_data = [
                str(data.get('date', '')),
                str(data.get('week', '')),
                str(data.get('day', '')),
                str(data.get('workout_type', '')),
                str(data.get('completed', '')),
                str(data.get('exercises_completed', '')),
                str(data.get('total_exercises', '')),
                str(data.get('duration_minutes', '')),
                str(data.get('intensity_rating', '')),
                str(data.get('notes', ''))
            ]
            
            worksheet.append_row(row_data)
            return True
            
        except Exception as e:
            st.error(f"Failed to save workout data: {str(e)}")
            return False
    
    def save_diet_data(self, data):
        """Save diet data to Google Sheets"""
        if not self.is_connected():
            return False
        
        try:
            headers = ['date', 'week', 'day', 'adherence_score', 'calories_estimated',
                      'meals_followed', 'total_planned_meals', 'notes']
            worksheet = self._get_or_create_worksheet('diet_data', headers)
            
            row_data = [
                str(data.get('date', '')),
                str(data.get('week', '')),
                str(data.get('day', '')),
                str(data.get('adherence_score', '')),
                str(data.get('calories_estimated', '')),
                str(data.get('meals_followed', '')),
                str(data.get('total_planned_meals', '')),
                str(data.get('notes', ''))
            ]
            
            worksheet.append_row(row_data)
            return True
            
        except Exception as e:
            st.error(f"Failed to save diet data: {str(e)}")
            return False
    
    def load_body_metrics(self):
        """Load body metrics data from Google Sheets"""
        if not self.is_connected():
            return pd.DataFrame()
        
        try:
            worksheet = self.spreadsheet.worksheet('body_metrics')
            data = worksheet.get_all_records()
            df = pd.DataFrame(data)
            
            if not df.empty:
                # Convert numeric columns
                numeric_cols = ['weight', 'fat_percentage', 'muscle_mass', 
                               'chest', 'waist', 'hips', 'arms', 'thighs']
                for col in numeric_cols:
                    if col in df.columns:
                        df[col] = pd.to_numeric(df[col], errors='coerce')
                
                # Convert date column
                df['date'] = pd.to_datetime(df['date'], errors='coerce')
            
            return df
            
        except gspread.WorksheetNotFound:
            return pd.DataFrame()
        except Exception as e:
            st.error(f"Failed to load body metrics: {str(e)}")
            return pd.DataFrame()
    
    def load_workout_data(self):
        """Load workout data from Google Sheets"""
        if not self.is_connected():
            return pd.DataFrame()
        
        try:
            worksheet = self.spreadsheet.worksheet('workout_data')
            data = worksheet.get_all_records()
            df = pd.DataFrame(data)
            
            if not df.empty:
                # Convert numeric columns
                numeric_cols = ['exercises_completed', 'total_exercises', 
                               'duration_minutes', 'intensity_rating']
                for col in numeric_cols:
                    if col in df.columns:
                        df[col] = pd.to_numeric(df[col], errors='coerce')
                
                # Convert boolean columns
                if 'completed' in df.columns:
                    df['completed'] = df['completed'].astype(str).str.lower() == 'true'
                
                # Convert date column
                df['date'] = pd.to_datetime(df['date'], errors='coerce')
            
            return df
            
        except gspread.WorksheetNotFound:
            return pd.DataFrame()
        except Exception as e:
            st.error(f"Failed to load workout data: {str(e)}")
            return pd.DataFrame()
    
    def load_diet_data(self):
        """Load diet data from Google Sheets"""
        if not self.is_connected():
            return pd.DataFrame()
        
        try:
            worksheet = self.spreadsheet.worksheet('diet_data')
            data = worksheet.get_all_records()
            df = pd.DataFrame(data)
            
            if not df.empty:
                # Convert numeric columns
                numeric_cols = ['adherence_score', 'calories_estimated', 
                               'meals_followed', 'total_planned_meals']
                for col in numeric_cols:
                    if col in df.columns:
                        df[col] = pd.to_numeric(df[col], errors='coerce')
                
                # Convert date column
                df['date'] = pd.to_datetime(df['date'], errors='coerce')
            
            return df
            
        except gspread.WorksheetNotFound:
            return pd.DataFrame()
        except Exception as e:
            st.error(f"Failed to load diet data: {str(e)}")
            return pd.DataFrame()
    
    def reset_all_data(self):
        """Clear all data from Google Sheets"""
        if not self.is_connected():
            return False
        
        try:
            sheet_names = ['body_metrics', 'workout_data', 'diet_data']
            
            for sheet_name in sheet_names:
                try:
                    worksheet = self.spreadsheet.worksheet(sheet_name)
                    # Clear all data except headers
                    if worksheet.row_count > 1:
                        worksheet.delete_rows(2, worksheet.row_count)
                except gspread.WorksheetNotFound:
                    continue  # Sheet doesn't exist, skip
            
            return True
            
        except Exception as e:
            st.error(f"Failed to reset data: {str(e)}")
            return False
    
    def get_spreadsheet_info(self):
        """Get information about the connected spreadsheet"""
        if not self.is_connected():
            return None
        
        try:
            worksheets = self.spreadsheet.worksheets()
            info = {
                'title': self.spreadsheet.title,
                'url': self.spreadsheet.url,
                'worksheets': []
            }
            
            for ws in worksheets:
                if ws.title in ['body_metrics', 'workout_data', 'diet_data']:
                    row_count = max(0, ws.row_count - 1)  # Subtract header row
                    info['worksheets'].append({
                        'name': ws.title,
                        'rows': row_count
                    })
            
            return info
            
        except Exception as e:
            st.error(f"Failed to get spreadsheet info: {str(e)}")
            return None