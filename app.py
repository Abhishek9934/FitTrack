import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import os
from utils.data_manager import DataManager
from utils.analytics import Analytics
from utils.mobile_nav import add_mobile_header

# Configure page for mobile-first PWA
st.set_page_config(
    page_title="Fitness Progress Tracker",
    page_icon="🏋️‍♂️",
    layout="wide",
    initial_sidebar_state="auto"
)

# Inject mobile-first CSS and PWA features
def inject_mobile_enhancements():
    st.markdown("""
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes, viewport-fit=cover">
    <meta name="theme-color" content="#FF6B6B">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="default">
    <meta name="apple-mobile-web-app-title" content="Fitness Tracker">
    <link rel="manifest" href="/static/manifest.json">
    <link rel="apple-touch-icon" href="/static/icons/icon-192x192.png">
    
    <style>
        /* Import mobile styles */
        @import url('/static/css/mobile_styles.css');
        
        /* Additional mobile optimizations */
        .main .block-container {
            padding: 1rem 0.75rem;
            max-width: 100%;
        }
        
        /* Mobile-first button styling */
        .stButton > button {
            min-height: 3.5rem;
            font-size: 1.1rem;
            font-weight: 600;
            border-radius: 12px;
            margin: 0.5rem 0;
            transition: all 0.3s ease;
        }
        
        .stButton > button:active {
            transform: scale(0.98);
        }
        
        /* Enhanced metrics for mobile */
        [data-testid="metric-container"] {
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 2px 12px rgba(0,0,0,0.08);
            border: 1px solid #E8E8E8;
            margin: 0.75rem 0;
        }
        
        /* Mobile navigation */
        .css-1d391kg {
            padding: 1rem;
        }
        
        /* Input styling for mobile */
        .stNumberInput input, .stTextInput input, .stSelectbox select {
            min-height: 3rem;
            font-size: 1.1rem;
            border-radius: 8px;
            border: 2px solid #E0E0E0;
            padding: 0.75rem;
        }
        
        .stNumberInput input:focus, .stTextInput input:focus {
            border-color: #FF6B6B;
            box-shadow: 0 0 0 3px rgba(255, 107, 107, 0.1);
        }
        
        /* Mobile sidebar adjustments */
        .css-1lcbmhc .css-17eq0hr h2 {
            font-size: 1.2rem;
            margin-bottom: 1rem;
        }
        
        /* Responsive columns */
        @media (max-width: 768px) {
            .row-widget.stHorizontal > div {
                flex: 1 1 100% !important;
                margin-bottom: 1rem;
            }
        }
        
        /* Touch feedback */
        button:active, .stCheckbox label:active {
            transform: scale(0.98);
            transition: transform 0.1s;
        }
        
        /* Enhanced table styling */
        .dataframe {
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        
        /* Quick stats styling */
        .metric-container {
            background: linear-gradient(135deg, #ffffff, #f8f9fa);
            border-left: 4px solid #FF6B6B;
            border-radius: 12px;
            padding: 1.5rem;
            margin: 0.75rem 0;
            box-shadow: 0 2px 12px rgba(0,0,0,0.08);
        }
    </style>
    
    <script src="/static/js/mobile_enhancements.js"></script>
    """, unsafe_allow_html=True)

inject_mobile_enhancements()

# Initialize data manager
data_manager = DataManager()

