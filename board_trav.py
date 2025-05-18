from random import choice

size = 4
clist = ['*', '.', '$', '#', '!', '@']
board = [[choice(clist) for j in range(size)] for i in range(size)]

print("board:")
for row in board:
	print(row)

print("board rows:")
for i in range(size):
	print(board[i])

print("board cols:")
for i in range(size):
	print(f"col{i+1}")
	for j in range(size):
		print("j,i",board[j][i])

print("diag forward")
idx = size
while idx > -size:
	for i in range(size):
		dprint = False
		for j in range(size):
			if i+j < 0 or i+j >= size:
				continue
			if idx+j < 0 or idx+j >= size:
				continue
			print("i+j,j+idx",i+j,j+idx)
			dprint = True
		if (dprint):
			print()
	idx -= 1

print("diag reverse")
idx = size
while idx > -size:
	for i in range(size - 1, -1, -1):
		dprint = False
		for j in range(size):
			if i-j+idx < 0 or i-j+idx >= size:
				continue
			if j+idx < 0 or j+idx >= size:
				continue
			print("i-j+idx,j+idx",i-j+idx,j+idx)
			dprint = True
		if (dprint):
			print()
	idx -= 1
