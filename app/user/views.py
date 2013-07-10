from flask import Blueprint, render_template

user = Blueprint('user', __name__,
                 template_folder='../templates/user')


@user.route('/')
def account():
    return render_template('account.html', title='Account')
