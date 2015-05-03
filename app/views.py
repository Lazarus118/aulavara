from flask import render_template, flash, redirect, session, url_for, request, g, abort, send_from_directory
from flask.ext.login import login_user, logout_user, current_user, login_required
from flask.ext.admin import helpers, expose
from werkzeug import secure_filename
from app import app, db, lm
from forms import LoginForm, adminForm
from models import User, Projects
import os

@app.before_request
def before_request():
	g.user = current_user


@app.route('/')
def index():
	post = Projects.query.all()
	commar = ','
	return render_template('index.html', post=post, commar=commar)
	


@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	if helpers.validate_form_on_submit(form):
		user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
		if user is not None:
			login_user(user)
			session['logged_in'] = True
			flash('You are now logged in')
			return redirect(url_for('admin'))
	return render_template('login.html', form=form)


@app.route('/logout')
def logout():
	logout_user()
	flash('You were logged out')
	return redirect(url_for('show_entries'))
	
	
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
		   

#***********************************************************************#
# // ADMIN //
#***********************************************************************#
@app.route('/admin/', methods=['GET', 'POST'])
def admin():
	
	#******************************************************************************#
	# //Concerned with uploading files
	#******************************************************************************#
	UPLOAD_FOLDER = ['/home/lazarus/Programming/Flask_apps/aulavara/app/static/img/']
	app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

	if request.method == 'POST':
		form = Projects(request.form['title'], 
						request.form['description'],
						request.form['button_list_title'],
						request.form['button_list_url'],
						request.form['tags'],
						request.files['file'])
		
		#***************************************************************#
		
		file = request.files['file']
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
			return redirect(url_for('admin'))
			
			
		db.session.add(form)
		db.session.commit()
			
		
	return render_template('admin.html')

		   
'''		   
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)
'''		   


#***********************************************************************#
# // NEW //
#***********************************************************************#
@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

