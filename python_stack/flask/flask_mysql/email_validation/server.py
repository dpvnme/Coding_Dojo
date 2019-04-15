from flask import Flask, render_template, session, redirect, request, flash
from mysqlconnection import connectToMySQL
import re

app = Flask(__name__)
app.secret_key = "llll"
@app.route('/')
def index():
    return render_template('index.html')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/check', methods=['POST'])
def check():
    valid = True
    print(len(request.form['email']))
    if not EMAIL_REGEX.match(request.form['email']):    # test whether a field matches the pattern
        valid = False
        flash("Invalid email address!", 'email')
    # if len(request.form['email']) < 1:
    #     valid = False
    #     flash("Email can't be empty!")
    db = connectToMySQL('email_validation')
    query = "SELECT * FROM email WHERE email=%(em)s;"
    data = {
        "em": request.form['email']
    }
    matching_email_list = db.query_db(query, data)
    # a SELECT query will always return a list
    # we can use whether or not the list was empty to infer uniqueness
    # if list is not empty, at least one email in db must have matched
    if len(matching_email_list) > 0:
        flash("Email already in use")
        valid = False
    
    if not valid:
        return redirect('/')
    else:
        flash(f"The email you entered({request.form['email']}) is valid. Thank you")
        mysql = connectToMySQL('email_validation')
        query = "INSERT INTO email (email, created_at, updated_at) VALUES (%(e)s, NOW(), NOW());"
        data = {
            'e': request.form['email'],
        }
        new_email = mysql.query_db(query, data)
        return redirect('/success')

@app.route('/success')
def success():
    
    mysql = connectToMySQL('email_validation')
    emails = mysql.query_db('SELECT * FROM email;')
    
    return render_template('success.html',emails=emails)


@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    mysql = connectToMySQL('email_validation')
    query = "DELETE FROM email WHERE id = %(id)s;"
    data = {
        'id': int(id)
    }
    mysql.query_db(query,data)
    return redirect('/success')


if __name__=='__main__':
    app.run(debug=True)

