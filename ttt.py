import os
import random
import time

# LEVEL GENERATING AND UPDATING

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
        print " ".join(row)
		
def update_board(level, pos, mark):
	level[pos[0]][pos[1]] = mark	
	return level

		
# ERROR HANDLING
		
def input_check(rowcol):
	pos_inputs = ["0", "1", "2"]
	errorcheck = False
	while errorcheck == False:
		print rowcol
		input_val = raw_input("Podaj wartosc (1-3): ")
		if input_val =="q":
			quit()
		elif  str(int(input_val) - 1) in pos_inputs:
			errorcheck = True
		else:
			print "Gupek! Jeszcze raz! "
	return str(int(input_val) - 1)

def coll_chek(level, pos):
	if level[pos[0]][pos[1]] == ".":
		return False
	else:
		return True
	
# INPUT HANDLING
	
def ask_pos(player):
	if player == "X":
		print "Teraz gra X"
		pos_row = input_check("Wiersz")
		pos_col = input_check("Kolumna")
	elif player == "O":
		print "Teraz gra O"
		pos_row = input_check("Wiersz")
		pos_col = input_check("Kolumna")
	return [int(pos_row), int(pos_col)]

# GAME CONDITIONS

def check_win(level, pos):
	return False

def game_ending(cond):
	if cond == "draw":
		print "REMIS"
		time.sleep(1)
		quit()

# EXECUTION
		
def main_game():
	
	# initial
	rounds = 1
	mark = "X"
	level = gen_board()
	display_board(level)
	
	# petla zliczajaca ruchy
	while rounds < 10:
		
		error_check = True
		if mark == "X":
			while error_check == True:
				print "Runda %s" % rounds
				pos_x = ask_pos("X")
				error_check = coll_chek(level, pos_x)
				display_board(level)
				
			if error_check == False:
				rounds += 1
				print "Nastepny gracz"
			#time.sleep(1)
			level = update_board(level, pos_x, mark)
			display_board(level)
			
			if check_win(level, pos_x) == True:
				print "The X wins"
				rounds = 0
			else:
				mark = "O"
				if rounds == 10:
					game_ending("draw")
				
		error_check = True
		if mark == "O":
			while error_check == True:
				print "Runda %s" % rounds
				pos_o = ask_pos("O")
				error_check = coll_chek(level, pos_o)
				display_board(level)
				
			if error_check == False:
				rounds += 1
				print "Nastepny gracz"
			#time.sleep(1)
			
			level = update_board(level, pos_o, mark)
			display_board(level)
			
			if check_win(level, pos_o) == True:
				print "The O wins"
				rounds = 0
			else:
				mark = "X"
				if rounds == 10:
					game_ending("draw")
					
								
main_game()							

