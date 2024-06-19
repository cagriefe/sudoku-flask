from flask import Flask, render_template, request, session
from game.generator import generate_sudoku
from game.validate import validate_sudoku

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your actual secret key

@app.route('/')
def index():
    # Generate a new Sudoku board and store it in the session
    board = generate_sudoku('expert')
    session['original_board'] = board  # Store the generated board in the session
    return render_template('index.html', board=board)

@app.route('/submit', methods=['POST'])
def submit():
    original_board = session.get('original_board')
    if not original_board:
        return redirect(url_for('index'))  # Redirect to index if original_board is not in session

    new_board = []
    for i in range(9):
        row = []
        for j in range(9):
            cell_value = request.form.get(f'cell-{i}-{j}', original_board[i][j])
            row.append(cell_value)
        new_board.append(row)

    # Validate the new Sudoku board
    if validate_sudoku(new_board):
        session['original_board'] = new_board  # Update the board in the session if valid
        return render_template('index.html', board=new_board)
    else:
        error_message = "Invalid board: a number is used more than 9 times."
        return render_template('index.html', board=original_board, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)