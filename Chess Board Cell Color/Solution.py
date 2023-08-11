def make_cell_board():

    first_row = []
    for i in range(0,4):
        first_row.append('White')
        first_row.append('Black')

    second_row = []
    for i in range(0,4):
        second_row.append('Black')
        second_row.append('White')
    
    chess_board = []
    for i in range(0,4):
        chess_board.append(first_row)
        chess_board.append(second_row)
    
    return chess_board

def cells_to_coordinates(cell, chess_board):
    letters = ['A','B','C','D','E','F','G','H']
    numbers = [ str(i+1) for i in range(8)][::-1]
    
    return str(letters.index(cell[0])) + str(numbers.index(cell[1]))


def solution(cell1, cell2):
    chess_board = make_cell_board()
    coordinates_1 = cells_to_coordinates(cell1, chess_board)
    coordinates_2 = cells_to_coordinates(cell2, chess_board)

    return chess_board[int(coordinates_1[0])][int(coordinates_1[1])] == chess_board[int(coordinates_2[0])][int(coordinates_2[1])]