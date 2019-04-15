from flask import Flask, render_template, request, redirect, flash
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = "as;dfkjasdfkl"
@app.route("/")
def index():
    mysql = connectToMySQL('first_flask')
    friends = mysql.query_db('SELECT * FROM friends;')
    # print(friends)
    return render_template("index.html", all_friends=friends)

@app.route("/create_friend", methods=["POST"])
def add_friend_to_db():
    valid = True
    if len(request.form['fname']) < 1:
        valid = False
        flash("Firstname can't be blank")
    if len(request.form['lname']) < 1:
        valid = False
        flash("Lastname can't be blank")
    if len(request.form['occ']) < 2:
        valid = False
        flash("Occupation must be at least two characters")

    if not valid:
        return redirect('/')
    else:
        flash("Successfuly add friend to the database")
        print(request.form)
        mysql = connectToMySQL('first_flask')
        query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(occup)s, NOW(), NOW());"
        data = {
            'fn': request.form['fname'],
            'ln': request.form['lname'],
            'occup': request.form['occ']
        }
        new_friend_id = mysql.query_db(query, data)
        return redirect('/')
            
if __name__ == "__main__":
    app.run(debug=True)
