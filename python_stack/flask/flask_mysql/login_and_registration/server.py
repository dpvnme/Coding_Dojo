from flask import Flask, render_template, session, redirect, request, flash
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
import random
import re

app = Flask(__name__)
app.secret_key = 'Top Secret'
bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX =  re.compile(r'^[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success')
def success():
    if "user_id" not in session:
        return redirect('/')
    return render_template("success.html")

@app.route('/registration', methods=['POST'])
def registration():
    errors = []
    #First Name - letters only, at least 2 characters and that it was submitted
    if len(request.form['first_name']) < 3:
        errors.append('First name must be at least two letters')
    if not NAME_REGEX.match(request.form['first_name']):
        errors.append('First name must be letter only')

    #Last Name - letters only, at least 2 characters and that it was submitted
    if len(request.form['last_name']) < 3:
        errors.append('Last name must be at least two letters')
    if not NAME_REGEX.match(request.form['last_name']):
        errors.append('Last name must be letter only')

    #Email - valid Email format, does not already exist in the database, and that it was submitted
    if not EMAIL_REGEX.match(request.form['email']):
        errors.append("Email must be in correct format")
    db = connectToMySQL('login_and_registration')
    query = "SELECT * FROM users WHERE email=%(em)s;"
    data = {
        "em": request.form['email']
    }
    matching_user = db.query_db(query, data)
    if matching_user:
        errors.append("Email already in use")
    
    #Password - at least 8 characters, and that it was submitted
    if len(request.form['password']) < 8:
        errors.append("Password must be at least 8 characters long")
    
    #Password Confirmation - matches password
    if request.form['password'] != request.form['password_confirmation']:
        errors.append("Password must match")
    
    if errors:
        for error in errors:
            flash(error)
        return redirect('/')

    #Add user to the database and hash the password
    password_hash = bcrypt.generate_password_hash(request.form['password'])
    db = connectToMySQL('login_and_registration')
    query = "INSERT INTO users (first_name, last_name, email, password_hash) VALUES(%(f)s, %(l)s, %(e)s, %(p)s)"
    data = {
        "f": request.form['first_name'],
        "l": request.form['last_name'],
        "e": request.form['email'],
        "p": password_hash
    }
    user_id = db.query_db(query, data)
    session['user_id'] = user_id
    return redirect('/success')

@app.route('/login', methods=['POST'])
def login():
    #Check whether the email provided is associated with a user in the database

    #If it is, check whether the password matches what's saved in the database
    return redirect('/')

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)