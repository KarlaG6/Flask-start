# NO TE OLVIDES DE ENTRAR EN DEBUGMODE => export FLASK_DEBUG=1

from flask import Flask, url_for, request, render_template, abort, redirect, session
from markupsafe import escape

app = Flask(__name__)

# Set the secret key to some random bytes.
app.secret_key = b'_jimin#jungkook]jin\jhope'

@app.route('/')
def index():
	if 'username' in session:
		return 'Logged in as %s' % escape(session['username'])
	return 'You are not logged in'

@app.route('/hello')
def hello():
	return 'Hello world'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('login.html')
# Bien hecho Karla jajajajaj

@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('index'))

#@app.route('/User/<username>')
#def show_user_profile(username):
	#show the user profile for that user
#	return 'User %s' %escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
	#show the post segun el id que debe ser integer
	return 'Post %d' %post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
	#show the subpath after de path/
	return 'Subpath %s' % escape(subpath)

@app.route('/user/<username>')
def profile(username):
	return '{}\'s profile'.format(escape(username))

@app.route('/index/')
@app.route('/index/<name>')
def myindex(name=None):
	return render_template('index.html', name=name)

# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
# 	if request.method == 'POST':
#     	f = request.files['the_file']
# 		f.save('/var/www/uploads/uploaded_file.txt')
# 	...

with app.test_request_context():
	print(url_for('index'))
	print(url_for('login'))
	print(url_for('login', next='/'))
	print(url_for('profile', username='Jhon Doe'))
	print(url_for('static', filename='index.html'))

