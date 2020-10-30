from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content (Markdown)', validators=[DataRequired()])
    picture = FileField('Image/Thumbnail', validators=[FileAllowed(['jpg', 'jfif', 'png'])])
    submit = SubmitField('Post')
