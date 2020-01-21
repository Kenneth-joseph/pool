from flask import render_template,redirect,url_for   #Takes in the name of the template.

from . import main


from flask_bootstrap import Bootstrap

@main.route('/')
def index():

    return render_template('index.html')
