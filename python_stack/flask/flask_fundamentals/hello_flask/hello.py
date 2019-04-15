from flask import Flask, render_template

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template("index.html", phrase="hello", times=5)

@app.route("/<name>")
def hello_person(name):
    return render_template("name.html",a_name=name)

# import statements, maybe some other routes
    
@app.route('/success')
def success():
    return "success"

# app.run(debug=True) should be the very last statement! 


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.


