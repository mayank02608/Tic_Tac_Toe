# # Tic-Tac-Toe Game

# board = [" ", " ", " ",
#          " ", " ", " ",
#          " ", " ", " "]


# def display_board():
#     print()
#     print(board[0], "|", board[1], "|", board[2])
#     print("--+---+--")
#     print(board[3], "|", board[4], "|", board[5])
#     print("--+---+--")
#     print(board[6], "|", board[7], "|", board[8])
#     print()


# def check_winner(player):
#     win = [
#         [0,1,2],
#         [3,4,5],
#         [6,7,8],
#         [0,3,6],
#         [1,4,7],
#         [2,5,8],
#         [0,4,8],
#         [2,4,6]
#     ]

#     for combo in win:
#         if board[combo[0]] == player and \
#            board[combo[1]] == player and \
#            board[combo[2]] == player:
#             return True

#     return False


# def board_full():
#     return " " not in board


# player = "X"

# while True:

#     display_board()

#     position = int(input(f"Player {player}, enter position (1-9): "))

#     if position < 1 or position > 9:
#         print("Invalid position!")
#         continue

#     if board[position-1] != " ":
#         print("Position already taken!")
#         continue

#     board[position-1] = player

#     if check_winner(player):
#         display_board()
#         print("Player", player, "Wins!")
#         break

#     if board_full():
#         display_board()
#         print("Match Draw!")
#         break

#     if player == "X":
#         player = "O"
#     else:
#         player = "X"

import random

# Create the board
board = [" " for i in range(9)]

# Display the board
def display_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

# Check winner
def check_winner(player):
    win = [
        [0,1,2], [3,4,5], [6,7,8],   # Rows
        [0,3,6], [1,4,7], [2,5,8],   # Columns
        [0,4,8], [2,4,6]             # Diagonals
    ]

    for combo in win:
        if board[combo[0]] == player and \
           board[combo[1]] == player and \
           board[combo[2]] == player:
            return True

    return False

# Check if board is full
def board_full():
    return " " not in board

# Computer's move
def computer_move():
    empty = []

    for i in range(9):
        if board[i] == " ":
            empty.append(i)

    move = random.choice(empty)
    board[move] = "O"

# Main Game
print("====== TIC TAC TOE ======")
print("You = X")
print("Computer = O")
print()

print("Board Positions")
print("1 | 2 | 3")
print("--+---+--")
print("4 | 5 | 6")
print("--+---+--")
print("7 | 8 | 9")

while True:

    display_board()

    # Player move
    position = int(input("Enter position (1-9): "))

    if position < 1 or position > 9:
        print("Invalid Position!")
        continue

    if board[position-1] != " ":
        print("Position already occupied!")
        continue

    board[position-1] = "X"

    if check_winner("X"):
        display_board()
        print("🎉 Congratulations! You Win!")
        break

    if board_full():
        display_board()
        print("Match Draw!")
        break

    # Computer move
    print("\nComputer is thinking...\n")
    computer_move()

    if check_winner("O"):
        display_board()
        print("💻 Computer Wins!")
        break

    if board_full():
        display_board()
        print("Match Draw!")
        break