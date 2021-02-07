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
    # """
    # Checks uniqueness in board columns
    # :param board:
    # :return:
    # """
    # size = len(board)
    # for i in range(size):
    #     col_list = []
    #     for j in range(size):
    #         col_list.append(board[j][i])
    #     print(col_list)
    pass
# print(check_uniqueness_in_columns(board))

def validate_board(board):

    pass