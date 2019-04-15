from flask import Flask, render_template, session, redirect, request, flash
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
import random


app = Flask(__name__)
app.secret_key = 'Top Secret'
bcrypt = Bcrypt(app)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/createUser', methods=['POST'])
def create():
    # include some logic to validate user input before adding them to the database!
    # create the hash
    pw_hash = bcrypt.generate_password_hash(request.form['password'])  
    print(pw_hash)  
    # prints something like b'$2b$12$sqjyok5RQccl9S6eFLhEPuaRaJCcH3Esl2RWLm/cimMIEnhnLb7iC'
    # be sure you set up your database so it can store password hashes this long (60 characters)
    mysql = connectToMySQL("bcrypt")
    query = "INSERT INTO users (username, password_hash) VALUES (%(username)s, %(password_hash)s);"
    # put the pw_hash in our data dictionary, NOT the password the user provided
    data = { "username" : request.form['email'],
             "password_hash" : pw_hash }
    mysql.query_db(query, data)
    # never render on a post, always redirect!
    return redirect("/")




if __name__=='__main__':
    app.run(debug=True)