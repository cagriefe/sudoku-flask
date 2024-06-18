from flask import Flask, render_template
from game.generator import generate_sudoku

app = Flask(__name__)

@app.route('/')
def index():
    board = generate_sudoku()
    return render_template('index.html', board=board)

if __name__ == '__main__':
    app.run(debug=True)