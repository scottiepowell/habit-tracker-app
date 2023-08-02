from flask_login import login_user, login_required, logout_user, current_user
from flask import Flask, render_template, request, url_for, redirect, flash
from . import app, db
from .models import User, Login, FailedLogin, CreateAdminForm, Habit
from datetime import datetime, timedelta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    # Query the habit data
    positive_habits = Habit.query.filter_by(habit_type='Positive').all()
    negative_habits = Habit.query.filter_by(habit_type='Negative').all()

    return render_template('dashboard.html', positive_habits=positive_habits, negative_habits=negative_habits)


from datetime import datetime, timedelta

@app.route('/admin')
def admin_view():
    if current_user.role != 'admin':
        flash('You do not have permission to access this page', 'error')
        return redirect(url_for('index'))

    user = User.query.filter_by(username='demo01').first()
    print(user)

    # Get the current time
    now = datetime.utcnow()

    # Get the number of user accounts
    num_accounts = User.query.count()

    # Get the number of logged in users in the last 72 hours
    three_days_ago = now - timedelta(hours=72)
    recent_logins = Login.query.filter(Login.timestamp >= three_days_ago).count()

    # Get the number and username of failed logins over the last two days
    two_days_ago = now - timedelta(days=2)
    recent_failed_logins = FailedLogin.query.filter(FailedLogin.timestamp >= two_days_ago).all()
    failed_login_info = [(login.user_id, User.query.get(login.user_id).username) for login in recent_failed_logins]

    # Get users' information including email, totp status, and last login time
    users_info = db.session.query(User.id, User.email, User.totp_secret, db.func.max(Login.timestamp)) \
        .join(Login, User.id == Login.user_id) \
        .group_by(User.id).all()
    print(users_info)  # should print out all the user information
    users_info = [(info[0], info[1], bool(info[2]), info[3]) for info in users_info]

    return render_template('admin.html', num_accounts=num_accounts, recent_logins=recent_logins, failed_login_info=failed_login_info, users_info=users_info)

@app.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    if current_user.role != 'admin':
        flash('You do not have permission to perform this action', 'error')
        return redirect(url_for('index'))

    user = User.query.get(user_id)
    if user is None:
        flash('User not found', 'error')
        return redirect(url_for('admin_view'))

    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully', 'success')
    return redirect(url_for('admin_view'))

@app.route('/create_admin', methods=['GET', 'POST'])
def create_admin():
    # only allow admins to access this page
    if current_user.role != 'admin':
        flash('You do not have permission to access this page', 'error')
        return redirect(url_for('index'))

    form = CreateAdminForm()
    if form.validate_on_submit():
        # check if the admin already exists
        admin = User.query.filter_by(username=form.username.data).first()
        if admin is not None:
            flash('Admin user already exists!', 'error')
            return redirect(url_for('create_admin'))

        # Create new User object
        admin = User(username=form.username.data, email=form.email.data, role='admin')
        admin.set_password(form.password.data)

        # Add new User to the database
        db.session.add(admin)
        db.session.commit()

        flash('Admin user created!', 'success')
        return redirect(url_for('admin_view'))

    return render_template('create_admin.html', form=form)

