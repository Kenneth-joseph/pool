from flask import render_template,redirect,url_for,abort   #Takes in the name of the template.
from flask_login import login_required,current_user
from ..models import User,Book
from .. import db
from . import main


from flask_bootstrap import Bootstrap

@main.route('/')
def index():
     

    return render_template ('index.html')

@main.route('/gallery')
@login_required
def gallery():

    return render_template('gallery.html')


@main.route('/about_us')
def about():

    return render_template('about-us.html')


@main.route('/book')
@login_required
def about():

    return render_template('book.html')