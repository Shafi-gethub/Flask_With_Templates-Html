
from flask import Flask, render_template


app = Flask(__name__)

posts = [
		# Dictionary 1
		{'author': 'Shafi Gilanizadeh',
		'title ': 'Blog post 1',
		'content':'details of the first post ',
		'date_posted': 'Jun 12, 2020'},

		# Dictionary 2
		{'author': 'Shafi Gilanizadeh',
		'title ': 'Blog post 2',
		'content':'details of the Second post ',
		'date_posted': 'Jun 15, 2020'}
		]

@app.route('/')
@app.route('/home')
def home():
	return render_template('Home.html', posts=posts)


@app.route('/about')
def about():
	return render_template('About.html', title ='About')