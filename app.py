import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import os
from utils.data_manager import DataManager
from utils.analytics import Analytics

# Configure page
st.set_page_config(
    page_title="Fitness Progress Tracker",
    page_icon="🏋️‍♂️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize data manager
data_manager = DataManager()

def main():
    st.title("🏋️‍♂️ Fitness Progress Tracker")
    st.markdown("Track your 7-day workout and diet plan progress")
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    st.sidebar.markdown("---")
    
    # Quick stats in sidebar
    st.sidebar.subheader("📊 Quick Stats")
    
    # Load recent data for quick stats
    body_metrics = data_manager.load_body_metrics()
    workout_data = data_manager.load_workout_data()
    diet_data = data_manager.load_diet_data()
    
    if not body_metrics.empty:
        latest_weight = body_metrics['weight'].iloc[-1]
        latest_fat_pct = body_metrics['fat_percentage'].iloc[-1]
        st.sidebar.metric("Current Weight", f"{latest_weight} kg")
        st.sidebar.metric("Current Fat %", f"{latest_fat_pct}%")
        
        # Calculate week compliance
        current_week = datetime.now().strftime("%Y-W%U")
        week_workouts = workout_data[workout_data['week'] == current_week] if not workout_data.empty else pd.DataFrame()
        week_diet = diet_data[diet_data['week'] == current_week] if not diet_data.empty else pd.DataFrame()
        
        if not week_workouts.empty:
            workout_compliance = (week_workouts['completed'].sum() / len(week_workouts)) * 100
            st.sidebar.metric("This Week's Workout Compliance", f"{workout_compliance:.0f}%")
        
        if not week_diet.empty:
            diet_compliance = week_diet['adherence_score'].mean() * 20  # Convert 1-5 scale to percentage
            st.sidebar.metric("This Week's Diet Compliance", f"{diet_compliance:.0f}%")
    else:
        st.sidebar.info("No data yet. Start tracking your progress!")
    
    # Main dashboard
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("📅 Current Week Progress")
        current_week = datetime.now().strftime("%Y-W%U")
        st.write(f"Week: {current_week}")
        
        # Show current week's plan
        from utils.workout_plans import get_weekly_plan
        weekly_plan = get_weekly_plan()
        
        st.write("**This Week's Focus:**")
        for day, plan in weekly_plan.items():
            completed_workouts = workout_data[
                (workout_data['week'] == current_week) & 
                (workout_data['day'] == day) & 
                (workout_data['completed'] == True)
            ] if not workout_data.empty else pd.DataFrame()
            
            status = "✅" if not completed_workouts.empty else "⭕"
            st.write(f"{status} {day}: {plan['type']}")
    
    with col2:
        st.subheader("📈 Recent Progress")
        if not body_metrics.empty and len(body_metrics) >= 2:
            recent_data = body_metrics.tail(2)
            weight_change = recent_data['weight'].iloc[-1] - recent_data['weight'].iloc[-2]
            fat_change = recent_data['fat_percentage'].iloc[-1] - recent_data['fat_percentage'].iloc[-2]
            
            weight_color = "inverse" if weight_change < 0 else "normal"
            fat_color = "inverse" if fat_change < 0 else "normal"
            
            st.metric(
                "Weight Change (Last Entry)", 
                f"{weight_change:+.1f} kg",
                delta=f"{weight_change:+.1f} kg",
                delta_color=weight_color
            )
            st.metric(
                "Fat % Change (Last Entry)", 
                f"{fat_change:+.1f}%",
                delta=f"{fat_change:+.1f}%",
                delta_color=fat_color
            )
        else:
            st.info("Need at least 2 entries to show progress")
    
    with col3:
        st.subheader("🎯 Goals & Targets")
        st.write("**Daily Targets:**")
        st.write("• Calories: 2,000-2,200 kcal")
        st.write("• Protein: 170-180g")
        st.write("• Carbs: 180-200g")
        st.write("• Fat: 55-65g")
        
        st.write("**Weekly Goals:**")
        st.write("• Complete all 7 workouts")
        st.write("• 80%+ diet adherence")
        st.write("• Consistent weight tracking")
    
    # Recent entries
    st.markdown("---")
    st.subheader("📋 Recent Entries")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Last 5 Body Measurements:**")
        if not body_metrics.empty:
            recent_metrics = body_metrics.tail(5)[['date', 'weight', 'fat_percentage']].copy()
            recent_metrics['date'] = pd.to_datetime(recent_metrics['date']).dt.strftime('%Y-%m-%d')
            st.dataframe(recent_metrics, use_container_width=True, hide_index=True)
        else:
            st.info("No body metrics recorded yet")
    
    with col2:
        st.write("**Recent Workout Completions:**")
        if not workout_data.empty:
            recent_workouts = workout_data[workout_data['completed'] == True].tail(5)[['date', 'day', 'workout_type']].copy()
            recent_workouts['date'] = pd.to_datetime(recent_workouts['date']).dt.strftime('%Y-%m-%d')
            st.dataframe(recent_workouts, use_container_width=True, hide_index=True)
        else:
            st.info("No workouts completed yet")
    
    # Quick action buttons
    st.markdown("---")
    st.subheader("⚡ Quick Actions")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("📊 Enter Today's Metrics", use_container_width=True):
            st.switch_page("pages/1_Weekly_Entry.py")
    
    with col2:
        if st.button("📈 View Analytics", use_container_width=True):
            st.switch_page("pages/2_Progress_Analytics.py")
    
    with col3:
        if st.button("📋 View Plan Details", use_container_width=True):
            st.switch_page("pages/3_Plan_Overview.py")
    
    with col4:
        if st.button("📤 Export Data", use_container_width=True):
            # Create export functionality
            if not body_metrics.empty or not workout_data.empty or not diet_data.empty:
                with st.spinner("Preparing export..."):
                    # Combine all data for export
                    export_data = {
                        'body_metrics': body_metrics,
                        'workout_data': workout_data,
                        'diet_data': diet_data
                    }
                    
                    # Create a download button for CSV
                    if not body_metrics.empty:
                        csv = body_metrics.to_csv(index=False)
                        st.download_button(
                            label="Download Body Metrics CSV",
                            data=csv,
                            file_name=f"fitness_progress_{datetime.now().strftime('%Y%m%d')}.csv",
                            mime="text/csv"
                        )
                    else:
                        st.warning("No data to export yet!")

if __name__ == "__main__":
    main()
