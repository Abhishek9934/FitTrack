import pandas as pd
import os
from datetime import datetime

class DataManager:
    def __init__(self):
        self.data_dir = "data"
        self.ensure_data_directory()
        
        # File paths
        self.body_metrics_file = os.path.join(self.data_dir, "body_metrics.csv")
        self.workout_data_file = os.path.join(self.data_dir, "workout_data.csv")
        self.diet_data_file = os.path.join(self.data_dir, "diet_data.csv")
        
        # Initialize files if they don't exist
        self.initialize_files()
    
    def ensure_data_directory(self):
        """Create data directory if it doesn't exist"""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
    
    def initialize_files(self):
        """Initialize CSV files with headers if they don't exist"""
        
        # Body metrics file
        if not os.path.exists(self.body_metrics_file):
            body_metrics_df = pd.DataFrame(columns=[
                'date', 'week', 'weight', 'fat_percentage', 'muscle_mass',
                'chest', 'waist', 'hips', 'arms', 'thighs', 'notes'
            ])
            body_metrics_df.to_csv(self.body_metrics_file, index=False)
        
        # Workout data file
        if not os.path.exists(self.workout_data_file):
            workout_df = pd.DataFrame(columns=[
                'date', 'week', 'day', 'workout_type', 'completed',
                'exercises_completed', 'total_exercises', 'duration_minutes',
                'intensity_rating', 'notes'
            ])
            workout_df.to_csv(self.workout_data_file, index=False)
        
        # Diet data file
        if not os.path.exists(self.diet_data_file):
            diet_df = pd.DataFrame(columns=[
                'date', 'week', 'day', 'adherence_score', 'calories_estimated',
                'meals_followed', 'total_planned_meals', 'notes'
            ])
            diet_df.to_csv(self.diet_data_file, index=False)
    
    def load_body_metrics(self):
        """Load body metrics data"""
        try:
            df = pd.read_csv(self.body_metrics_file)
            if not df.empty:
                df['date'] = pd.to_datetime(df['date'])
            return df
        except Exception as e:
            print(f"Error loading body metrics: {e}")
            return pd.DataFrame()
    
    def load_workout_data(self):
        """Load workout data"""
        try:
            df = pd.read_csv(self.workout_data_file)
            if not df.empty:
                df['date'] = pd.to_datetime(df['date'])
            return df
        except Exception as e:
            print(f"Error loading workout data: {e}")
            return pd.DataFrame()
    
    def load_diet_data(self):
        """Load diet data"""
        try:
            df = pd.read_csv(self.diet_data_file)
            if not df.empty:
                df['date'] = pd.to_datetime(df['date'])
            return df
        except Exception as e:
            print(f"Error loading diet data: {e}")
            return pd.DataFrame()
    
    def save_body_metrics(self, date, weight, fat_percentage, muscle_mass=None,
                         chest=None, waist=None, hips=None, arms=None, thighs=None, notes=""):
        """Save body metrics data"""
        try:
            df = self.load_body_metrics()
            week = date.strftime("%Y-W%U")
            
            new_row = {
                'date': date,
                'week': week,
                'weight': weight,
                'fat_percentage': fat_percentage,
                'muscle_mass': muscle_mass,
                'chest': chest,
                'waist': waist,
                'hips': hips,
                'arms': arms,
                'thighs': thighs,
                'notes': notes
            }
            
            # Check if entry for this date already exists
            if not df.empty and 'date' in df.columns:
                df['date'] = pd.to_datetime(df['date'])
                existing_entry = df[df['date'].dt.date == date.date()]
                if not existing_entry.empty:
                    # Update existing entry
                    for col, value in new_row.items():
                        df.loc[df['date'].dt.date == date.date(), col] = value
                else:
                    # Add new entry
                    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            else:
                # Add new entry
                df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            
            df.to_csv(self.body_metrics_file, index=False)
            return True
        except Exception as e:
            print(f"Error saving body metrics: {e}")
            return False
    
    def save_workout_data(self, date, day, workout_type, completed, exercises_completed,
                         total_exercises, duration_minutes=None, intensity_rating=None, notes=""):
        """Save workout data"""
        try:
            df = self.load_workout_data()
            week = date.strftime("%Y-W%U")
            
            new_row = {
                'date': date,
                'week': week,
                'day': day,
                'workout_type': workout_type,
                'completed': completed,
                'exercises_completed': exercises_completed,
                'total_exercises': total_exercises,
                'duration_minutes': duration_minutes,
                'intensity_rating': intensity_rating,
                'notes': notes
            }
            
            # Check if entry for this date and workout already exists
            if not df.empty and 'date' in df.columns:
                df['date'] = pd.to_datetime(df['date'])
                existing_entry = df[(df['date'].dt.date == date.date()) & (df['day'] == day)]
                if not existing_entry.empty:
                    # Update existing entry
                    for col, value in new_row.items():
                        df.loc[(df['date'].dt.date == date.date()) & (df['day'] == day), col] = value
                else:
                    # Add new entry
                    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            else:
                # Add new entry
                df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            
            df.to_csv(self.workout_data_file, index=False)
            return True
        except Exception as e:
            print(f"Error saving workout data: {e}")
            return False
    
    def save_diet_data(self, date, day, adherence_score, calories_estimated=None,
                      meals_followed=None, total_planned_meals=None, notes=""):
        """Save diet data"""
        try:
            df = self.load_diet_data()
            week = date.strftime("%Y-W%U")
            
            new_row = {
                'date': date,
                'week': week,
                'day': day,
                'adherence_score': adherence_score,
                'calories_estimated': calories_estimated,
                'meals_followed': meals_followed,
                'total_planned_meals': total_planned_meals,
                'notes': notes
            }
            
            # Check if entry for this date already exists
            if not df.empty and 'date' in df.columns:
                df['date'] = pd.to_datetime(df['date'])
                existing_entry = df[(df['date'].dt.date == date.date()) & (df['day'] == day)]
                if not existing_entry.empty:
                    # Update existing entry
                    for col, value in new_row.items():
                        df.loc[(df['date'].dt.date == date.date()) & (df['day'] == day), col] = value
                else:
                    # Add new entry
                    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            else:
                # Add new entry
                df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            
            df.to_csv(self.diet_data_file, index=False)
            return True
        except Exception as e:
            print(f"Error saving diet data: {e}")
            return False
    
    def get_weekly_summary(self, week):
        """Get summary data for a specific week"""
        body_metrics = self.load_body_metrics()
        workout_data = self.load_workout_data()
        diet_data = self.load_diet_data()
        
        summary = {
            'week': week,
            'body_metrics': body_metrics[body_metrics['week'] == week] if not body_metrics.empty else pd.DataFrame(),
            'workout_data': workout_data[workout_data['week'] == week] if not workout_data.empty else pd.DataFrame(),
            'diet_data': diet_data[diet_data['week'] == week] if not diet_data.empty else pd.DataFrame()
        }
        
        # Calculate compliance scores
        if not summary['workout_data'].empty:
            summary['workout_compliance'] = (summary['workout_data']['completed'].sum() / len(summary['workout_data'])) * 100
        else:
            summary['workout_compliance'] = 0
        
        if not summary['diet_data'].empty:
            summary['diet_compliance'] = (summary['diet_data']['adherence_score'].mean() / 5) * 100
        else:
            summary['diet_compliance'] = 0
        
        return summary
    
    def reset_all_data(self):
        """Reset all data by recreating empty CSV files"""
        try:
            # Remove existing files
            if os.path.exists(self.body_metrics_file):
                os.remove(self.body_metrics_file)
            if os.path.exists(self.workout_data_file):
                os.remove(self.workout_data_file)
            if os.path.exists(self.diet_data_file):
                os.remove(self.diet_data_file)
            
            # Recreate empty files with headers
            self.initialize_files()
            return True
        except Exception as e:
            print(f"Error resetting data: {e}")
            return False
    
    def get_data_file_info(self):
        """Get information about data files"""
        info = {
            'data_directory': os.path.abspath(self.data_dir),
            'files': []
        }
        
        files_info = [
            ('body_metrics.csv', self.body_metrics_file, 'Body measurements and metrics'),
            ('workout_data.csv', self.workout_data_file, 'Workout completion and progress'),
            ('diet_data.csv', self.diet_data_file, 'Diet adherence and nutrition tracking')
        ]
        
        for name, path, description in files_info:
            if os.path.exists(path):
                file_size = os.path.getsize(path)
                # Count rows (subtract 1 for header)
                try:
                    df = pd.read_csv(path)
                    row_count = len(df)
                except:
                    row_count = 0
                
                info['files'].append({
                    'name': name,
                    'path': os.path.abspath(path),
                    'description': description,
                    'size_bytes': file_size,
                    'row_count': row_count
                })
            else:
                info['files'].append({
                    'name': name,
                    'path': os.path.abspath(path),
                    'description': description,
                    'size_bytes': 0,
                    'row_count': 0
                })
        
        return info
