import numpy as np
import random


# Game board
def create_board():
    return np.zeros((6, 6), dtype=int)


# Ships on the board
def place_ships(board):
    ships = [3, 2, 2, 1, 1, 1]
    for ship in ships:
        placed = False
        while not placed:
            x = random.randint(0, 5)
            y = random.randint(0, 5)
            orientation = random.randint(0, 1)
            if orientation == 0:
                # Ships horizontally
                if y + ship <= 6 and np.sum(board[x, y:y + ship]) == 0:
                    board[x, y:y + ship] = ship
                    placed = True
            else:
                # Ships vertically
                if x + ship <= 6 and np.sum(board[x:x + ship, y]) == 0:
                    board[x:x + ship, y] = ship
                    placed = True


# Display board on console
def print_board(board):
    print("  | 1 | 2 | 3 | 4 | 5 | 6|")
    print("  " + "-" * 21)
    for i in range(6):
        row = ""
        for j in range(6):
            if j == 0:
                row += f"{i + 1} |"
            if board[i][j] == 0 or board[i][j] == -1:
                row += "   |"
            elif board[i][j] > 0:
                row += " X |"
            else:
                row += " O |"
        print(row)
        print("  " + "-" * 21)


# Cooardinates of ships check
def is_ship(board, x, y):
    return board[x][y] > 0


# Shoot check
def make_shot(board, x, y):
    if board[x][y] == -1 or board[x][y] == -2:
        print("Вы в порядке капитан? мы уже стреляли сюда!")
    elif is_ship(board, x, y):
        board[x][y] = -2
        print("Попал! Так, где ром?!!!!")
    else:
        board[x][y] = -1
        print("Мимо!")


# game over check
def game_over(board):
    return np.count_nonzero(board > 0) == 0


# game loop
def game():
    board = create_board()
    place_ships(board)
    print("Морской бой и тысяча чертей !!!")
    print_board(board)
    while not game_over(board):
        guess = input("Угадайте строку и столбец (например, 3,4): ")
        guess = guess.split(",")
        x = int(guess[0]) - 1
        y = int(guess[1]) - 1
        make_shot(board, x, y)
        print_board(board)
    print("Йо хо хо, ты победил!!!")


# game)
game()
