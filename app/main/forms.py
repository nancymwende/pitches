from wtforms import StringField,TextAreaField, SubmitField, SelectField 
from wtforms.validators import DataRequired,Email,Length
from flask_wtf import FlaskForm

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')
    
    

class UpdateProfileForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired(), Length(1, 64)])
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    bio = TextAreaField('About...', validators=[DataRequired(), Length(1, 100)])
    submit = SubmitField('Submit')
    
    
class PostForm(FlaskForm):
    title = StringField('Pitch title',validators=[DataRequired()])
    text = TextAreaField('Text',validators=[DataRequired()])
    category = SelectField('Type',choices=[('Love','Love'),('Funny','Funny'),('Happy','Happy'),('Friendship','Friendship')],validators=[DataRequired()])
    submit = SubmitField('Submit')    
    

class CommentForm(FlaskForm):
    comment = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Submit')    