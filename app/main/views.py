from flask import (Blueprint, render_template, request, 
                        flash, redirect, url_for) 

main = Blueprint('main', __name__, 
                        template_folder='../templates/main') 

@main.route('/') 
def index(): 
  return render_template('index.html', title='Home') 

@main.route('/about') 
def about():
  return render_template('about.html', title='About') 

@main.route('/terms')
def terms():
  return render_template('terms.html', title='Terms') 

@main.route('/privacy') 
def privacy():
  return render_template('privacy.html', title='Privacy')
