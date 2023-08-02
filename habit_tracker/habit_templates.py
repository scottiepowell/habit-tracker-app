# habits_templates.py
from models import Habit
from . import db
from .negative_habits_template import negative_habits
from .positive_habits_template import positive_habits
from datetime import datetime

def create_habit_templates(user_id):
    for habit in negative_habits:
        new_habit = Habit(id=user_id, name=habit["name"], duration=habit["duration"], location=habit["location"], time=datetime.strptime(habit["time"], '%Y-%m-%dT%H:%M'), habit_type=habit["habit_type"], note=habit["note"])
        db.session.add(new_habit)

    for habit in positive_habits:
        new_habit = Habit(id=user_id, name=habit["name"], duration=habit["duration"], location=habit["location"], time=datetime.strptime(habit["time"], '%Y-%m-%dT%H:%M'), habit_type=habit["habit_type"], note=habit["note"])
        db.session.add(new_habit)
        
    db.session.commit()

