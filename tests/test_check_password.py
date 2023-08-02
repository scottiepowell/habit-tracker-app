from habit_tracker import app
from habit_tracker.models import *

def test_check_password():
    user = User(username='demo', email='demo@email.com')
    user.set_password('1234')
    assert user.check_password('1234') is True  # The password should be correct
    assert user.check_password('wrong') is False  # The password should be incorrect


