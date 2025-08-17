import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from utils.hybrid_manager import HybridManager
from utils.analytics import Analytics
from utils.mobile_nav import add_mobile_header

# Configure page for mobile
st.set_page_config(
    page_title="Progress Analytics - Fitness Tracker",
    page_icon="📈",
    layout="wide"
)

# Mobile enhancements
st.markdown("""
<style>
    @import url('/static/css/mobile_styles.css');
    
    /* Analytics page optimizations */
    .plotly {
        width: 100% !important;
        height: auto !important;
    }
    
    .js-plotly-plot {
        margin: 1rem 0;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    /* Mobile-friendly tabs */
    .stTabs [data-baseweb="tab-list"] {
        overflow-x: auto;
        scrollbar-width: none;
        -ms-overflow-style: none;
    }
    
    .stTabs [data-baseweb="tab-list"]::-webkit-scrollbar {
        display: none;
    }
    
    /* Enhanced metrics grid */
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, #ffffff, #f8f9fa);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 0.75rem 0;
        box-shadow: 0 2px 12px rgba(0,0,0,0.08);
        border-left: 4px solid #4ECDC4;
    }
    
    /* Dataframe styling */
    .dataframe {
        font-size: 0.9rem;
        border-radius: 8px;
        overflow: hidden;
    }
    
    /* Progress indicators */
    .stProgress > div > div {
        border-radius: 8px;
        height: 1rem;
    }
    
    @media (max-width: 768px) {
        .js-plotly-plot {
            height: 300px !important;
        }
        
        /* Stack metrics vertically on mobile */
        [data-testid="column"] {
            margin-bottom: 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Initialize data manager and analytics
data_manager = HybridManager()
analytics = Analytics(data_manager)

def main():
    # Add mobile header with FontAwesome icon
    add_mobile_header("Progress Analytics", "fas fa-chart-line")
    
    # Load data
    body_metrics = data_manager.load_body_metrics()
    workout_data = data_manager.load_workout_data()
    diet_data = data_manager.load_diet_data()
    
    # Check if we have any data
    if body_metrics.empty and workout_data.empty and diet_data.empty:
        st.warning("📊 No data available yet. Start tracking your progress by entering data!")
        if st.button("➕ Enter Data Now"):
            st.switch_page("pages/1_Weekly_Entry.py")
        return
    
    # Progress statistics
    stats = analytics.get_progress_stats()
    
    if stats:
        st.subheader("📊 Progress Summary")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if 'total_weight_change' in stats:
                weight_change = stats['total_weight_change']
                delta_color = "inverse" if weight_change < 0 else "normal"
                st.metric(
                    "Total Weight Change",
                    f"{weight_change:+.1f} kg",
                    delta=f"{weight_change:+.1f} kg",
                    delta_color=delta_color
                )
            else:
                st.metric("Total Weight Change", "No data")
        
        with col2:
            if 'total_fat_change' in stats:
                fat_change = stats['total_fat_change']
                delta_color = "inverse" if fat_change < 0 else "normal"
                st.metric(
                    "Total Fat % Change",
                    f"{fat_change:+.1f}%",
                    delta=f"{fat_change:+.1f}%",
                    delta_color=delta_color
                )
            else:
                st.metric("Total Fat % Change", "No data")
        
        with col3:
            if 'overall_workout_compliance' in stats:
                workout_compliance = stats['overall_workout_compliance']
                st.metric(
                    "Workout Compliance",
                    f"{workout_compliance:.0f}%",
                    delta=f"{workout_compliance - 80:.0f}% vs target" if workout_compliance else None
                )
            else:
                st.metric("Workout Compliance", "No data")
        
        with col4:
            if 'overall_diet_compliance' in stats:
                diet_compliance = stats['overall_diet_compliance']
                st.metric(
                    "Diet Compliance",
                    f"{diet_compliance:.0f}%",
                    delta=f"{diet_compliance - 80:.0f}% vs target" if diet_compliance else None
                )
            else:
                st.metric("Diet Compliance", "No data")
    
    # Charts section
    st.markdown("---")
    
    # Weight and Fat Percentage Charts
    col1, col2 = st.columns(2)
    
    with col1:
        weight_chart = analytics.create_weight_progress_chart()
        if weight_chart:
            st.plotly_chart(weight_chart, use_container_width=True)
        else:
            st.info("📊 Weight chart will appear here once you enter body metrics")
    
    with col2:
        fat_chart = analytics.create_fat_percentage_chart()
        if fat_chart:
            st.plotly_chart(fat_chart, use_container_width=True)
        else:
            st.info("📊 Fat percentage chart will appear here once you enter body metrics")
    
    # Body measurements chart
    measurements_chart = analytics.create_body_measurements_chart()
    if measurements_chart:
        st.plotly_chart(measurements_chart, use_container_width=True)
    
    # Compliance tracking
    compliance_chart = analytics.create_compliance_chart()
    if compliance_chart:
        st.plotly_chart(compliance_chart, use_container_width=True)
    else:
        st.info("📊 Compliance chart will appear here once you enter workout and diet data")
    
    # Workout heatmap
    workout_heatmap = analytics.create_workout_heatmap()
    if workout_heatmap:
        st.plotly_chart(workout_heatmap, use_container_width=True)
    
    # Detailed analytics
    st.markdown("---")
    st.subheader("📋 Detailed Analysis")
    
    tab1, tab2, tab3 = st.tabs(["📊 Weekly Breakdown", "🎯 Goal Tracking", "📈 Trends"])
    
    with tab1:
        if not body_metrics.empty or not workout_data.empty or not diet_data.empty:
            # Get unique weeks
            weeks = set()
            if not body_metrics.empty:
                weeks.update(body_metrics['week'].unique())
            if not workout_data.empty:
                weeks.update(workout_data['week'].unique())
            if not diet_data.empty:
                weeks.update(diet_data['week'].unique())
            
            if weeks:
                selected_week = st.selectbox("Select Week", sorted(weeks, reverse=True))
                
                # Get weekly summary
                weekly_summary = data_manager.get_weekly_summary(selected_week)
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Workout Compliance", f"{weekly_summary['workout_compliance']:.0f}%")
                
                with col2:
                    st.metric("Diet Compliance", f"{weekly_summary['diet_compliance']:.0f}%")
                
                with col3:
                    overall_compliance = (weekly_summary['workout_compliance'] + weekly_summary['diet_compliance']) / 2
                    st.metric("Overall Compliance", f"{overall_compliance:.0f}%")
                
                # Show detailed weekly data
                if not weekly_summary['body_metrics'].empty:
                    st.subheader("Body Metrics This Week")
                    display_metrics = weekly_summary['body_metrics'][['date', 'weight', 'fat_percentage']].copy()
                    display_metrics['date'] = pd.to_datetime(display_metrics['date']).dt.strftime('%Y-%m-%d')
                    st.dataframe(display_metrics, use_container_width=True, hide_index=True)
                
                if not weekly_summary['workout_data'].empty:
                    st.subheader("Workouts This Week")
                    display_workouts = weekly_summary['workout_data'][['date', 'day', 'workout_type', 'completed', 'exercises_completed', 'total_exercises']].copy()
                    display_workouts['date'] = pd.to_datetime(display_workouts['date']).dt.strftime('%Y-%m-%d')
                    display_workouts['completion_rate'] = (display_workouts['exercises_completed'] / display_workouts['total_exercises'] * 100).round(0).astype(str) + '%'
                    st.dataframe(display_workouts, use_container_width=True, hide_index=True)
        else:
            st.info("No weekly data available yet")
    
    with tab2:
        st.markdown("### 🎯 Goal Progress")
        
        # Weight loss goal tracking
        if not body_metrics.empty and len(body_metrics) >= 2:
            start_weight = body_metrics['weight'].iloc[0]
            current_weight = body_metrics['weight'].iloc[-1]
            weight_lost = start_weight - current_weight
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Starting Weight", f"{start_weight:.1f} kg")
                st.metric("Current Weight", f"{current_weight:.1f} kg")
                st.metric("Weight Lost", f"{weight_lost:.1f} kg", delta=f"{weight_lost:.1f} kg")
            
            with col2:
                # Assuming a target of 10% weight loss
                target_weight_loss = start_weight * 0.1
                progress_percentage = (weight_lost / target_weight_loss * 100) if target_weight_loss > 0 else 0
                
                st.metric("Target Weight Loss", f"{target_weight_loss:.1f} kg")
                st.metric("Progress to Goal", f"{progress_percentage:.0f}%")
                
                # Progress bar
                st.progress(min(progress_percentage / 100, 1.0))
        
        # Fat percentage goal tracking
        if not body_metrics.empty and len(body_metrics) >= 2:
            start_fat = body_metrics['fat_percentage'].iloc[0]
            current_fat = body_metrics['fat_percentage'].iloc[-1]
            fat_lost = start_fat - current_fat
            
            st.markdown("### Fat Percentage Goal")
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Starting Fat %", f"{start_fat:.1f}%")
                st.metric("Current Fat %", f"{current_fat:.1f}%")
            
            with col2:
                st.metric("Fat % Reduced", f"{fat_lost:.1f}%", delta=f"{fat_lost:.1f}%")
        
        # Calorie target tracking
        if not diet_data.empty:
            avg_calories = diet_data['calories_estimated'].mean()
            target_calories = 2100  # Middle of 2000-2200 range
            
            st.markdown("### Calorie Target Adherence")
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Average Daily Calories", f"{avg_calories:.0f} kcal")
                st.metric("Target Calories", f"{target_calories} kcal")
            
            with col2:
                calorie_adherence = (1 - abs(avg_calories - target_calories) / target_calories) * 100
                st.metric("Calorie Adherence", f"{calorie_adherence:.0f}%")
    
    with tab3:
        st.markdown("### 📈 Trend Analysis")
        
        if not body_metrics.empty and len(body_metrics) >= 3:
            # Calculate trends
            recent_data = body_metrics.tail(4)  # Last 4 entries
            
            # Weight trend
            weight_trend = recent_data['weight'].pct_change().mean() * 100
            fat_trend = recent_data['fat_percentage'].pct_change().mean() * 100
            
            col1, col2 = st.columns(2)
            
            with col1:
                trend_direction = "📉 Decreasing" if weight_trend < 0 else "📈 Increasing"
                st.metric(
                    "Weight Trend (Recent)",
                    trend_direction,
                    delta=f"{weight_trend:.2f}% change rate"
                )
            
            with col2:
                fat_trend_direction = "📉 Decreasing" if fat_trend < 0 else "📈 Increasing"
                st.metric(
                    "Fat % Trend (Recent)",
                    fat_trend_direction,
                    delta=f"{fat_trend:.2f}% change rate"
                )
            
            # Compliance trends
            if not workout_data.empty and not diet_data.empty:
                # Get weekly compliance data
                weeks = sorted(set(workout_data['week'].unique()) & set(diet_data['week'].unique()))
                
                if len(weeks) >= 2:
                    recent_weeks = weeks[-2:]
                    
                    workout_trend = []
                    diet_trend = []
                    
                    for week in recent_weeks:
                        week_workouts = workout_data[workout_data['week'] == week]
                        week_diet = diet_data[diet_data['week'] == week]
                        
                        if not week_workouts.empty:
                            workout_compliance = (week_workouts['completed'].sum() / len(week_workouts)) * 100
                            workout_trend.append(workout_compliance)
                        
                        if not week_diet.empty:
                            diet_compliance = (week_diet['adherence_score'].mean() / 5) * 100
                            diet_trend.append(diet_compliance)
                    
                    if len(workout_trend) >= 2:
                        workout_change = workout_trend[-1] - workout_trend[-2]
                        workout_trend_dir = "📈 Improving" if workout_change > 0 else "📉 Declining"
                        st.metric(
                            "Workout Compliance Trend",
                            workout_trend_dir,
                            delta=f"{workout_change:+.0f}% vs last week"
                        )
                    
                    if len(diet_trend) >= 2:
                        diet_change = diet_trend[-1] - diet_trend[-2]
                        diet_trend_dir = "📈 Improving" if diet_change > 0 else "📉 Declining"
                        st.metric(
                            "Diet Compliance Trend",
                            diet_trend_dir,
                            delta=f"{diet_change:+.0f}% vs last week"
                        )
        else:
            st.info("Need more data points to show trends. Keep tracking!")
    
    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🏠 Back to Dashboard", use_container_width=True):
            st.switch_page("app.py")
    
    with col2:
        if st.button("📅 Enter Data", use_container_width=True):
            st.switch_page("pages/1_Weekly_Entry.py")
    
    with col3:
        if st.button("📋 View Plan", use_container_width=True):
            st.switch_page("pages/3_Plan_Overview.py")

if __name__ == "__main__":
    main()
    # Add mobile navigation

