from flask import (Blueprint, redirect, render_template, request,
                   session, url_for)

accounts = Blueprint('core', __name__)


@accounts.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('accounts/login.html', title='Log In')
    else:
        pass


@accounts.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('accounts/register.html', title='Register')
    else:
        pass


@accounts.route('/<username>')
def profile(username):
    return render_template('accounts/profile.html', title='Profile',
                           username=username)


@accounts.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'GET':
        return render_template('accounts/settings.html', title='Settings')
    else:
        pass


@accounts.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))
