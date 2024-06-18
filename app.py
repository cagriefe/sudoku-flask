from flask import Flask, render_template, request
from game.generator import generate_sudoku
from game.validate import validate_sudoku

app = Flask(__name__)

# Generate a Sudoku board
@app.route('/')
def index():
    board = generate_sudoku('expert')
    return render_template('index.html', board=board)

# Handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            cell_value = request.form.get(f'cell-{i}-{j}', '')  # Get the form data
            row.append(cell_value)
        board.append(row)
    
    # Validate the Sudoku board
    if not validate_sudoku(board):
        error_message = "Invalid board: a number is used more than 9 times."
        return render_template('index.html', board=board, error_message=error_message)
    
    return render_template('index.html', board=board)

if __name__ == '__main__':
    app.run(debug=True)