def main():
    # Add mobile header with FontAwesome icon
    add_mobile_header("Fitness Tracker", "fas fa-dumbbell")
    
    # PWA Installation prompt
    st.markdown("""
    <div style="background: linear-gradient(135deg, #4ECDC4, #44A08D); color: white; padding: 1rem; 
                border-radius: 12px; margin: 1rem 0; text-align: center;">
        <strong>📱 Install as Mobile App</strong><br>
        <small>Add to your phone's home screen for the best experience!</small><br>
        <small>Safari: Share → Add to Home Screen</small>
    </div>
    """, unsafe_allow_html=True)
    
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
    
    # Main dashboard with mobile-friendly cards
    st.markdown("""
    <div style="background: white; border-radius: 16px; padding: 1.5rem; margin: 1rem 0; 
                box-shadow: 0 4px 16px rgba(0,0,0,0.1); border-left: 6px solid #FF6B6B;">
        <h3 style="color: #2C3E50; margin: 0 0 1rem 0;">📅 Current Week Progress</h3>
    </div>
    """, unsafe_allow_html=True)
    
    current_week = datetime.now().strftime("%Y-W%U")
    st.info(f"📆 Week: {current_week}")
    
    # Show current week's plan in a mobile-friendly format
    from utils.workout_plans import get_weekly_plan
    weekly_plan = get_weekly_plan()
    
    # Create workout progress cards
    for day, plan in weekly_plan.items():
        completed_workouts = workout_data[
            (workout_data['week'] == current_week) & 
            (workout_data['day'] == day) & 
            (workout_data['completed'] == True)
        ] if not workout_data.empty else pd.DataFrame()
        
        status = "✅" if not completed_workouts.empty else "⭕"
        status_color = "#4ECDC4" if not completed_workouts.empty else "#E0E0E0"
        
        st.markdown(f"""
        <div style="background: white; border-radius: 12px; padding: 1rem; margin: 0.5rem 0; 
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1); border-left: 4px solid {status_color};">
            <strong>{status} {day}</strong><br>
            <small style="color: #666;">{plan['type']}</small>
        </div>
        """, unsafe_allow_html=True)
    
    # Progress metrics section
    st.markdown("""
    <div style="background: white; border-radius: 16px; padding: 1.5rem; margin: 1.5rem 0; 
                box-shadow: 0 4px 16px rgba(0,0,0,0.1); border-left: 6px solid #4ECDC4;">
        <h3 style="color: #2C3E50; margin: 0 0 1rem 0;">📈 Recent Progress</h3>
    </div>
    """, unsafe_allow_html=True)
    
    if not body_metrics.empty and len(body_metrics) >= 2:
        recent_data = body_metrics.tail(2)
        weight_change = recent_data['weight'].iloc[-1] - recent_data['weight'].iloc[-2]
        fat_change = recent_data['fat_percentage'].iloc[-1] - recent_data['fat_percentage'].iloc[-2]
        
        weight_color = "inverse" if weight_change < 0 else "normal"
        fat_color = "inverse" if fat_change < 0 else "normal"
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric(
                "Weight Change", 
                f"{weight_change:+.1f} kg",
                delta=f"{weight_change:+.1f} kg",
                delta_color=weight_color
            )
        with col2:
            st.metric(
                "Fat % Change", 
                f"{fat_change:+.1f}%",
                delta=f"{fat_change:+.1f}%",
                delta_color=fat_color
            )
    else:
        st.info("Need at least 2 entries to show progress")
    
    # Goals section
    st.markdown("""
    <div style="background: white; border-radius: 16px; padding: 1.5rem; margin: 1.5rem 0; 
                box-shadow: 0 4px 16px rgba(0,0,0,0.1); border-left: 6px solid #FF8E53;">
        <h3 style="color: #2C3E50; margin: 0 0 1rem 0;">🎯 Goals & Targets</h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
            <div>
                <strong>Daily Targets:</strong><br>
                <small>• Calories: 2,000-2,200 kcal<br>
                • Protein: 170-180g<br>
                • Carbs: 180-200g<br>
                • Fat: 55-65g</small>
            </div>
            <div>
                <strong>Weekly Goals:</strong><br>
                <small>• Complete all 7 workouts<br>
                • 80%+ diet adherence<br>
                • Consistent weight tracking</small>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
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
    
    # Quick action buttons - Mobile-first design
    st.markdown("""
    <div style="background: white; border-radius: 16px; padding: 1.5rem; margin: 1.5rem 0; 
                box-shadow: 0 4px 16px rgba(0,0,0,0.1); border-left: 6px solid #96CEB4;">
        <h3 style="color: #2C3E50; margin: 0 0 1rem 0;">⚡ Quick Actions</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Mobile-optimized action buttons
    if st.button("📊 Enter Today's Metrics", key="metrics_btn", use_container_width=True):
        st.switch_page("pages/1_Weekly_Entry.py")
    
    if st.button("📈 View Progress Analytics", key="analytics_btn", use_container_width=True):
        st.switch_page("pages/2_Progress_Analytics.py")
    
    if st.button("📋 View Workout & Diet Plan", key="plan_btn", use_container_width=True):
        st.switch_page("pages/3_Plan_Overview.py")
    
    # Data Management Section
    st.markdown("---")
    st.subheader("🗂️ Data Management")
    
    # Show data storage information
    data_info = data_manager.get_data_file_info()
    
    with st.expander("📍 Data Storage Information"):
        st.write(f"**Data Directory:** `{data_info['data_directory']}`")
        st.write("**Data Files:**")
        
        for file_info in data_info['files']:
            col1, col2, col3 = st.columns([2, 1, 1])
            with col1:
                st.write(f"• **{file_info['name']}** - {file_info['description']}")
            with col2:
                st.write(f"{file_info['row_count']} records")
            with col3:
                st.write(f"{file_info['size_bytes']} bytes")
    
    # Export and Reset functionality
    col1, col2 = st.columns(2)
    
    with col1:
        # Export functionality
        if not body_metrics.empty or not workout_data.empty or not diet_data.empty:
            if st.button("📤 Export All Data", key="export_btn", use_container_width=True):
                if not body_metrics.empty:
                    csv = body_metrics.to_csv(index=False)
                    st.download_button(
                        label="📥 Download Body Metrics CSV",
                        data=csv,
                        file_name=f"fitness_progress_{datetime.now().strftime('%Y%m%d')}.csv",
                        mime="text/csv",
                        use_container_width=True
                    )
                else:
                    st.warning("No data to export yet!")
        else:
            st.info("📝 Start tracking to enable data export")
    
    with col2:
        # Reset data functionality with session state
        if 'show_reset_confirm' not in st.session_state:
            st.session_state.show_reset_confirm = False
        
        if not st.session_state.show_reset_confirm:
            if st.button("🗑️ Reset All Data", key="reset_btn", use_container_width=True, type="secondary"):
                st.session_state.show_reset_confirm = True
                st.rerun()
        else:
            st.warning("⚠️ This will permanently delete all your fitness data!")
            
            col_confirm, col_cancel = st.columns(2)
            with col_confirm:
                if st.button("✅ Confirm Reset", key="confirm_reset", use_container_width=True):
                    with st.spinner("Resetting all data..."):
                        if data_manager.reset_all_data():
                            # Clear any cached data in session state
                            for key in list(st.session_state.keys()):
                                if key.startswith(('body_', 'workout_', 'diet_')):
                                    del st.session_state[key]
                            
                            st.session_state.show_reset_confirm = False
                            st.success("✅ All data has been reset successfully!")
                            st.info("🔄 Refreshing the app...")
                            st.balloons()
                            st.rerun()
                        else:
                            st.error("❌ Failed to reset data. Please try again.")
            
            with col_cancel:
                if st.button("❌ Cancel", key="cancel_reset", use_container_width=True):
                    st.session_state.show_reset_confirm = False
                    st.rerun()

if __name__ == "__main__":
    inject_mobile_enhancements()
    main()
