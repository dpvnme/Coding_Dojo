from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/<x>')
# def number(x):
#     return render_template('checkerboard.html', a_number=int(x))

@app.route('/<num>')
def checkerBoard(num):
    return render_template('checkerboard.html', a_number=int(num))

def makeBoard(num):
    board = []
    for i in range(num):
        row = []
        for j in range(num):
            if (i%2==0):
                if (j%2==0):
                    row.append("red")
                else:
                    row.append("black")
            else:
                if (j%2==0):
                    row.append("black")
                else:
                    row.append("red")
        board.append(row)
    return board


if __name__=='__main__':
    app.run(debug=True)