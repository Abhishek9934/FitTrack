import streamlit as st
from utils.workout_plans import get_weekly_plan, get_daily_targets, get_exercise_categories
from utils.mobile_nav import render_mobile_navigation, add_mobile_header

# Configure page for mobile
st.set_page_config(
    page_title="Plan Overview - Fitness Tracker",
    page_icon="📋",
    layout="wide"
)

# Mobile enhancements
st.markdown("""
<style>
    @import url('/static/css/mobile_styles.css');
    
    /* Plan overview optimizations */
    .stSelectbox > div > div {
        min-height: 3rem;
        font-size: 1.1rem;
        border-radius: 8px;
    }
    
    /* Enhanced expandable sections */
    .streamlit-expanderHeader {
        background: #F8F9FA;
        border-radius: 8px;
        padding: 1rem;
        font-weight: 600;
        margin: 0.5rem 0;
        border: 1px solid #E0E0E0;
    }
    
    .streamlit-expanderHeader:hover {
        background: #E9ECEF;
        border-color: #FF6B6B;
    }
    
    /* Exercise list styling */
    .exercise-list {
        background: #F8F9FA;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 4px solid #4ECDC4;
    }
    
    /* Meal plan styling */
    .meal-plan {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        border-left: 4px solid #FF6B6B;
    }
    
    /* Mobile-friendly tables */
    .dataframe {
        font-size: 0.85rem;
        overflow-x: auto;
    }
    
    /* Section spacing */
    h3 {
        margin: 1.5rem 0 1rem 0;
        color: #2C3E50;
    }
    
    /* Card-like containers */
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    
    @media (max-width: 768px) {
        /* Mobile table adjustments */
        .dataframe {
            font-size: 0.8rem;
        }
        
        /* Compact sections */
        .streamlit-expanderContent {
            padding: 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Add mobile header
    add_mobile_header("Plan Overview", "📋")
    st.markdown("**Target:** 2,000–2,200 kcal/day | **Macros:** P: 170–180g | C: 180–200g | F: 55–65g")
    
    # Overview tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📅 Weekly Schedule", "🏋️‍♂️ Workout Details", "🍽️ Diet Plan", "🎯 Targets & Goals"])
    
    with tab1:
        st.subheader("📅 Weekly Schedule Overview")
        
        weekly_plan = get_weekly_plan()
        
        # Create a nice overview table
        schedule_data = []
        for day, plan in weekly_plan.items():
            schedule_data.append({
                'Day': day,
                'Workout Type': plan['type'],
                'Exercise Count': len(plan['exercises']),
                'Breakfast': plan['diet']['breakfast'][:50] + '...' if len(plan['diet']['breakfast']) > 50 else plan['diet']['breakfast'],
                'Lunch': plan['diet']['lunch'][:50] + '...' if len(plan['diet']['lunch']) > 50 else plan['diet']['lunch']
            })
        
        st.dataframe(schedule_data, use_container_width=True, hide_index=True)
        
        st.markdown("### 📊 Weekly Distribution")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            workout_types = {}
            for day, plan in weekly_plan.items():
                workout_type = plan['type'].split('(')[0].strip()
                workout_types[workout_type] = workout_types.get(workout_type, 0) + 1
            
            st.markdown("**Workout Types:**")
            for workout_type, count in workout_types.items():
                st.write(f"• {workout_type}: {count} day(s)")
        
        with col2:
            total_exercises = sum(len(plan['exercises']) for plan in weekly_plan.values())
            avg_exercises = total_exercises / 7
            
            st.markdown("**Exercise Volume:**")
            st.write(f"• Total exercises per week: {total_exercises}")
            st.write(f"• Average per day: {avg_exercises:.1f}")
            st.write(f"• Rest days: 0 (Active recovery)")
        
        with col3:
            st.markdown("**Focus Areas:**")
            st.write("• Push movements: 2 days")
            st.write("• Pull movements: 2 days")
            st.write("• Legs: 2 days")
            st.write("• Cardio: 2 days")
            st.write("• Core: Every day")
    
    with tab2:
        st.subheader("🏋️‍♂️ Detailed Workout Plans")
        
        weekly_plan = get_weekly_plan()
        
        # Day selector
        selected_day = st.selectbox("Select Day", list(weekly_plan.keys()))
        
        if selected_day:
            day_plan = weekly_plan[selected_day]
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"### {selected_day} - {day_plan['type']}")
                
                st.markdown("**Exercises:**")
                for i, exercise in enumerate(day_plan['exercises'], 1):
                    st.write(f"{i}. {exercise}")
                
                # Exercise categories
                exercise_categories = get_exercise_categories()
                st.markdown("### 💪 Muscle Groups Targeted")
                
                # Determine which categories this workout hits
                workout_type = day_plan['type'].lower()
                targeted_groups = []
                
                if 'push' in workout_type:
                    targeted_groups.extend(exercise_categories['Push'])
                if 'pull' in workout_type:
                    targeted_groups.extend(exercise_categories['Pull'])
                if 'legs' in workout_type or 'leg' in workout_type:
                    targeted_groups.extend(exercise_categories['Legs'])
                if 'swimming' in workout_type or 'badminton' in workout_type:
                    targeted_groups.extend(exercise_categories['Cardio'])
                if 'core' in workout_type:
                    targeted_groups.extend(exercise_categories['Core'])
                
                # Remove duplicates and display
                targeted_groups = list(set(targeted_groups))
                for group in targeted_groups:
                    st.write(f"• {group}")
            
            with col2:
                st.markdown("### 📊 Workout Stats")
                
                total_exercises = len(day_plan['exercises'])
                estimated_time = 60  # Default estimation
                
                # Estimate time based on workout type
                if 'swimming' in day_plan['type'].lower():
                    estimated_time = 35
                elif 'badminton' in day_plan['type'].lower():
                    estimated_time = 75
                elif 'push' in day_plan['type'].lower() or 'pull' in day_plan['type'].lower():
                    estimated_time = 70
                elif 'legs' in day_plan['type'].lower():
                    estimated_time = 80
                
                st.metric("Total Exercises", total_exercises)
                st.metric("Estimated Duration", f"{estimated_time} min")
                
                # Intensity guidance
                st.markdown("### 🎯 Intensity Guide")
                st.write("**RPE Scale:**")
                st.write("• RPE 7: Could do 3 more reps")
                st.write("• RPE 8: Could do 2 more reps")
                st.write("• RPE 9: Could do 1 more rep")
                
                st.markdown("### ⚠️ Safety Tips")
                st.write("• Warm up properly")
                st.write("• Focus on form over weight")
                st.write("• Rest 2-3 minutes between sets")
                st.write("• Stop if you feel pain")
    
    with tab3:
        st.subheader("🍽️ Indian Diet Plan Details")
        
        weekly_plan = get_weekly_plan()
        daily_targets = get_daily_targets()
        
        # Day selector for diet
        selected_day_diet = st.selectbox("Select Day for Diet", list(weekly_plan.keys()), key="diet_day")
        
        if selected_day_diet:
            day_plan = weekly_plan[selected_day_diet]
            diet_plan = day_plan['diet']
            
            st.markdown(f"### {selected_day_diet} Diet Plan")
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                # Display meals in a nice format
                meal_times = [
                    ('breakfast', 'Breakfast', '🌅'),
                    ('mid_morning', 'Mid-Morning', '☕'),
                    ('lunch', 'Lunch', '🍽️'),
                    ('pre_workout', 'Pre-Workout', '💪'),
                    ('post_workout_dinner', 'Post-Workout Dinner', '🌙'),
                    ('optional_snack', 'Optional Snack', '🍎')
                ]
                
                for meal_key, meal_name, emoji in meal_times:
                    meal_content = diet_plan.get(meal_key, 'Not specified')
                    if meal_content != '–':
                        st.markdown(f"**{emoji} {meal_name}**")
                        st.write(meal_content)
                        st.markdown("")
                    else:
                        st.markdown(f"**{emoji} {meal_name}**")
                        st.write("No specific meal planned")
                        st.markdown("")
            
            with col2:
                st.markdown("### 🎯 Daily Targets")
                st.metric("Calories", f"{daily_targets['calories']['min']}-{daily_targets['calories']['max']} kcal")
                st.metric("Protein", f"{daily_targets['protein']['min']}-{daily_targets['protein']['max']} g")
                st.metric("Carbs", f"{daily_targets['carbs']['min']}-{daily_targets['carbs']['max']} g")
                st.metric("Fat", f"{daily_targets['fat']['min']}-{daily_targets['fat']['max']} g")
                
                st.markdown("### 💡 Diet Tips")
                st.write("• Drink plenty of water")
                st.write("• Eat slowly and mindfully")
                st.write("• Prepare meals in advance")
                st.write("• Include variety in vegetables")
                st.write("• Time post-workout nutrition")
        
        # Macro breakdown section
        st.markdown("---")
        st.subheader("📊 Nutritional Breakdown")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("### 🥩 Protein Sources")
            protein_sources = [
                "Egg whites and whole eggs",
                "Chicken curry",
                "Fish curry",
                "Paneer (cottage cheese)",
                "Dal (lentils)",
                "Whey protein",
                "Soya curry",
                "Curd/Yogurt"
            ]
            for source in protein_sources:
                st.write(f"• {source}")
        
        with col2:
            st.markdown("### 🍞 Carbohydrate Sources")
            carb_sources = [
                "Chapatis (whole wheat)",
                "Sweet potato",
                "Banana",
                "Bread (whole grain)",
                "Rice (occasional)",
                "Vegetables (fibrous carbs)"
            ]
            for source in carb_sources:
                st.write(f"• {source}")
        
        with col3:
            st.markdown("### 🥜 Fat Sources")
            fat_sources = [
                "Peanut butter",
                "Flaxseed",
                "Cooking oils (moderate)",
                "Nuts (portion controlled)",
                "Egg yolks",
                "Fish (omega-3)"
            ]
            for source in fat_sources:
                st.write(f"• {source}")
    
    with tab4:
        st.subheader("🎯 Goals & Success Metrics")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📊 Primary Goals")
            st.write("**Fat Loss:**")
            st.write("• Sustainable weight reduction")
            st.write("• Maintain muscle mass")
            st.write("• Improve body composition")
            st.write("")
            
            st.write("**Fitness Goals:**")
            st.write("• Increase strength and endurance")
            st.write("• Improve cardiovascular health")
            st.write("• Build consistent exercise habits")
            st.write("")
            
            st.write("**Nutrition Goals:**")
            st.write("• Meet daily macro targets")
            st.write("• Develop healthy eating patterns")
            st.write("• Optimize meal timing")
        
        with col2:
            st.markdown("### 📈 Success Metrics")
            st.write("**Weekly Targets:**")
            st.write("• Complete all 7 workouts: 100%")
            st.write("• Diet adherence: 80%+")
            st.write("• Track body metrics: 2x/week")
            st.write("")
            
            st.write("**Monthly Targets:**")
            st.write("• Weight loss: 2-4 kg")
            st.write("• Fat percentage: -2-3%")
            st.write("• Strength improvement: Progressive")
            st.write("")
            
            st.write("**Long-term Goals (3 months):**")
            st.write("• Achieve target body composition")
            st.write("• Establish sustainable habits")
            st.write("• Improved fitness benchmarks")
        
        st.markdown("---")
        st.subheader("💡 Success Tips")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("**🏋️‍♂️ Workout Tips**")
            st.write("• Consistency over perfection")
            st.write("• Progressive overload")
            st.write("• Proper form and technique")
            st.write("• Adequate rest between sets")
            st.write("• Listen to your body")
        
        with col2:
            st.markdown("**🍽️ Nutrition Tips**")
            st.write("• Meal prep on weekends")
            st.write("• Stay hydrated (3-4L water)")
            st.write("• Time your pre/post workout meals")
            st.write("• Include variety in vegetables")
            st.write("• Don't skip meals")
        
        with col3:
            st.markdown("**📊 Tracking Tips**")
            st.write("• Weigh yourself consistently")
            st.write("• Take progress photos")
            st.write("• Track measurements weekly")
            st.write("• Monitor energy levels")
            st.write("• Celebrate small wins")
        
        # Plan adherence guidelines
        st.markdown("---")
        st.subheader("📋 Plan Adherence Guidelines")
        
        adherence_info = {
            "Excellent (90-100%)": {
                "description": "Following plan almost perfectly",
                "color": "green",
                "tips": ["You're doing great!", "Focus on maintaining consistency", "Consider slight progressions"]
            },
            "Good (80-89%)": {
                "description": "Strong adherence with minor deviations",
                "color": "blue", 
                "tips": ["Identify what's working well", "Address minor obstacles", "Stay motivated"]
            },
            "Average (70-79%)": {
                "description": "Moderate adherence, room for improvement",
                "color": "orange",
                "tips": ["Review your schedule", "Simplify meal prep", "Find accountability partner"]
            },
            "Needs Improvement (<70%)": {
                "description": "Significant adjustments needed",
                "color": "red",
                "tips": ["Start with smaller goals", "Address major barriers", "Consider plan modifications"]
            }
        }
        
        for level, info in adherence_info.items():
            with st.expander(f"{level}: {info['description']}"):
                for tip in info['tips']:
                    st.write(f"• {tip}")
    
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
        if st.button("📈 View Analytics", use_container_width=True):
            st.switch_page("pages/2_Progress_Analytics.py")

if __name__ == "__main__":
    main()
    # Add mobile navigation
    render_mobile_navigation()
