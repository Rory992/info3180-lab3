from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
	"""docstring for ContactForm"""
	name = StringField("Name", validators=[DataRequired()])
	email = StringField('E-mail', validators=[DataRequired(), Email()])
	subject = StringField("Subject", validators=[DataRequired()])
	message = TextAreaField("Message", validators=[DataRequired()], render_kw={"rows": 5, "cols": 60})
