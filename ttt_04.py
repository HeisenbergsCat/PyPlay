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

def ask_input():
	errorcheck = False
	while errorcheck == False:
		rowcol = raw_input("Podaj wiersz (1-3): ")
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
	pos_row = ask_input()
	pos_col = ask_input()
	return [int(pos_row), int(pos_col)]

# GAME CONDITIONS

def check_col(level, pos):
    check_result =[]
    for i in range(0, len(level)):
        check_result.append(level[i][pos[0]])
    return "".join(check_result)

def check_row(level, pos):
    check_result =[]
    for i in range(0, len(level)):
        check_result.append(level[pos[1]][i])
    return "".join(check_result)

def check_diag(level, pos):
    return "",join(check_result)

def check_win(level, pos):
	win_conds = ["XXX", "OOO"]
	if check_col(level, pos) in win_conds:
		return True
	elif check_row(level, pos) in win_conds:
		return True
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
	
	
	return player

main_game()
