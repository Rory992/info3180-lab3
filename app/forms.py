from flask_wtf import FlaskForm
from wtforms import StringField, TextField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
	"""docstring for ContactForm"""
	name = StringField("Name", validators=[DataRequired()])
	email = StringField('E-mail', validators=[DataRequired(), Email()])
	subject = StringField("Subject", validators=[DataRequired()])
	message = TextField("Message", validators=[DataRequired()])
