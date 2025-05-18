'''
[1,2] [1,1]
[3,2] [3,4]

7, 9
9, 11
'''

def matx_mul(matx_one, matx_two):
	for i in matx_one:
		if len(i) != len(matx_two):
			return []

	one_rows = len(matx_one)
	two_cols = len(matx_two[0])
	res = [[0 for z in range(two_cols)] for x in range(one_rows)]

	# for each row in the first matx
	for row in range(one_rows):
		# for each column in the second matx
		for i in range(two_cols):
			nsum = 0
			# for each value in the current row of the first matx
			for j in range(len(row)):
				nsum += row[j] * matx_two[j][i]
			res[row][i] = nsum

	return res
