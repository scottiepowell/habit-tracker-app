# create_admin.py
from habit_tracker import app, db
from habit_tracker.models import User

def create_admin():
    with app.app_context(): # using app_context to leverage app database in independent script.
        # check if the admin already exists
        admin = User.query.filter_by(username='admin2').first()
        if admin is None:
            # Create new User object
            admin = User(username='admin2', email='admin2@roadmaps.link', role='admin')
            admin.set_password('admin2')

            # Add new User to the database
            db.session.add(admin)
            db.session.commit()
            print("Admin user created!")
        else:
            print("Admin user already exists!")

if __name__ == "__main__":
    create_admin()
