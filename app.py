from flask import Flask, render_template, request
from game.generator import generate_sudoku

app = Flask(__name__)

@app.route('/')
def index():
    board = generate_sudoku('expert')
    return render_template('index.html', board=board)

@app.route('/submit', methods=['POST'])
def submit():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            cell_value = request.form.get(f'cell-{i}-{j}')
            if cell_value == '' or cell_value is None:
                row.append("")
            else:
                row.append(int(cell_value))
        board.append(row)
    
    # Process the board as needed (e.g., validate it, solve it, etc.)
    # For now, just print the board to the console
    print(board)
    
    return render_template('index.html', board=board)

if __name__ == '__main__':
    app.run(debug=True)