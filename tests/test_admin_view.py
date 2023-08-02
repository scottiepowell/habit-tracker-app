import pytest
from unittest.mock import Mock
from habit_tracker import app, db
from habit_tracker.models import User, Login, datetime

@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # here you can populate your test db
        yield client

        # after each test, you drop all tables
        with app.app_context():
            db.drop_all()

def test_admin_view(client, mocker):
    # first, you mock current user and set its role to admin
    mocker.patch('flask_login.utils._get_user', return_value=Mock(role='admin'))

    # you can set up your db here, for example, insert some users and logins...
    with app.app_context():
        user1 = User(username='demo02', role='admin')
        db.session.add(user1)
        db.session.commit()  # commit first so that user1.id is assigned

        login1 = Login(user_id=user1.id, timestamp=datetime.utcnow())
        db.session.add(login1)
        db.session.commit()

    # now, you mock the db.session.query
    mocked_query = mocker.patch('habit_tracker.db.session.query')
    # you have to prepare the return value for your query
    # it should match the structure of your actual query
    mocked_query.return_value.join.return_value.group_by.return_value.all.return_value = [(1, 'test@email.com', 'totp_secret', datetime.utcnow())]

    response = client.get('/admin')

    # Now you can make assertions about the response...
    assert response.status_code == 200

    # Don't forget to check whether your mock was actually called
    assert mocked_query.called
