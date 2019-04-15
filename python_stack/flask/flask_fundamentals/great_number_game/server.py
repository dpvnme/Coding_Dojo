from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)

app.secret_key = "Secret"

@app.route('/')
def index():
    session['my_num'] = random.randint(1, 10)
    
    if (session['my_num'] == session['user_num']):
        session['message'] = "that's the number"
    else:
        session['message'] = "that's not it"
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def process_form():
    session['user_num'] = request.form['user_number']
    print(session['user_num'])
    return redirect('index.html')



if __name__=='__main__':
    app.run(debug=True)