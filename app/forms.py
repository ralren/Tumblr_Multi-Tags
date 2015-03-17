from flask.ext.wtf import Form
from wtforms import TextField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(Form):
	tags = TextField('Enter tags here.', validators=[DataRequired()])
	submit = SubmitField("Search")