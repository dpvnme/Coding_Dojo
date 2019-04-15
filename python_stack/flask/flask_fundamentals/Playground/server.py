from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play/<num>')
def play(num):
    return render_template('index.html',a_number =int(num))

@app.route('/play/<num>/<color>')
def play2(num,color):
    return render_template('index.html',a_number=int(num),a_color=color)

if __name__=="__main__":
    app.run(debug=True)
