#8. Implement user authentication and registration in a Flask app using Flask-Login.
from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb+srv://bhavesh:bhavesh@cluster0.t0d1cat.mongodb.net/?retryWrites=true&w=majority')
db = client['client_database']  # Replace 'client_database' with your database name
collection = db['users']  # Replace 'users' with your collection name

@app.route("/")
def login():
    return render_template('login2.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/home")
def home():
    return render_template('home1.html')

@app.route("/signup", methods=['POST'])
def signup():
    email = request.form.get('email')
    password = request.form.get('password')

    # Check if user already exists
    if collection.find_one({'email': email}):
        return "User already exists. Please sign in."

    # Insert new user into MongoDB
    user = {'email': email, 'password': password}
    collection.insert_one(user)

    return "Registration successful. Please sign in."

@app.route("/login_validation", methods=['POST'])

def login1():
    email = request.form.get('email')
    password = request.form.get('password')
    client = MongoClient('mongodb+srv://bhavesh:bhavesh@cluster0.t0d1cat.mongodb.net/?retryWrites=true&w=majority')
    db = client['client_database']  # Replace 'client_database' with your database name
    collection = db['users'] 

    # Check if user exists and password matches
    user = collection.find_one({'email': email, 'password': password})
    print(user)
    if user:
        # Valid credentials, redirect to the home page or perform desired actions
        return render_template('home1.html', user=user)
    else:
        # Invalid credentials, show error message and prompt to sign up
        return "User not found. Please sign up."

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)