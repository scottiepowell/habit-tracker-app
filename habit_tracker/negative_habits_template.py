from datetime import datetime

# get the current time in the required format
current_time = datetime.now().strftime('%Y-%m-%dT%H:%M')

negative_habits = [
    {"name": "Skipping Meals", "duration": 30, "location": "Anywhere", "time": current_time, "habit_type": "Diet", "note": "Avoid skipping meals"},
    {"name": "Smoking/Excessive Drinking", "duration": 120, "location": "Bars, Home", "time": current_time, "habit_type": "Physical", "note": "Moderation is key"},
    {"name": "Being Constantly Late", "duration": 60, "location": "Workplace, Home", "time": current_time, "habit_type": "Social", "note": "Punctuality is important"},
    {"name": "Overuse of Social Media", "duration": 180, "location": "Anywhere", "time": current_time, "habit_type": "Mental", "note": "Limit screen time"},
    {"name": "Junk Food", "duration": 60, "location": "Anywhere", "time": current_time, "habit_type": "Diet", "note": "Aim for a balanced diet"},
    {"name": "Being Inactive", "duration": 240, "location": "Anywhere", "time": current_time, "habit_type": "Physical", "note": "Physical activity is important"},
    {"name": "Lack of Sleep", "duration": 420, "location": "Home", "time": current_time, "habit_type": "Mental", "note": "Ensure 7-9 hours of sleep"},
    {"name": "Constantly Checking Email/Messages", "duration": 120, "location": "Workplace, Home", "time": current_time, "habit_type": "Mental", "note": "Set specific times for checking"},
    {"name": "Procrastinating Important Tasks", "duration": 120, "location": "Workplace, Home", "time": current_time, "habit_type": "Mental", "note": "Prioritize important tasks"},
    {"name": "Neglecting Personal Hygiene", "duration": 30, "location": "Home", "time": current_time, "habit_type": "Physical", "note": "Maintain daily hygiene routines"},
    {"name": "Poor Financial Habits", "duration": 120, "location": "Anywhere", "time": current_time, "habit_type": "Financial", "note": "Live within your means"},
    {"name": "Negative Self-Talk", "duration": 60, "location": "Anywhere", "time": current_time, "habit_type": "Mental", "note": "Maintain a positive mindset"},
    {"name": "Holding Grudges", "duration": 60, "location": "Anywhere", "time": current_time, "habit_type": "Social", "note": "Forgiveness can lead to healing"},
    {"name": "Ignoring Emotions", "duration": 60, "location": "Anywhere", "time": current_time, "habit_type": "Mental", "note": "Expressing emotions is healthy"},
    {"name": "Overworking", "duration": 480, "location": "Workplace", "time": current_time, "habit_type": "Mental", "note": "Take regular breaks"},
    {"name": "Habitual Lying", "duration": 5, "location": "Anywhere", "time": current_time, "habit_type": "Social", "note": "Honesty is the best policy"},
    {"name": "Depending on Others for Happiness", "duration": 60, "location": "Anywhere", "time": current_time, "habit_type": "Mental", "note": "Find happiness within"},
    {"name": "Impulsive Decisions", "duration": 30, "location": "Anywhere", "time": current_time, "habit_type": "Mental", "note": "Think before acting"},
    {"name": "Not Drinking Enough Water", "duration": 120, "location": "Anywhere", "time": current_time, "habit_type": "Diet", "note": "Stay hydrated"},
    {"name": "Ignoring Health Problems", "duration": 60, "location": "Anywhere", "time": current_time, "habit_type": "Physical", "note": "Regular check-ups are important"}
]
