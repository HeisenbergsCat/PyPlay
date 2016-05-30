import os
import time
import random

def coin_toss(toss_num):
	ran = random.randrange(0, toss_num, 1)
	return ran

def gen_row(lev_len):
	row = []
	x = 0
	coin = coin_toss(2)
	while x < lev_len:
		if coin == 0:
			row.append(".")
			coin = coin_toss(2)
			x += 1
		elif coin == 1:
			row.append(".")
			coin = coin_toss(2)
			x += 1

	return row

def display_level(level):
	os.system("clear")
	print " ".join(level)

def display_matrix(matrix):
	os.system("clear")
	for row in matrix:
		print " ".join(row)


def gen_matrix(cols,rows):
	matrix = []
	for i in range(0, cols):
		row = gen_row(rows)
		matrix.append(row)
	return matrix


test_level = gen_matrix(30,30)

pos = [len(test_level) /2,len(test_level) /2]
i = 0
while pos[0] != len(test_level) - 1 and pos[1] != len(test_level) - 1:
	coin = coin_toss(4)
	if coin == 0:
		pos[1] += 1
		test_level[pos[0]][pos[1]] = "@"
		i += 1
	elif coin == 1:
		pos[0] += 1
		test_level[pos[0]][pos[1]] = "^"
		i += 1
	elif coin == 2:
		pos[0] -= 1
		test_level[pos[0]][pos[1]] = "*"
		i += 1
	elif coin == 3:
		pos[1] -= 1
		test_level[pos[0]][pos[1]] = "%"
		i += 1
	else:
		break
	time.sleep(0.01)

	display_matrix(test_level)
	print pos
	print "steps: " + str(i)

	def test_function():
		#jakas funkcja dodana
		return

	def kolejna():
		#dodajmy jeszcze jedna funkcje
		return
