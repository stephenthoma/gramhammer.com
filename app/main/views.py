from flask import Blueprint, render_template, request

main = Blueprint('main', __name__,
                 template_folder='../templates/main')


@main.route('/')
def index():
    return render_template('index.html', title='Home')


@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html', title='Log In')
    else:
        pass


@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html', title='Register')
    else:
        pass


@main.route('/about')
def about():
    return render_template('about.html', title='About')


@main.route('/terms')
def terms():
    return render_template('terms.html', title='Terms')


@main.route('/privacy')
def privacy():
    return render_template('privacy.html', title='Privacy')


@main.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')
