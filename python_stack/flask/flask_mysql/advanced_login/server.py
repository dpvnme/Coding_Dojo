from flask import Flask, render_template, session, redirect, request, flash
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
import datetime
import random
import re

app = Flask(__name__)
app.secret_key = 'Top Secret'
bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX =  re.compile(r'^[a-zA-Z]+$')
SCHEMA = "advanced_login"

@app.route('/')
def index():
    if "user_id" not in session:
        return render_template('index.html')
    if session['user_level'] != 9:
        return redirect('/user')
    return redirect('/admin')

@app.route('/user')
def user():
    if "user_id" not in session:
        return redirect('/')
    if session['user_level'] == 9:
        return redirect('/admin')
    return render_template("user.html")

@app.route('/admin')
def admin():
    if "user_id" not in session:
        return redirect('/danger')
    if session['user_level'] != 9:
        return redirect('/danger')
    else:
        db = connectToMySQL(SCHEMA)
        query = "SELECT * FROM users;"
        matching_users = db.query_db(query)
        return render_template('admin.html', users = matching_users)

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
    db = connectToMySQL(SCHEMA)
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
    db = connectToMySQL(SCHEMA)
    query = "INSERT INTO users (first_name, last_name, email, password_hash, user_level) VALUES(%(f)s, %(l)s, %(e)s, %(p)s, %(ul)s)"
    data = {
        "f": request.form['first_name'],
        "l": request.form['last_name'],
        "e": request.form['email'],
        "p": password_hash,
        "ul": int(1)
    }
    user_id = db.query_db(query, data)


    session['user_id'] = user_id
    session['user_level'] = int(1)
    session['hash'] = bcrypt.generate_password_hash(str(datetime.datetime.now()))
    return redirect('/user')

@app.route('/login', methods=['POST'])
def login():
    #Check whether the email provided is associated with a user in the database
    db = connectToMySQL(SCHEMA)
    query = "SELECT * FROM users WHERE email=%(em)s;"
    data = {
        "em": request.form['email']
    }
    matching_users = db.query_db(query, data)
    if matching_users:
        user = matching_users[0]
        if bcrypt.check_password_hash(user['password_hash'], request.form['password']):
            session['user_id'] = user['id']
            if user['user_level'] == 9:
                session['user_level'] = 9
                session['hash'] = bcrypt.generate_password_hash(str(user['created_at']))
                print(session['hash'])
                return redirect("/admin")
            else:
                session['user_level'] = 1
                session['hash'] = bcrypt.generate_password_hash(str(user['created_at']))
                return redirect('/user')
    
    flash("Email or password invalid")
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/danger')
def danger():
    if 'user_id' not in session:
        return redirect('/')
    if session['user_level'] != 9:
        session.clear()
        return render_template('danger.html')
    return redirect('/admin')

@app.route('/remove/<id>')
def remove(id):
    if session['user_level'] != 9:
        return redirect('/danger')
    else:
        mysql = connectToMySQL(SCHEMA)
        query = "DELETE FROM users WHERE id = %(id)s;"
        data = {
            'id': int(id)
        }
        mysql.query_db(query, data)
        return redirect('/admin')

@app.route('/change/<id>')
def change(id):
    if session['user_level'] != 9:
        return redirect('/danger')

    db = connectToMySQL(SCHEMA)
    query = "SELECT * FROM users WHERE id = %(id)s;"
    data = {
        'id': int(id)
    }
    matching_users = db.query_db(query, data)
    user = matching_users[0]

    if session['user_id'] == user['id']:
        flash("You can't demote yourself")
        return redirect('/admin')

    if user['user_level'] == 9:
        mysql = connectToMySQL(SCHEMA)
        query = "UPDATE users SET user_level = 1 WHERE id = %(id)s;"
        data = {
            'id': int(id)
        }
        mysql.query_db(query, data)
        return redirect('/admin')
    else:
        mysql = connectToMySQL(SCHEMA)
        query = "UPDATE users SET user_level = 9 WHERE id = %(id)s;"
        data = {
            'id': int(id)
        }
        mysql.query_db(query, data)
        return redirect('/admin')

if __name__=='__main__':
    app.run(debug=True)