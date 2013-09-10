from flask import Blueprint, render_template

about = Blueprint('about', __name__)


@about.route('/')
def main():
    return render_template('about/about.html', title='About')


@about.route('/privacy')
def privacy():
    return render_template('about/privacy.html', title='Privacy')


@about.route('/terms')
def terms():
    return render_template('about/terms.html', title='Terms')


@about.route('/contact')
def contact():
    return render_template('about/contact.html', title='Contact')
