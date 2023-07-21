from app import app, User

with app.app_context():
    user = User.query.filter_by(username='demo02').first()
    print(user.check_password('1234'))

