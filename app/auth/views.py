from flask import render_template,redirect,url_for, flash,request
from . import auth
from flask_login import login_required,login_user,logout_user
from ..models import User
from .form import LoginForm,RegistrationForm
from .. import db