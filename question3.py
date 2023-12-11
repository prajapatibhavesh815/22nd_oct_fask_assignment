#3. Develop a Flask app that uses URL parameters to display dynamic content.
#importing the flask Module
from flask import Flask

# Flask constructor takes the name of
# current module (__name__) as argument
app = Flask(__name__)

@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def home():
	return 'You are at home page.'

@app.route('/allow')
def allow():
	return 'You have been allowed to enter.'

@app.route('/disallow')
def disallow():
	return 'You have not been allowed to enter.'

# main driver function
if __name__ == '__main__':
	# run() method of Flask class runs the application
	# on the local development server.
	app.run(host="0.0.0.0")
