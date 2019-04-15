from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/say/<name>')
def hello_name(name):
    return f"Hello {name}!"

@app.route('/repeat/<num>/<a_string>')
def repeat(num,a_string):
    return str(a_string) * int(num)

@app.route('/<path:path>')
def catch_all(path):
    return "404 path not found"


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
