from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

# class CommentForm(FlaskForm):
#     content=TextAreaField('comment on blog', validators=[Required()])
#     submit=SubmitField('comment')

class BookForm(FlaskForm):
    name = StringField('Title',validators=[Required()])
    category = SelectField('Category',choices=[('Technology','Technology'),('Music','Music'),('Sports','Sports')],validators = [Required()])
    post = TextAreaField('Your blog', validators = [Required()])
    submit = SubmitField('share your blog')
