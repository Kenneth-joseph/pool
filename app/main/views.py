from flask import render_template,redirect,url_for,abort   #Takes in the name of the template.
from flask_login import login_required,current_user
from ..models import User,Book
from .. import db
from . import main
from .forms import BookForm

from flask_bootstrap import Bootstrap

@main.route('/')
def index():
     

    return render_template ('index.html')

@main.route('/book',methods=['GET','POST'])
@login_required
def book():
    form=BookForm()
    if form.validate_on_submit():
        name=form.name.data
        tday=form.tday.data
        user_id=current_user

        new_book= Book(name=name,tday=tday,user_id=current_user._get_current_object().id)
        
        new_book.save_book()
        return redirect(url_for('main.index'))
    return render_template('book/book.html',form=form)

@main.route('/gallery')
def gallery():

    return render_template('gallery.html')

@main.route('/about_us')
def about():

    return render_template('about-us.html')


