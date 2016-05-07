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

def display_board(board, roundnum, player):
	os.system("clear")
	for row in board:
		print " ".join(row)
	
def error_msg(error_type):
	if error_type == "collision":
		print "Tam juz cos jest!"
		time.sleep(0.8)
	if error_type == "wronginput":
		print "Gupek! Jeszcze raz! "
		time.sleep(0.8)
		
		

def update_board(level, roundnum, player):
	error_check = True
	while error_check == True:
		pos = ask_pos()
		error_check = coll_check(level, pos)
		if error_check == False:
			level[pos[0]][pos[1]] = player
		else:
			error = "collision"
			error_msg(error)
	return level


# ERROR HANDLING

def input_check(inputed):
	pos_inputs = ["1", "2", "3"]
	if inputed in pos_inputs:
		return True
	else:
		return False
	
def game_quit():
	os.system("clear")
	print "Dzieki za gre!"
	time.sleep(0.8)
	quit()

def coll_check(level, pos):
	if level[pos[0]][pos[1]] == ".":
		return False
	else:
		return True

# INPUT HANDLING

def ask_input(inpvar):
	errorcheck = False
	while errorcheck == False:
		inp_string = "Podaj %s (1-3): " % inpvar
		rowcol = raw_input(inp_string)
		if rowcol == "q":
			game_quit()
		elif input_check(rowcol) == True:
			errorcheck = True
			rowcol = str(int(rowcol) - 1)
			return rowcol
		else:
			error = "wronginput"
			error_msg(error)
			
def ask_pos():
	pos_row = ask_input("wiersz")
	pos_col = ask_input("kolumne")
	return [int(pos_row), int(pos_col)]

# GAME CONDITIONS

def analyze_level(level):
	result = ""
	output = []
	diaga = level[0][0] + level[1][1] + level[2][2]
	diagb = level[0][2] + level[1][1] + level[2][0]
	for j in range(0,3):
		for i in range(0,3):
			result = result + level[j][i]
			
	for j in range(0,3):
		for i in range(0,3):
			result = result + level[i][j]
			
	for k in range(0, 16, 3):
		output.append(result[k:k+3])
	output.append(diaga)
	output.append(diagb)
	return output
		

def check_win(level):
	win_conds = ["XXX", "OOO"]
	level_stat = analyze_level(level)
	if win_conds[0] in level_stat:
		return "xwin"
	elif win_conds[1] in level_stat:
		return "owin"
	else:
		return False

def game_ending(cond):
	if cond == "draw":
		print "REMIS"
		time.sleep(1)
		os.system("clear")
		quit()
	elif cond == "xwin":
		print "X Wygralo!"
		time.sleep(0.8)
		quit()
	elif cond == "owin":
		print "O Wygralo!"
		time.sleep(0.8)
		quit()
		
def game_status(roundnum, player):
	print "Runda %s" % roundnum
	print "Teraz gra %s" % player

# EXECUTION

def main_game():
	
	print "TIC TAC TOE!"
	time.sleep(1)
	os.system("clear")

	# initial
	rounds = 1
	player = "O"
	level = gen_board()
	display_board(level, rounds, player)
	
	while rounds < 10:
		# round initialize
		player_count = round(level, player, rounds)
		# switching players conditions
		if player_count == "O":
			player = "X"
			rounds += 1
		elif player_count =="X":
			player = "O"
			rounds += 1
		# next round
		if rounds == 10:
			game_ending("draw")
	
	
def round(level, player, roundnum):
	
	game_status(roundnum, player)
	update_board(level, roundnum, player)
	display_board(level, roundnum, player)
	game_ending(check_win(level))
	
	
	return player

main_game()
