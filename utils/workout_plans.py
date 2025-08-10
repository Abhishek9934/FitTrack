def get_weekly_plan():
    """Return the 7-day workout and diet plan structure"""
    return {
        'Monday': {
            'type': 'Push (Chest, Shoulders, Triceps + Core)',
            'exercises': [
                'Barbell Bench Press (4x6-8)',
                'Incline Dumbbell Press (3x8-10)',
                'Overhead Barbell Press (3x8-10)',
                'Dumbbell Lateral Raises (3x12-15)',
                'Rope Triceps Pushdown (3x12-15)',
                'Plank to Shoulder Tap (3x30-40 sec)',
                'Hanging Knee Raises (3x12-15)'
            ],
            'diet': {
                'breakfast': '3 egg whites + 1 whole egg bhurji, 2 chapatis, salad',
                'mid_morning': 'Curd + flaxseed, roasted chana',
                'lunch': 'Chicken/paneer bhurji, 2 chapatis, mixed sabji, salad',
                'pre_workout': 'Banana + bread + PB',
                'post_workout_dinner': 'Whey + fish/chicken/soya curry, 2 chapatis, spinach',
                'optional_snack': 'Cottage cheese / curd'
            }
        },
        'Tuesday': {
            'type': 'Pull (Back, Biceps + Core)',
            'exercises': [
                'Pull-Ups (4x6-8)',
                'Barbell Bent-Over Rows (4x8-10)',
                'Seated Cable Rows (3x10-12)',
                'Face Pulls (3x12-15)',
                'Barbell Bicep Curl (3x8-10)',
                'Cable Woodchoppers (3x12-15 each side)',
                'Mountain Climbers (3x30 sec)'
            ],
            'diet': {
                'breakfast': 'Veg omelette (3 egg whites + 1 whole egg), 2 chapatis, salad',
                'mid_morning': 'Curd + roasted chana',
                'lunch': 'Chicken curry / rajma, 2 chapatis, green sabji',
                'pre_workout': 'Banana + bread + PB',
                'post_workout_dinner': 'Whey + chicken/paneer, 2 chapatis, spinach sabji',
                'optional_snack': 'Cottage cheese / curd'
            }
        },
        'Wednesday': {
            'type': 'Legs & Core',
            'exercises': [
                'Barbell Back Squats (4x6-8)',
                'Romanian Deadlift (3x8-10)',
                'Walking Lunges (3x12-14 each leg)',
                'Leg Press (3x10-12)',
                'Hanging Leg Raises (3x12-15)',
                'Side Plank Hip Lifts (3x12-15 each side)'
            ],
            'diet': {
                'breakfast': 'Eggs (3 whites + 1 whole), 2 chapatis, spinach sabji',
                'mid_morning': 'Curd + flaxseed',
                'lunch': 'Fish / soya curry, 2 chapatis, cabbage sabji',
                'pre_workout': 'Banana + bread + PB',
                'post_workout_dinner': 'Whey + chicken/paneer curry, 2 chapatis, bottle gourd sabji',
                'optional_snack': 'Cottage cheese / curd'
            }
        },
        'Thursday': {
            'type': 'Push + Core Conditioning',
            'exercises': [
                'Dumbbell Bench Press (4x6-8)',
                'Incline Dumbbell Press (3x8-10)',
                'Arnold Press (3x8-10)',
                'Dumbbell Lateral Raises (3x12-15)',
                'Rope Triceps Pushdown (3x12-15)',
                'Plank to Shoulder Tap (3x30-40 sec)',
                'Hanging Knee Raises (3x12-15)'
            ],
            'diet': {
                'breakfast': '3 egg whites + 1 whole egg bhurji, 2 chapatis, salad',
                'mid_morning': 'Curd + flaxseed, roasted chana',
                'lunch': 'Dal curry, 2 chapatis, sabji',
                'pre_workout': 'Banana + bread + PB',
                'post_workout_dinner': 'Whey + chicken, 2 chapatis, spinach',
                'optional_snack': 'Cottage cheese / curd'
            }
        },
        'Friday': {
            'type': 'Pull + Legs Hybrid & Core',
            'exercises': [
                'Pull-Ups (3x6-8)',
                'Barbell Bent-Over Rows (3x8-10)',
                'Barbell Back Squats (3x6-8)',
                'Romanian Deadlift (3x8-10)',
                'Barbell Bicep Curl (3x8-10)',
                'Cable Woodchoppers (3x12-15 each side)',
                'Mountain Climbers (3x30 sec)'
            ],
            'diet': {
                'breakfast': 'Veg omelette (3 egg whites + 1 whole egg), 2 chapatis, salad',
                'mid_morning': 'Curd + roasted chana',
                'lunch': 'Chicken curry + sweet potato, 2 chapatis, sabji',
                'pre_workout': 'Banana + bread + PB',
                'post_workout_dinner': 'Whey + chicken/paneer, 2 chapatis, spinach sabji',
                'optional_snack': 'Cottage cheese / curd'
            }
        },
        'Saturday': {
            'type': 'Swimming',
            'exercises': [
                'Steady pace with sprint intervals (20-30 mins)',
                'Treading water (5-10 mins)'
            ],
            'diet': {
                'breakfast': '2 egg whites + 1 whole egg, 1 chapati',
                'mid_morning': '–',
                'lunch': 'Chicken curry / dal makhani, 2 chapatis, spinach sabji',
                'pre_workout': 'Whey + banana (post-swim)',
                'post_workout_dinner': 'Fish / paneer curry, 2 chapatis, mixed sabji',
                'optional_snack': 'Cottage cheese / curd'
            }
        },
        'Sunday': {
            'type': 'Badminton',
            'exercises': [
                'Fast-paced play (45-60 mins)',
                'Core circuit: Planks, Side Plank Hip Drops, Flutter Kicks'
            ],
            'diet': {
                'breakfast': 'Whey + 1 chapati + banana (pre-game)',
                'mid_morning': '–',
                'lunch': 'Dal tadka, 2 chapatis, green beans sabji',
                'pre_workout': '–',
                'post_workout_dinner': 'Fish / soya curry, 2 chapatis, bottle gourd sabji',
                'optional_snack': 'Curd + flaxseed'
            }
        }
    }

def get_daily_targets():
    """Return daily nutritional targets"""
    return {
        'calories': {'min': 2000, 'max': 2200},
        'protein': {'min': 170, 'max': 180},
        'carbs': {'min': 180, 'max': 200},
        'fat': {'min': 55, 'max': 65}
    }

def get_exercise_categories():
    """Return exercise categories for tracking"""
    return {
        'Push': ['Chest', 'Shoulders', 'Triceps', 'Core'],
        'Pull': ['Back', 'Biceps', 'Core'],
        'Legs': ['Quads', 'Hamstrings', 'Glutes', 'Calves', 'Core'],
        'Cardio': ['Swimming', 'Badminton', 'Running'],
        'Core': ['Abs', 'Obliques', 'Lower Back']
    }
