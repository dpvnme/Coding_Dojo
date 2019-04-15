from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)



@app.route('/')
def table():
    my_users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template('index.html', users=my_users)





if __name__=='__main__':
    app.run(debug=True)