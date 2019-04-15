from flask import Flask, render_template, session, redirect, request, session
import random

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
@app.route('/')
def index():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1  # reading and updating session data
    else:
        session['visits'] = 1 # setting session data
    return render_template('index.html',)






if __name__=='__main__':
    app.run(debug=True)