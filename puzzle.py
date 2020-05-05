"""
Puzzle board validator
"""
# 20 may edit

def check_uniqueness_in_rows(board: list):
    """
    Checks uniqueness in board rows
    >>> check_uniqueness_in_rows(['12*','315','9**'])
    True
    """
    for row in board:  # iterating through row
        for element in row:
            if element == "*" or element == " ":  # * or ' ' duplicates are allowed
                pass
            else:
                if row.count(element) > 1:  # checking duplicates
                    return False
    return True


def check_uniqueness_in_columns(board: list):
    """
    Checks uniqueness in board columns
    >>> check_uniqueness_in_columns(['1**','345','1**'])
    False
    """
    size = len(board)
    rotated_board = []
    # Rotating the board to use the former function
    for i in range(size):
        col_list = []
        for j in range(size):
            col_list.append(board[j][i])
        rotated_board.append("".join(col_list))

    return check_uniqueness_in_rows(rotated_board)


def check_color_uniqueness(board):
    """
    Checks for color duplicates
    >>> check_color_uniqueness(['18*','231','31*'])
    False
    """
    color_lists = []
    board = [list(row) for row in board]
    board = [row+['t'] for row in board]
    board.append(['t' for el in range(len(board)+1)])
    size = len(board)
    for column in range(size):
        temp_list = []
        for row in range(size):
            v_element = board[row][column]
            if v_element == '*':
                board[row][column] = 't'
            elif v_element == 't':  # move horizontally to follow the color
                for index, element in enumerate(board[row-1]):
                    if element == '*' or element == 't':
                        board[row-1][column] = 't'
                    else:
                        temp_list.append(element)
                        board[row - 1][index] = 't'
            else:
                temp_list.append(v_element)
                board[row][column] = 't'  # mark changes on occupied elements
        color_lists.append("".join(temp_list))

    return check_uniqueness_in_rows(color_lists)

def validate_board(board):
    """
    Validates the board
    :param board:
    :return:
    """
    return check_uniqueness_in_columns(board) and check_uniqueness_in_rows(board) \
    and check_color_uniqueness(board)
