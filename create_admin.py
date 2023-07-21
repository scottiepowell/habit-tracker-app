# create_admin.py
from app import db
from models import User

def create_admin():
    # check if the admin already exists
    admin = User.query.filter_by(username='admin').first()
    if admin is None:
        # Create new User object
        admin = User(username='admin', email='admin@roadmaps.link', role='admin')
        admin.set_password('admin')

        # Add new User to the database
        db.session.add(admin)
        db.session.commit()
        print("Admin user created!")
    else:
        print("Admin user already exists!")

if __name__ == "__main__":
    create_admin()