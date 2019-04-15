from flask import Flask, render_template, session, redirect, request
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route('/')
def index():
    mysql = connectToMySQL('c+r_pets')
    pets = mysql.query_db('SELECT * FROM pets;')
    print(pets)
    return render_template("index.html", all_pets=pets)
    

@app.route('/add_pet', methods=['POST'])
def add_pet():
    mysql = connectToMySQL('c+r_pets')
    query = "INSERT INTO pets (name, type, created_at, updated_at) VALUES (%(n)s, %(t)s, NOW(), NOW());"
    data = {
        'n': request.form['name'],
        't': request.form['type'],
    }
    new_pet = mysql.query_db(query, data)


    return redirect('/')
if __name__=='__main__':
    app.run(debug=True)