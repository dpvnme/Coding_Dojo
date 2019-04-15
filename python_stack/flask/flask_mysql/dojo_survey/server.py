from flask import Flask, render_template, session, redirect, request, flash
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = "klasfdjas"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():

    valid = True
    if len(request.form['name']) < 1:
        flash("Your name can't be empty")
        valid = False
    if len(request.form['location']) < 1:
        flash("You must pick a location")
        valid = False
    if len(request.form['language']) < 1:
        flash("You must pick a language")
        valid = False
    if not valid:
        return redirect('/')
    else:
        print("Got POST info")
        mysql = connectToMySQL('dojo_survey')
        query = "INSERT INTO survey (name, location, language, comment, created_at, updated_at) VALUES (%(nam)s, %(loc)s, %(lang)s, %(com)s, NOW(), NOW());"
        data = {
        'nam': request.form['name'],
        'loc': request.form['location'],
        'lang': request.form['language'],
        'com': request.form['comment']
        }
        mysql.query_db(query, data)
        mysql = connectToMySQL('dojo_survey')
        curr_user = mysql.query_db('SELECT * FROM survey;')
        print(curr_user)
        return render_template('result.html', user = curr_user)


if __name__=='__main__':
    app.run(debug=True)