def soln(coordinates):
	row = int(coordinates[-1])
	col = coordinates[0]

	col_c = (ord(col) - 97) + 1

	if col_c % 2 != 0 and row % 2 == 0:
		return True

	if col_c % 2 == 0 and row % 2 != 0:
		return True

	return False

for i in ["a1", "c4", "f2", "h7"]:
	res = soln(i)
	print(res,end=' ')
