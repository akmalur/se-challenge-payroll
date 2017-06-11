# src/web/auth/views.py
from flask import flash, redirect, url_for, render_template
from flask_login import login_user, logout_user, login_required

from . import auth
from src.common.database import Database
from src.domain.users import createUserService
from src.web.auth.login_form import LoginForm
from src.web.auth.registration_form import RegistrationForm

userService = createUserService(Database)


@auth.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        userService.createUser(email=form.email.data,password=form.password.data)
        flash('You have successfully registered! You may now login')

        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form, title='Register')

@auth.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = userService.findUserByEmail(form.email.data)
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('reports.reports'))
        else:
            flash('Invalid email or password')

    return render_template('auth/login.html', form=form, title='Login')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully been logged out.')

    return redirect(url_for('auth.login'))