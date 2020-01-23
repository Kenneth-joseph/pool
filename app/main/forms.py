from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,TextAreaField,SubmitField,IntegerField
from wtforms.validators import Required


# class CommentForm(FlaskForm):
#     content=TextAreaField('comment on blog', validators=[Required()])
#     submit=SubmitField('comment')

class BookForm(FlaskForm):
    name = StringField('Name',validators=[Required()])
    tday = SelectField('Time of the Day',choices=[('Morning','Morning'),('Noon','Noon'),('Evening','Evening')],validators = [Required()])
    submit= SubmitField('Book')

class SlotForm(FlaskForm):
    slot=IntegerField('Book Slots', validators=[Required()])

