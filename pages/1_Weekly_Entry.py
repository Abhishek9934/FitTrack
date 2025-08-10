import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from utils.data_manager import DataManager
from utils.workout_plans import get_weekly_plan
from utils.mobile_nav import render_mobile_navigation, add_mobile_header, add_floating_action_button

# Configure page for mobile
st.set_page_config(
    page_title="Weekly Entry - Fitness Tracker",
    page_icon="📅",
    layout="wide"
)

# Mobile enhancements
st.markdown("""
<style>
    @import url('/static/css/mobile_styles.css');
    
    /* Page-specific mobile optimizations */
    .stTabs [data-baseweb="tab-list"] {
        justify-content: space-around;
        flex-wrap: wrap;
    }
    
    .stTabs [data-baseweb="tab"] {
        min-height: 3rem;
        font-size: 1rem;
        font-weight: 600;
        flex: 1;
        min-width: 120px;
    }
    
    /* Enhanced form styling */
    .stNumberInput > div > div {
        margin-bottom: 1rem;
    }
    
    .stCheckbox {
        margin: 0.5rem 0;
        padding: 0.75rem;
        background: #F8F9FA;
        border-radius: 8px;
        border: 1px solid #E0E0E0;
    }
    
    .stCheckbox:hover {
        background: #E9ECEF;
        border-color: #FF6B6B;
    }
    
    /* Progress bar styling */
    .stProgress {
        margin: 1rem 0;
    }
    
    /* Mobile date picker */
    .stDateInput > div > div > input {
        min-height: 3rem;
        font-size: 1.1rem;
        border-radius: 8px;
    }
    
    /* Section headers */
    h2, h3 {
        color: #2C3E50;
        margin: 1.5rem 0 1rem 0;
    }
    
    /* Info boxes */
    .stAlert {
        border-radius: 8px;
        margin: 1rem 0;
        padding: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize data manager
data_manager = DataManager()

def main():
    # Add mobile header with FontAwesome icon
    add_mobile_header("Weekly Entry", "fas fa-plus-circle")
    
    # Date selection
    col1, col2 = st.columns([1, 2])
    with col1:
        selected_date = st.date_input("Select Date", value=datetime.now().date())
    
    with col2:
        day_name = selected_date.strftime("%A")
        week = selected_date.strftime("%Y-W%U")
        st.info(f"Day: {day_name} | Week: {week}")
    
    # Get weekly plan
    weekly_plan = get_weekly_plan()
    day_plan = weekly_plan.get(day_name, {})
    
    # Create tabs for different entry types
    tab1, tab2, tab3 = st.tabs(["🔢 Body Metrics", "🏋️‍♂️ Workout Tracking", "🍽️ Diet Tracking"])
    
    with tab1:
        st.subheader("Body Measurements")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Essential Metrics**")
            weight = st.number_input("Weight (kg)", min_value=40.0, max_value=200.0, value=70.0, step=0.1)
            fat_percentage = st.number_input("Fat Percentage (%)", min_value=5.0, max_value=50.0, value=15.0, step=0.1)
            muscle_mass = st.number_input("Muscle Mass (kg) - Optional", min_value=20.0, max_value=100.0, value=None, step=0.1)
        
        with col2:
            st.markdown("**Body Measurements (cm) - Optional**")
            chest = st.number_input("Chest", min_value=60.0, max_value=200.0, value=None, step=0.5)
            waist = st.number_input("Waist", min_value=50.0, max_value=150.0, value=None, step=0.5)
            hips = st.number_input("Hips", min_value=60.0, max_value=200.0, value=None, step=0.5)
            arms = st.number_input("Arms", min_value=20.0, max_value=60.0, value=None, step=0.5)
            thighs = st.number_input("Thighs", min_value=30.0, max_value=100.0, value=None, step=0.5)
        
        body_notes = st.text_area("Notes (optional)", placeholder="Any observations, how you're feeling, etc.")
        
        if st.button("💾 Save Body Metrics", type="primary", use_container_width=True):
            success = data_manager.save_body_metrics(
                date=datetime.combine(selected_date, datetime.min.time()),
                weight=weight,
                fat_percentage=fat_percentage,
                muscle_mass=muscle_mass,
                chest=chest,
                waist=waist,
                hips=hips,
                arms=arms,
                thighs=thighs,
                notes=body_notes
            )
            
            if success:
                st.success("✅ Body metrics saved successfully!")
                st.rerun()
            else:
                st.error("❌ Failed to save body metrics")
    
    with tab2:
        st.subheader(f"Workout Tracking - {day_name}")
        
        if day_plan:
            st.info(f"Today's Focus: {day_plan['type']}")
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown("**Planned Exercises:**")
                exercises = day_plan.get('exercises', [])
                
                completed_exercises = []
                for i, exercise in enumerate(exercises):
                    completed = st.checkbox(f"{exercise}", key=f"ex_{i}")
                    if completed:
                        completed_exercises.append(exercise)
                
                total_exercises = len(exercises)
                exercises_completed = len(completed_exercises)
                
                # Calculate completion percentage
                completion_percentage = (exercises_completed / total_exercises) * 100 if total_exercises > 0 else 0
                st.progress(completion_percentage / 100)
                st.write(f"Completed: {exercises_completed}/{total_exercises} exercises ({completion_percentage:.0f}%)")
            
            with col2:
                st.markdown("**Workout Details**")
                workout_completed = st.checkbox("Mark workout as completed")
                duration = st.number_input("Duration (minutes)", min_value=0, max_value=300, value=60)
                intensity = st.selectbox("Intensity Rating", [1, 2, 3, 4, 5], index=2, 
                                        help="1 = Very Easy, 5 = Maximum Effort")
                workout_notes = st.text_area("Workout Notes", placeholder="How did it feel? Any modifications?")
        else:
            st.warning("No specific workout plan found for this day")
            
            # Generic workout entry
            workout_type = st.text_input("Workout Type", placeholder="e.g., Cardio, Custom workout")
            exercises_completed = st.number_input("Exercises Completed", min_value=0, max_value=20, value=0)
            total_exercises = st.number_input("Total Planned Exercises", min_value=1, max_value=20, value=5)
            workout_completed = st.checkbox("Mark workout as completed")
            duration = st.number_input("Duration (minutes)", min_value=0, max_value=300, value=60)
            intensity = st.selectbox("Intensity Rating", [1, 2, 3, 4, 5], index=2)
            workout_notes = st.text_area("Workout Notes", placeholder="Details about your workout")
        
        if st.button("💾 Save Workout Data", type="primary"):
            workout_type = day_plan.get('type', 'Custom Workout') if day_plan else workout_type
            
            success = data_manager.save_workout_data(
                date=datetime.combine(selected_date, datetime.min.time()),
                day=day_name,
                workout_type=workout_type,
                completed=workout_completed,
                exercises_completed=exercises_completed,
                total_exercises=total_exercises if day_plan else total_exercises,
                duration_minutes=duration,
                intensity_rating=intensity,
                notes=workout_notes
            )
            
            if success:
                st.success("✅ Workout data saved successfully!")
                st.rerun()
            else:
                st.error("❌ Failed to save workout data")
    
    with tab3:
        st.subheader(f"Diet Tracking - {day_name}")
        
        if day_plan and 'diet' in day_plan:
            st.info("Today's Meal Plan:")
            diet_plan = day_plan['diet']
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown("**Planned Meals:**")
                for meal_time, meal_content in diet_plan.items():
                    meal_display = meal_time.replace('_', ' ').title()
                    if meal_content != '–':
                        st.write(f"**{meal_display}:** {meal_content}")
                    else:
                        st.write(f"**{meal_display}:** No specific meal planned")
            
            with col2:
                st.markdown("**Diet Adherence**")
                adherence_score = st.selectbox(
                    "How well did you follow the meal plan?",
                    options=[1, 2, 3, 4, 5],
                    index=2,
                    format_func=lambda x: {
                        1: "1 - Poorly (0-20%)",
                        2: "2 - Below Average (20-40%)",
                        3: "3 - Average (40-60%)",
                        4: "4 - Good (60-80%)",
                        5: "5 - Excellent (80-100%)"
                    }[x]
                )
                
                calories_estimated = st.number_input(
                    "Estimated Calories Consumed",
                    min_value=500,
                    max_value=4000,
                    value=2100,
                    step=50,
                    help="Target: 2000-2200 kcal"
                )
                
                meals_followed = st.number_input(
                    "Meals Followed from Plan",
                    min_value=0,
                    max_value=6,
                    value=4
                )
                
                diet_notes = st.text_area(
                    "Diet Notes",
                    placeholder="Any deviations, how you felt, etc."
                )
        else:
            st.warning("No specific diet plan found for this day")
            
            # Generic diet entry
            adherence_score = st.selectbox(
                "Overall Diet Quality Today",
                options=[1, 2, 3, 4, 5],
                index=2,
                format_func=lambda x: {
                    1: "1 - Poor",
                    2: "2 - Below Average",
                    3: "3 - Average",
                    4: "4 - Good",
                    5: "5 - Excellent"
                }[x]
            )
            
            calories_estimated = st.number_input(
                "Estimated Calories Consumed",
                min_value=500,
                max_value=4000,
                value=2100,
                step=50
            )
            
            meals_followed = st.number_input("Healthy Meals Today", min_value=0, max_value=6, value=3)
            diet_notes = st.text_area("Diet Notes")
        
        if st.button("💾 Save Diet Data", type="primary"):
            total_planned_meals = 6  # Breakfast, Mid-morning, Lunch, Pre-workout, Dinner, Snack
            
            success = data_manager.save_diet_data(
                date=datetime.combine(selected_date, datetime.min.time()),
                day=day_name,
                adherence_score=adherence_score,
                calories_estimated=calories_estimated,
                meals_followed=meals_followed,
                total_planned_meals=total_planned_meals,
                notes=diet_notes
            )
            
            if success:
                st.success("✅ Diet data saved successfully!")
                st.rerun()
            else:
                st.error("❌ Failed to save diet data")
    
    # Quick navigation
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🏠 Back to Dashboard", use_container_width=True):
            st.switch_page("app.py")
    
    with col2:
        if st.button("📈 View Analytics", use_container_width=True):
            st.switch_page("pages/2_Progress_Analytics.py")
    
    with col3:
        if st.button("📋 View Plan", use_container_width=True):
            st.switch_page("pages/3_Plan_Overview.py")

if __name__ == "__main__":
    main()
    # Add mobile navigation
    render_mobile_navigation()
