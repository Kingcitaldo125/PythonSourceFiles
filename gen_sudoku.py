from random import randint

def valid_row(row):
	xset = set([])

	for r in row:
		if r == ".":
			continue

		if r in xset:
			return False

		xset.add(r)

	return True

def valid_col(board, col):
	xset = set([])

	for i in range(len(board)):
		if board[i][col] == ".":
			continue

		if board[i][col] in xset:
			return False

		xset.add(board[i][col])

	return True

def valid_board(board):
	for i in range(len(board)):
		if not valid_row(board[i]) or not valid_col(board, i):
			return False

	return True

def gen_row(entropy):
	row = []

	for i in range(9):
		ri = randint(1,10)
		if ri > entropy:
			row.append(".")
			continue
		row.append(str(randint(1,9)))

	return row

def gen_board(entropy=5):
	board = []

	while len(board) < 9:
		row = gen_row(entropy)

		while 1:
			if valid_row(row):
				break

			row = gen_row(entropy)

		board.append(row)
		#print(f"board {board}")

		if not valid_board(board):
			board = []

	board = str(board).replace('[','{').replace(']','}').split("},")
	return board

from sys import argv

board = gen_board(int(argv[1])-1)

for b in board[:-1]:
	print(b+"},")
print(board[-1])

#print(board)
