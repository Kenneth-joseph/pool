from flask import render_template    #Takes in the name of the template.
from app import app
from flask_bootstrap import Bootstrap


#Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('navbar.html')