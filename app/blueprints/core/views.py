from flask import Blueprint, render_template, request

core = Blueprint('core', __name__)


@core.route('/')
def index():
    return render_template('core/index.html', title='Home')


@core.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('core/login.html', title='Log In')
    else:
        pass


@core.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('core/register.html', title='Register')
    else:
        pass
