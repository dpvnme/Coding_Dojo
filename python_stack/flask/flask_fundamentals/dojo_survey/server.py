from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    print("Got POST info")
    print(request.form)
    name_from_form = request.form['name']
    loc_from_form = request.form['location']
    lang_from_form = request.form['language']
    com_from_form = request.form['comment']
    return render_template('result.html', name_on_template=name_from_form, loc_on_template=loc_from_form, lang_on_template=lang_from_form, com_on_template=com_from_form)


if __name__=='__main__':
    app.run(debug=True)