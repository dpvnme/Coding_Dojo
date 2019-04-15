from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  

app.secret_key = 'keep it secret, keep it safe'

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print("Got POST info")
    session['strawberry'] = int(request.form['strawberry'])
    session['raspberry'] = int(request.form['raspberry'])
    session['apple'] = int(request.form['apple'])
    session['black'] = int(request.form['blackberry'])
    session['fname'] = request.form['first_name']
    session['lname'] = request.form['last_name']
    session['id'] = request.form['student_id']
    return redirect("/show")
    # return render_template("checkout.html", straw=strawberry, rasp=raspberry, app=apple, blk=black, fname=fname, lname=lname, id=id)

@app.route("/show")
def refresh():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template("checkout.html", straw=session['strawberry'], rasp=session['raspberry'], app=session['apple'], blk=session['black'], fname=session['fname'], lname=session['lname'], id=session['id'])

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    