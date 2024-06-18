def validate_sudoku(board):
    counts = {str(i): 0 for i in range(1, 10)}
    
    for row in board:
        for cell in row:
            if cell != "":
                counts[cell] += 1
                if counts[cell] > 9:
                    return False
    return True