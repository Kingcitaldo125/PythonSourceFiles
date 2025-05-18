def print_portion(matx, i, j, N):
	k = i

	while k < N:
		if i >= N or j < 0:
			break
		print(matx[i][j], end='')
		i += 1
		j -= 1
		k += 1
	print()

N = 2

matx = [[i+j for j in range(N)] for i in range(N)]

for m in matx:
	print(m)

print(matx[0][0])

for i in range(N-1):
	for j in range(1,N):
		if j > i:
			print_portion(matx, i, j, N)

print(matx[N-1][N-1])
