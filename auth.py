from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from flask_dance.contrib.google import make_google_blueprint, google
from flask_dance.contrib.facebook import make_facebook_blueprint, facebook
from flask import redirect, url_for, jsonify, flash, render_template, request, session
from models import User, LoginForm, RegistrationForm,TwoFactorForm
from app import app, db
import pyotp, qrcode
import os

login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id) #loads the user in the db with the 'id'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        user.totp_secret = pyotp.random_base32() # Add this line to generate a TOTP secret
        db.session.add(user)
        db.session.commit()
        print(f"User ID after registration and commit: {user.id}")  # Print the user ID after registration
        print(f"Generated TOTP Secret during registration: {user.totp_secret}")
        print("User ID during registration: ", user.id)
        url = get_totp_uri(user)  # get_totp_uri is a standalone function
        image = qrcode.make(url)
        qr_code_directory = os.path.join(app.root_path, 'static/qr_codes')  # Get the full path to your directory
        os.makedirs(qr_code_directory, exist_ok=True)  # Ensure the directory exists
        qr_code_path = os.path.join(qr_code_directory, '{}.png'.format(user.email))
        image.save(qr_code_path)
        qr_code_url = url_for('static', filename='qr_codes/{}.png'.format(user.email))  # URL to access the QR code

        # Flash message and redirect to 2FA setup confirmation
        flash('Registration successful. Please scan the QR code and enter the code here to complete setup.', 'success')
        
        session['user_id_temp'] = user.id
        print(f"Session data after setting user_id_temp in register: {session}")
        
        return render_template('qr_code.html', form=TwoFactorForm(), qr_code_path=qr_code_url)

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # get user from database
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        else:
            # Successful login. Check if 2FA is set up.
            if user.totp_secret:
                # 2FA is set up. Ask for the 2FA token.
                session['user_id_temp'] = user.id
                print(f"Session data after setting user_id_temp in login: {session}")
                print(f"User ID in session after login: {session['user_id_temp']}")  # Print the user ID from the session after login

                return redirect(url_for('confirm_2fa'))
            else:
                # 2FA is not set up. Redirect to 2FA setup.
                session['user_id_temp'] = user.id
                print(f"Session data after setting user_id_temp in login: {session}")
                return redirect(url_for('setup_2fa'))
    return render_template('login.html', title='Sign In', form=form)

def after_user_registration(user):
    user.totp_secret = pyotp.random_base32()
    db.session.commit()       

def get_totp_uri(user):
    return 'otpauth://totp/habit-tracker-app:{0}?secret={1}&issuer=habit-tracker-app' \
        .format(user.email, user.totp_secret)

@app.route('/confirm_2fa', methods=['GET', 'POST'])
def confirm_2fa():
    # Assume you have a form for the 2FA code
    form = TwoFactorForm()
    
    print(f"Session data before getting user_id_temp in confirm_2fa: {session}")

    # You should fetch the user based on the 'user_id_temp' saved in the session
    user_id_temp = session.get('user_id_temp')
    user = User.query.get(user_id_temp)
    print(f"User fetched from DB in confirm_2fa: {user}")  # Print the fetched user object
    
    if user is None:
        flash('An error occurred, please try again', 'error')
        return redirect(url_for('login'))
    
    if form.validate_on_submit():
        totp = pyotp.TOTP(user.totp_secret)
        print("User ID during OTP_verification: ", user.id)
        print(f"TOTP Secret during OTP verification: {user.totp_secret}")
        print('Entered Token: ', form.totp_token.data)  # Debug print
        print('Expected Token: ', totp.now())  # Debug print
        if totp.verify(form.totp_token.data):
            login_user(user)
            flash('Logged in successfully', 'success')
            return redirect(url_for('dashboard'))  # change to your landing page
        else:
            flash('Invalid 2FA code', 'error')
            return redirect(url_for('confirm_2fa'))

    return render_template('qr_code.html', form=form) 

@app.route('/setup_2fa', methods=['GET', 'POST'])
def setup_2fa():
    # Assume you have a form for the 2FA setup
    form = TwoFactorForm()

    # You should fetch the user based on the 'user_id_temp' saved in the session
    user_id_temp = session.get('user_id_temp')
    user = User.query.get(user_id_temp)
    print(f"User fetched from DB in setup_2fa: {user}")  # Print the fetched user object

    if user is None:
        flash('An error occurred, please try again', 'error')
        return redirect(url_for('login'))
    
    if user.totp_secret is None:
        user.totp_secret = pyotp.random_base32() # Generate a new TOTP secret
        db.session.commit()
        
        url = get_totp_uri(user)  # get_totp_uri is a standalone function
        image = qrcode.make(url)
        qr_code_directory = os.path.join(app.root_path, 'static/qr_codes')  # Get the full path to your directory
        os.makedirs(qr_code_directory, exist_ok=True)  # Ensure the directory exists
        qr_code_path = os.path.join(qr_code_directory, '{}.png'.format(user.email))
        image.save(qr_code_path)
        qr_code_url = url_for('static', filename='qr_codes/{}.png'.format(user.email))  # URL to access the QR code
    else:
        qr_code_url = url_for('static', filename='qr_codes/{}.png'.format(user.email))  # URL to access the QR code

    if form.validate_on_submit():
        # Flash message and redirect to 2FA setup confirmation
        flash('2FA setup successful. Please scan the QR code and enter the code here to complete setup.', 'success')
        return render_template('qr_code.html', form=TwoFactorForm(), qr_code_path=qr_code_url)

    return render_template('two_factor_auth.html', form=form, qr_code_path=qr_code_url)

        



