from flask import Flask, render_template, session, redirect, request
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route('/')
def home():
    mysql = connectToMySQL('semi_restful_users')
    users = mysql.query_db('SELECT * FROM users;')
    print(users)
    return render_template('home.html', all_users=users)

@app.route('/users/new')
def new():
    return render_template('new.html')

@app.route('/users/create', methods=['POST'])
def create():
    mysql = connectToMySQL('semi_restful_users')
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(em)s, NOW(), NOW());"
    data = {
        'fn': request.form['first_name'],
        'ln': request.form['last_name'],
        'em': request.form['email']
    }
    new_user = mysql.query_db(query, data)
    return redirect(f'/users/{new_user}')

@app.route('/users/<id>/show')
def show(id):
    mysql = connectToMySQL('semi_restful_users')
    query = mysql.query_db('SELECT * FROM users WHERE user_id = %(user_id)s;')
    data = {
        'user_id' : int(id)
    }
    user = mysql.query_db(query, data)
    print(user)
    
    return render_template('user.html', user=user)


if __name__=='__main__':
    app.run(debug=True)