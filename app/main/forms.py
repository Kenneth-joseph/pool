from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,TextAreaField,SubmitField,IntegerField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class BookForm(FlaskForm):
    name = StringField('Name',validators=[Required()])
    tday = SelectField('Time of the Day',choices=[('Morning','Morning'),('Noon','Noon'),('Evening','Evening')],validators = [Required()])
    submit= SubmitField('Book')

class SlotForm(FlaskForm):
    slot=IntegerField('Book Slots', validators=[Required()])
