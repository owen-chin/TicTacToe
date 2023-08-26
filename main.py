"""
Owen Chin
This program allows a users to play tictactoe against an AI
1/9/23
"""


import copy, random


board = [[" "," "," "],
         [" "," "," "],
         [" "," "," "]
]

current_player = "X"
winner = 'None'


def display_board():
    print("  0   1   2")
    print("    |   |   ")
    print("0 " + board[0][0] + " | "  + board[0][1] + " | " + board[0][2])
    print("    |   |   ")
    print(" ---+---+---")
    print("    |   |   ")
    print("1 " + board[1][0] + " | "  + board[1][1] + " | " + board[1][2])
    print("    |   |   ")
    print(" ---+---+---")
    print("    |   |   ")
    print("2 " + board[2][0] + " | "  + board[2][1] + " | " + board[2][2])
    print("    |   |   ")


def main():
    again = 'Y'
    while again in ['y', 'Y']:
        reset_game()
        while not game_over():
            display_board()
            p1_move()
            if not game_over():
                change_player()
                display_board()
                p2_move()
                if not game_over():
                    change_player()

        display_board()
        print("Winner =", winner)
        again = input("Play again?: ")[0]
    

def p1_move():
    valid_input = False
    
    print("Player {} it's your turn".format(current_player))
    while not valid_input:
        try:
            row, col = eval(input("Enter a row and column (row, col): "))
            if board[row][col] == " ":
                valid_input = True
                board[row][col] = current_player
                break
            print("invalid input try again")
        except Exception as ex:
            print(ex)


def p2_move():
    corner_list = [(0, 0), (0, 2), (2, 0), (2, 2)]
    sides_list = [(0, 1), (1, 0), (1, 2), (2, 1)]
    center_list = [(1, 1)]
    open_list = []
    
    for pos in corner_list[::-1]:
    	if board[pos[0]][pos[1]] != " ":
            corner_list.remove(pos)
    
    for pos in center_list[::-1]:
    	if board[pos[0]][pos[1]] != " ":
            center_list.remove(pos)
        
    for pos in sides_list[::-1]:
    	if board[pos[0]][pos[1]] != " ":
            sides_list.remove(pos)

    open_list += corner_list + sides_list + center_list
    
    # Checks if winner  
    for pos in open_list:
        board_copy = copy.deepcopy(board)
        board_copy[pos[0]][pos[1]] = current_player
        if is_winner(board_copy, current_player):
            board[pos[0]][pos[1]] = current_player
            return None

    # Checks to block
    for pos in open_list:
        board_copy = copy.deepcopy(board)
        board_copy[pos[0]][pos[1]] = "X"
        if is_winner(board_copy, "X"):
            board[pos[0]][pos[1]] = current_player
            return None
            
    # Check corners
    if len(corner_list) != 0:
        corner_pos = random.choice(corner_list)
        board[corner_pos[0]][corner_pos[1]] = current_player
    # Checks center
    elif len(center_list) != 0:
        board[1][1] = current_player
    # Checks sides
    else:
        side_pos = random.choice(sides_list)
        board[side_pos[0]][side_pos[1]] = current_player
    

def reset_game():
    global winner, current_player
    winner = "None"
    
    for row in range(3):
        for col in range(3):
            board[row][col] = " "
    current_player = "X"


def game_over():
    global winner
    if is_winner(board, "X"):
        winner = "X"
        return True
    elif is_winner(board, "O"):
        winner = "O"
        return True
    else:
    	return board_full(board)


def is_winner(game_board, player):
    global winner

    # Checks rows (horizontal)
    if [player] * 3 in game_board:
        winner = player
        return True
        
    # Checks columns (vertical)
    for col in range(3):
        if player == game_board[0][col] == game_board[1][col] == game_board[2][col]:
            winner = player
            return True
            
    # Checks diagonals
    if player == game_board[0][0] == game_board[1][1] == game_board[2][2] or \
       player == game_board[0][2] == game_board[1][1] == game_board[2][0]:
        winner = player
        return True   
    return False


def board_full(game_board):
    # Checks if tied
    return not any(" " in col for col in game_board)


def change_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"


if __name__ == '__main__':
    main()