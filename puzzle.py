"""
Puzzle board validator
"""
# board = [
#  "**** ****",
#  "***1 ****",
#  "**  3****",
#  "* 4 1****",
#  "     9 5 ",
#  " 6  83  *",
#  "3   1  **",
#  "  8  2***",
#  "  2  ****"
# ]
def check_uniqueness_in_rows(board: list):
    """

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

def validate_board(board):

    pass