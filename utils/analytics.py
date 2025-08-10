import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta

class Analytics:
    def __init__(self, data_manager):
        self.data_manager = data_manager
    
    def create_weight_progress_chart(self):
        """Create weight progress line chart"""
        body_metrics = self.data_manager.load_body_metrics()
        
        if body_metrics.empty:
            return None
        
        fig = px.line(
            body_metrics, 
            x='date', 
            y='weight',
            title='Weight Progress Over Time',
            markers=True,
            line_shape='spline'
        )
        
        fig.update_layout(
            xaxis_title="Date",
            yaxis_title="Weight (kg)",
            hovermode='x unified'
        )
        
        # Add trend line
        if len(body_metrics) > 1:
            z = np.polyfit(range(len(body_metrics)), body_metrics['weight'], 1)
            trend_line = np.poly1d(z)
            fig.add_trace(
                go.Scatter(
                    x=body_metrics['date'],
                    y=trend_line(range(len(body_metrics))),
                    mode='lines',
                    name='Trend',
                    line=dict(dash='dash', color='red', width=2)
                )
            )
        
        return fig
    
    def create_fat_percentage_chart(self):
        """Create fat percentage progress chart"""
        body_metrics = self.data_manager.load_body_metrics()
        
        if body_metrics.empty:
            return None
        
        fig = px.line(
            body_metrics, 
            x='date', 
            y='fat_percentage',
            title='Fat Percentage Progress Over Time',
            markers=True,
            line_shape='spline',
            color_discrete_sequence=['#FF6B6B']
        )
        
        fig.update_layout(
            xaxis_title="Date",
            yaxis_title="Fat Percentage (%)",
            hovermode='x unified'
        )
        
        # Add trend line
        if len(body_metrics) > 1:
            z = np.polyfit(range(len(body_metrics)), body_metrics['fat_percentage'], 1)
            trend_line = np.poly1d(z)
            fig.add_trace(
                go.Scatter(
                    x=body_metrics['date'],
                    y=trend_line(range(len(body_metrics))),
                    mode='lines',
                    name='Trend',
                    line=dict(dash='dash', color='darkred', width=2)
                )
            )
        
        return fig
    
    def create_body_measurements_chart(self):
        """Create body measurements chart"""
        body_metrics = self.data_manager.load_body_metrics()
        
        if body_metrics.empty:
            return None
        
        # Select measurement columns that have data
        measurement_cols = ['chest', 'waist', 'hips', 'arms', 'thighs']
        available_cols = [col for col in measurement_cols if col in body_metrics.columns and body_metrics[col].notna().any()]
        
        if not available_cols:
            return None
        
        fig = go.Figure()
        
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
        
        for i, col in enumerate(available_cols):
            fig.add_trace(
                go.Scatter(
                    x=body_metrics['date'],
                    y=body_metrics[col],
                    mode='lines+markers',
                    name=col.title(),
                    line=dict(color=colors[i % len(colors)], width=2),
                    marker=dict(size=6)
                )
            )
        
        fig.update_layout(
            title='Body Measurements Progress',
            xaxis_title="Date",
            yaxis_title="Measurement (cm)",
            hovermode='x unified',
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        
        return fig
    
    def create_compliance_chart(self):
        """Create weekly compliance chart"""
        workout_data = self.data_manager.load_workout_data()
        diet_data = self.data_manager.load_diet_data()
        
        if workout_data.empty and diet_data.empty:
            return None
        
        # Calculate weekly compliance
        compliance_data = []
        
        # Get all weeks from both datasets
        weeks = set()
        if not workout_data.empty:
            weeks.update(workout_data['week'].unique())
        if not diet_data.empty:
            weeks.update(diet_data['week'].unique())
        
        for week in sorted(weeks):
            week_data = {'week': week}
            
            # Workout compliance
            week_workouts = workout_data[workout_data['week'] == week] if not workout_data.empty else pd.DataFrame()
            if not week_workouts.empty:
                week_data['workout_compliance'] = (week_workouts['completed'].sum() / len(week_workouts)) * 100
            else:
                week_data['workout_compliance'] = 0
            
            # Diet compliance
            week_diet = diet_data[diet_data['week'] == week] if not diet_data.empty else pd.DataFrame()
            if not week_diet.empty:
                week_data['diet_compliance'] = (week_diet['adherence_score'].mean() / 5) * 100
            else:
                week_data['diet_compliance'] = 0
            
            compliance_data.append(week_data)
        
        if not compliance_data:
            return None
        
        compliance_df = pd.DataFrame(compliance_data)
        
        fig = go.Figure()
        
        fig.add_trace(
            go.Scatter(
                x=compliance_df['week'],
                y=compliance_df['workout_compliance'],
                mode='lines+markers',
                name='Workout Compliance',
                line=dict(color='#4ECDC4', width=3),
                marker=dict(size=8)
            )
        )
        
        fig.add_trace(
            go.Scatter(
                x=compliance_df['week'],
                y=compliance_df['diet_compliance'],
                mode='lines+markers',
                name='Diet Compliance',
                line=dict(color='#FF6B6B', width=3),
                marker=dict(size=8)
            )
        )
        
        # Add 80% target line
        fig.add_hline(y=80, line_dash="dash", line_color="gray", 
                     annotation_text="80% Target")
        
        fig.update_layout(
            title='Weekly Compliance Tracking',
            xaxis_title="Week",
            yaxis_title="Compliance (%)",
            hovermode='x unified',
            yaxis=dict(range=[0, 100])
        )
        
        return fig
    
    def create_workout_heatmap(self):
        """Create workout completion heatmap"""
        workout_data = self.data_manager.load_workout_data()
        
        if workout_data.empty:
            return None
        
        # Create a pivot table for the heatmap
        workout_data['day_of_week'] = workout_data['date'].dt.day_name()
        workout_data['week_start'] = workout_data['date'].dt.to_period('W').dt.start_time
        
        pivot_data = workout_data.pivot_table(
            values='completed',
            index='week_start',
            columns='day_of_week',
            aggfunc='max',
            fill_value=0
        )
        
        # Reorder columns to start with Monday
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        pivot_data = pivot_data.reindex(columns=[day for day in day_order if day in pivot_data.columns])
        
        fig = px.imshow(
            pivot_data,
            title='Workout Completion Heatmap',
            color_continuous_scale='RdYlGn',
            aspect='auto'
        )
        
        fig.update_layout(
            xaxis_title="Day of Week",
            yaxis_title="Week Starting",
        )
        
        return fig
    
    def get_progress_stats(self):
        """Calculate various progress statistics"""
        body_metrics = self.data_manager.load_body_metrics()
        workout_data = self.data_manager.load_workout_data()
        diet_data = self.data_manager.load_diet_data()
        
        stats = {}
        
        if not body_metrics.empty:
            # Weight progress
            if len(body_metrics) >= 2:
                weight_change = body_metrics['weight'].iloc[-1] - body_metrics['weight'].iloc[0]
                fat_change = body_metrics['fat_percentage'].iloc[-1] - body_metrics['fat_percentage'].iloc[0]
                
                stats['total_weight_change'] = weight_change
                stats['total_fat_change'] = fat_change
                
                # Calculate average weekly change
                weeks_tracked = len(body_metrics)
                stats['avg_weekly_weight_change'] = weight_change / max(weeks_tracked, 1)
                stats['avg_weekly_fat_change'] = fat_change / max(weeks_tracked, 1)
            
            stats['total_entries'] = len(body_metrics)
            stats['tracking_start_date'] = body_metrics['date'].min()
            stats['last_entry_date'] = body_metrics['date'].max()
        
        if not workout_data.empty:
            stats['total_workouts_completed'] = workout_data['completed'].sum()
            stats['total_workouts_planned'] = len(workout_data)
            stats['overall_workout_compliance'] = (stats['total_workouts_completed'] / stats['total_workouts_planned']) * 100
        
        if not diet_data.empty:
            stats['avg_diet_adherence'] = diet_data['adherence_score'].mean()
            stats['overall_diet_compliance'] = (stats['avg_diet_adherence'] / 5) * 100
        
        return stats
    
    def create_summary_dashboard(self):
        """Create a comprehensive summary dashboard"""
        body_metrics = self.data_manager.load_body_metrics()
        
        if body_metrics.empty:
            return None
        
        # Create subplots
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Weight Progress', 'Fat Percentage', 'Weekly Weight Change', 'Body Measurements'),
            specs=[[{"secondary_y": False}, {"secondary_y": False}],
                   [{"secondary_y": False}, {"secondary_y": False}]]
        )
        
        # Weight progress
        fig.add_trace(
            go.Scatter(x=body_metrics['date'], y=body_metrics['weight'],
                      mode='lines+markers', name='Weight', line=dict(color='#4ECDC4')),
            row=1, col=1
        )
        
        # Fat percentage
        fig.add_trace(
            go.Scatter(x=body_metrics['date'], y=body_metrics['fat_percentage'],
                      mode='lines+markers', name='Fat %', line=dict(color='#FF6B6B')),
            row=1, col=2
        )
        
        # Weekly weight change
        if len(body_metrics) > 1:
            body_metrics_sorted = body_metrics.sort_values('date')
            body_metrics_sorted['weight_change'] = body_metrics_sorted['weight'].diff()
            
            fig.add_trace(
                go.Bar(x=body_metrics_sorted['date'], y=body_metrics_sorted['weight_change'],
                      name='Weekly Change', marker_color='#96CEB4'),
                row=2, col=1
            )
        
        # Body measurements (if available)
        measurement_cols = ['chest', 'waist', 'hips']
        for i, col in enumerate(measurement_cols):
            if col in body_metrics.columns and body_metrics[col].notna().any():
                fig.add_trace(
                    go.Scatter(x=body_metrics['date'], y=body_metrics[col],
                              mode='lines+markers', name=col.title()),
                    row=2, col=2
                )
        
        fig.update_layout(height=600, title_text="Fitness Progress Summary Dashboard")
        
        return fig
