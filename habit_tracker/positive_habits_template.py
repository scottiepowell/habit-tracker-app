from datetime import datetime

# get the current time in the required format
current_time = datetime.now().strftime('%Y-%m-%dT%H:%M')

positive_habits = [
    {"name": "Regular Exercise", "duration": 60, "location": "Gym", "time": current_time, "habit_type": "Physical", "note": "Improve physical health"},
    {"name": "Balanced Diet", "duration": 90, "location": "Home", "time": current_time, "habit_type": "Diet", "note": "Eat a variety of foods"},
    {"name": "Drink Plenty of Water", "duration": 5, "location": "Anywhere", "time": current_time, "habit_type": "Diet", "note": "Stay hydrated"},
    {"name": "Adequate Sleep", "duration": 480, "location": "Home", "time": current_time, "habit_type": "Mental", "note": "Ensure 7-9 hours of sleep"},
    {"name": "Reading Books", "duration": 30, "location": "Home", "time": current_time, "habit_type": "Mental", "note": "Expand knowledge and imagination"},
    {"name": "Mindfulness/Meditation", "duration": 20, "location": "Home", "time": current_time, "habit_type": "Mental", "note": "Improve focus and reduce stress"},
    {"name": "Avoid Procrastination", "duration": 120, "location": "Workplace", "time": current_time, "habit_type": "Mental", "note": "Increase productivity"},
    {"name": "Regular Health Check-Ups", "duration": 60, "location": "Health Center", "time": current_time, "habit_type": "Physical", "note": "Prevent health issues"},
    {"name": "Goal Setting", "duration": 30, "location": "Home", "time": current_time, "habit_type": "Mental", "note": "Achieve personal and professional goals"},
    {"name": "Clean Living Space", "duration": 30, "location": "Home", "time": current_time, "habit_type": "Mental", "note": "Maintain a tidy environment"},
    {"name": "Consistent Learning", "duration": 60, "location": "Anywhere", "time": current_time, "habit_type": "Mental", "note": "Improve skills and knowledge"},
    {"name": "Healthy Relationships", "duration": 60, "location": "Anywhere", "time": current_time, "habit_type": "Social", "note": "Foster emotional well-being"},
    {"name": "Express Gratitude", "duration": 10, "location": "Home", "time": current_time, "habit_type": "Mental", "note": "Boost positive emotions"},
    {"name": "Time in Nature", "duration": 60, "location": "Outdoors", "time": current_time, "habit_type": "Mental", "note": "Reduce stress and boost mood"},
    {"name": "Help Others", "duration": 60, "location": "Anywhere", "time": current_time, "habit_type": "Social", "note": "Increase happiness and life satisfaction"},
    {"name": "Practice a Hobby", "duration": 60, "location": "Home", "time": current_time, "habit_type": "Mental", "note": "Boost creativity and reduce stress"},
    {"name": "Limit Screen Time", "duration": 120, "location": "Anywhere", "time": current_time, "habit_type": "Mental", "note": "Protect eyesight and improve productivity"},
    {"name": "Save and Invest", "duration": 60, "location": "Home", "time": current_time, "habit_type": "Financial", "note": "Ensure financial security"},
    {"name": "Regular Breaks", "duration": 15, "location": "Workplace", "time": current_time, "habit_type": "Mental", "note": "Improve productivity and focus"},
    {"name": "Positive Mindset", "duration": 15, "location": "Anywhere", "time": current_time, "habit_type": "Mental", "note": "Improve overall life satisfaction"},
]
