from Solution import solution, make_cell_board, cells_to_coordinates


def test_chess_board():

    sol = make_cell_board()
    assert sol == [
        ['White','Black','White','Black','White','Black','White','Black'],
        ['Black','White','Black','White','Black','White','Black','White'],
        ['White','Black','White','Black','White','Black','White','Black'],
        ['Black','White','Black','White','Black','White','Black','White'],
        ['White','Black','White','Black','White','Black','White','Black'],
        ['Black','White','Black','White','Black','White','Black','White'],
        ['White','Black','White','Black','White','Black','White','Black'],
        ['Black','White','Black','White','Black','White','Black','White']
        ]

def test_coordinate_conversion():
    chess_board = make_cell_board()
    sol = cells_to_coordinates('G6',chess_board)
    assert sol == '62'

def test_different_color_cells():
    sol = solution('A1','H1')
    assert sol == False