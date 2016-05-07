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

def update_board(level, mark):
	error_check = True
	while error_check == True:
		pos = ask_pos(mark, level)
		error_check = coll_check(level, pos)
		if error_check == False:
			level[pos[0]][pos[1]] = mark
		else:
			os.system("clear")
			print "Tam juz cos jest!"
			time.sleep(0.8)
			display_board(level)
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
			os.system("clear")
			print "Gupek! Jeszcze raz! "
			time.sleep(0.8)
			display_board(level)
	return str(int(input_val) - 1)

def coll_check(level, pos):
	if level[pos[0]][pos[1]] == ".":
		return False
	else:
		return True

# INPUT HANDLING

def ask_pos(player, level):
	if player == "X":
		print "Teraz gra X"
		pos_row = input_check("Wiersz", level)
		pos_col = input_check("Kolumna", level)
	elif player == "O":
		print "Teraz gra O"
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
	rounds = 1
	player = "O"
	level = gen_board()
	display_board(level)
	
	while rounds < 10:
		# round initialize
		player_count = round(level, player, rounds)
		# switching players conditions
		if player_count == "O":
			player = "X"
		elif player_count =="X":
			player = "O"
		# next round
		rounds += 1
		if rounds == 10:
			game_ending("draw")
	
	
def round(level, player, roundnum):
	
	print "Runda %s" % roundnum
	update_board(level, player)
	display_board(level)
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