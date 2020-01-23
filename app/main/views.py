from flask import render_template,redirect,url_for,abort ,request #Takes in the name of the template.
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
def book():

    return render_template('book.html')

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)