#4. Create a Flask app with a form that accepts user input and displays it.
# importing Flask and other modules
from flask import Flask, request, render_template 

# Flask constructor
app = Flask(__name__) 

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["POST", "GET"])
def form():
	if request.method == "POST":
	   # getting input with name = fname in HTML form
	    first_name = request.form.get('fname')
	   # getting input with name = lname in HTML form 
	    last_name = request.form.get("lname") 
	    return "Your name is " + first_name + " " + last_name
	return render_template("form.html")

if __name__=='__main__':
   app.run(host="0.0.0.0",port=5004)
