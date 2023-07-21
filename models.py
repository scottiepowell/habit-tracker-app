# models.py
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Date
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class Habit(db.Model):
    __tablename__ = 'habits'

    habit_id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String(255), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    habit_type = db.Column(db.String(20), nullable=False)
    note = db.Column(db.String(255))
    entries = db.relationship('DailyEntry', backref='habit')

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)  # flask-login requires the primary key column to be named 'id'
    username = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(255), nullable=True)
    password_hash = db.Column(db.String(255), nullable=True)
    habits = db.relationship('Habit', backref='user')
    totp_secret = db.Column(db.String(16))
    role = db.Column(db.String(80), nullable=False, default='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class DailyEntry(db.Model):
    __tablename__ = 'daily_entries'

    entry_id = db.Column(db.Integer, primary_key=True)
    habit_id = db.Column(db.Integer, db.ForeignKey('habits.habit_id'))
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    progress = db.Column(db.Integer, nullable=False)

class MonthlySummary(db.Model):
    __tablename__ = 'monthly_summaries'

    summary_id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer, db.ForeignKey('users.id'))
    habit_id = db.Column(db.Integer, db.ForeignKey('habits.habit_id'))
    month = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    total_duration = db.Column(db.Integer, nullable=False)
    total_entries = db.Column(db.Integer, nullable=False)

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])  # Make sure you have an Email field
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class TwoFactorForm(FlaskForm):
    totp_token = StringField('2FA Code', validators=[DataRequired()])
    submit = SubmitField('Verify')

class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class FailedLogin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)