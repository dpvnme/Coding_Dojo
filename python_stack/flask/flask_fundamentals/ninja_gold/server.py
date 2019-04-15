from flask import Flask, render_template, session, redirect, request
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = "top secret"

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    

    if 'activities' not in session:
        session['activities'] = []

    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    now = datetime.now().strftime('%Y/%m/%d %I:%M %p')
    building_map = {
        "farm": random.randint(10,20),
        "cave": random.randint(5,10),
        "house": random.randint(2,5),
        "casino": random.randint(-50,50)
    }
    curr_gold = building_map[request.form['building']]
    session['gold'] += curr_gold
    # print('*'*80)
    # print(request.form['building'], curr_gold)
    # print('*'*80)
    

    # activity = {
    #     'content' : "",
    #     'css_class : "green-text"
    # }
    building = request.form['building']
    curr_gold = building_map[building]
    if curr_gold > 0:
        activity = {
            'content': f"Earned {curr_gold} golds from the {building}! ({now})",
            'css_class' : 'green-text'
        }
    else:
        activity = {
            'content': f"Entered {building}! and lost {curr_gold} ({now})",
            'css_class' : 'red-text'
        }
    session['activities'].insert(0, activity)

    print(session['activities'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)