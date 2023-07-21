from flask_login import login_user, login_required, logout_user, current_user
from flask import Flask, render_template, request, url_for, redirect, flash
from app import app, db
from models import User, Login, FailedLogin
from datetime import datetime, timedelta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
@login_required
def dashboard():
    # Implement the logic for the user's dashboard
    return render_template('dashboard.html')

from datetime import datetime, timedelta

@app.route('/admin')
def admin_view():
    if current_user.role != 'admin':
        flash('You do not have permission to access this page', 'error')
        return redirect(url_for('index'))

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

    return render_template('admin.html', num_accounts=num_accounts, recent_logins=recent_logins, failed_login_info=failed_login_info)

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