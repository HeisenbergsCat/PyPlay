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
	print ""

def update_board(level, roundnum, player):
	error_check = True
	while error_check == True:
		#pos = ask_pos()
		pos = random_pos()	
		error_check = coll_check(level, pos)
		if error_check == False:
			level[pos[0]][pos[1]] = player
		else:
			pass
			#error = "collision"
			#error_msg(error)
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
	
def error_msg(error_type):
	if error_type == "collision":
		print "Collision!"
		time.sleep(0.8)
	if error_type == "wronginput":
		print "Gupek! Jeszcze raz! "
		time.sleep(0.8)
	
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
			
			
def random_pos():
	pos_row = random.randrange(0,3)
	pos_col = random.randrange(0,3)
	return [pos_row, pos_col]
	

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
	winner = "draw"
	if cond == "draw":
		winner = "remis"
		#quit()
	elif cond == "xwin":
		winner = "xwin"
		#quit()
	elif cond == "owin":
		winner = "owin"
		#quit()
	return winner
		
def game_status(roundnum, player):
	print "Runda %s" % roundnum
	print "Teraz gra %s" % player

# EXECUTION

def round(level, player, roundnum):
	
	#game_status(roundnum, player)
	out_world = update_board(level, roundnum, player)
	#display_board(level, roundnum, player)
	out_winner = game_ending(check_win(level))
	
	return [player, out_winner, out_world]

def main_game():
	# initial
	rounds = 1
	player = "O"
	level = gen_board()
	#display_board(level, rounds, player)
	
	while rounds < 10:	
		# round initialize
		player_count = round(level, player, rounds)
		# switching players conditions
		
		if player_count[0] == "O":
			player = "X"
			if player_count[1] == "owin" or player_count[1] == "xwin":
				break
			else:
				rounds += 1
		elif player_count[0] =="X":
			player = "O"
			if player_count[1] == "owin" or player_count[1] == "xwin":
				break
			else:
				rounds += 1
		# next round
		elif rounds == 10:
			game_ending("draw")
	
	return [player_count[1], player_count[2]]

database = []
temp = []

i = 0
while i < 100:
	temp = main_game()
	if temp not in database:
		database.append(temp)
		i +=1
	elif temp in database:
		pass
		#print database
		#print len(database)
		#time.sleep(0.1)
		
	
	
#print database
xwins = 0
owins = 0
draws = 0
for i in range(0, len(database) - 1):
	print database[i][0] + " " + str(database[i][1])
	if database[i][0] == "xwin":
		xwins += 1
	elif database[i][0] == "owin":
		owins += 1
	elif database[i][0] == "draw":
		draws += 1
		
print ""
print "GAMES PLAYED: %s" % len(database)
print "XWINS: %s" % xwins
print "OWINS: %s" % owins
print "DRAWS: %s" % draws
