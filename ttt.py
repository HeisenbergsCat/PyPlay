import os
import random

def gen_random_row():
    row = []
    for i in range(0,3):
        randomtoss = str(random.randrange(-1,2))
        if randomtoss == "-1":
            randomtoss = "."
        elif randomtoss == "0":
            randomtoss = "O"
        elif randomtoss == "1":
            randomtoss = "X"
        row.append(randomtoss)
    return row

def gen_row():
    row = []
    for i in range(0,3):
        row.append(".")
    return row

def gen_board():
    board = []
    for i in range(0,3):
        board.append(gen_row())
    return board

def display_board(board):
    os.system("clear")
    for row in board:
        print "   ".join(row)

def ask_pos(player):
	#wczytywanie pozycji
	if player == "X":
        print "Teraz gra X"
        pos_row = raw_input("Podaj wierz (0-2): "
        pos_col = raw_input("Podaj kolumne (0-2): ")
	elif player = "O":
        print "Teraz gra O"
        pos_row = raw_input("Podaj wierz (0-2): "
        pos_col = raw_input("Podaj kolumne (0-2): ")
    return (pos_row, pos_col)


level = gen_board()

def main_game():
    rounds = 9
    while rounds > 0:
        if mark == "X":
            pos_x = ask_pos("X")
            update_board(pos_x)
            if check_win(pos_x) == True:
                print "The X wins"
                rounds = 0
            else:
                rounds -= 1
                mark = "O"
        if mark == "O":
            pos_o = ask_pos("O")
            update_board(pos_o)
            if check_win(pos_o) == True:
                print "Tho O wins"
                rounds = 0
            else:
                rounds -= 1
                mark = "X"

ask_pos("X")
display_board(level)
