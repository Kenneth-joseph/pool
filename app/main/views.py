from flask import render_template,redirect,url_for   #Takes in the name of the template.
from app import app
from . import main


from flask_bootstrap import Bootstrap


#Views
@app.route('/Home')
def home():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('navbar.html')


@main.route('/')
def index():

    return render_template('index.html')
