from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from ..models import User




class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[DataRequired(),Email()])
    username = StringField('Enter your username',validators = [DataRequired()])
    password = PasswordField('Password',validators = [DataRequired(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [DataRequired()])
    submit = SubmitField('Sign Up')
    
    
    def validate_email(self,data_field):
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError('There is an account with that email')
            
    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('The username is taken')
            
    
class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators =[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
    
    
    