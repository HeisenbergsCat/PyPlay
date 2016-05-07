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
	print "Runda %s" % roundnum
	print "Teraz gra %s" % player
	
def error_msg(error_type):
	if error_type == "collision":
		os.system("clear")
		print "Tam juz cos jest!"
		time.sleep(0.8)
	if error_type == "wronginput":
		os.system("clear")
		print "Gupek! Jeszcze raz! "
		time.sleep(0.8)
		
		

def update_board(level, roundnum, player):
	error_check = True
	while error_check == True:
		pos = ask_pos(player, level, roundnum)
		error_check = coll_check(level, pos)
		if error_check == False:
			level[pos[0]][pos[1]] = player
		else:
			error = "collision"
			error_msg(error)
	return level


# ERROR HANDLING

def input_check(rowcol, level):
	pos_inputs = ["1", "2", "3"]
	errorcheck = False
	while errorcheck == False:
		print rowcol
		input_val = raw_input("Podaj wartosc (1-3): ")
		if input_val =="q":
			os.system("clear")
			print "Dzieki za gre!"
			time.sleep(0.8)
			quit()
		elif  str(input_val) in pos_inputs:
			errorcheck = True
		else:
			error = "wronginput"
			return error
	return str(int(input_val) - 1)

def coll_check(level, pos):
	if level[pos[0]][pos[1]] == ".":
		return False
	else:
		return True

# INPUT HANDLING

def ask_pos(player, level, roundnum):
	display_board(level, roundnum, player)
	if player == "X":
		pos_row = input_check("Wiersz", level)
		pos_col = input_check("Kolumna", level)
	elif player == "O":
		pos_row = input_check("Wiersz", level)
		pos_col = input_check("Kolumna", level)
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

# EXECUTION

def main_game():

	# initial
	rounds = 0
	player = "O"
	level = gen_board()
	display_board(level, rounds, player)
	
	while rounds < 10:
		# round initialize
		rounds += 1
		player_count = round(level, player, rounds)
		# switching players conditions
		if player_count == "O":
			player = "X"
		elif player_count =="X":
			player = "O"
		# next round
		if rounds == 9:
			game_ending("draw")
	
	
def round(level, player, roundnum):
	
	update_board(level, roundnum, player)
	#display_board(level, roundnum, player)
	return player


'''
test_level = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "X"]]
test_pos = [2, 2]

display_board(test_level)
print ""
print check_col(test_level, test_pos)
print check_row(test_level, test_pos)
print check_win(test_level, test_pos)
'''

main_game()
