from wtforms import form, fields, validators

class LoginForm(form.Form):
	username = fields.TextField('username', validators=[validators.DataRequired()])
	password = fields.PasswordField('password', validators=[validators.DataRequired()])
	
	
class adminForm(form.Form):
	title = fields.TextField('title')
	description = fields.TextField('description')
	button_list_title = fields.TextField('button_list_title')
	button_list_url = fields.TextField('button_list_url')
	tags = fields.TextField('tags')
	file = fields.FileField('file')
	file2 = fields.FileField('file2')
	
