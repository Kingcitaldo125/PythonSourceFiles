def get_neighbors(grid, coords):
	lx = coords[0]
	ly = coords[1]
	neighbors = []

	# only include fresh oranges to the right or below
	if lx + 1 >= 0 and lx + 1 < len(grid):
		if grid[lx+1][ly] == 1:
			neighbors.append([lx+1, ly])
	if ly + 1 >= 0 and ly + 1 < len(grid):
		if grid[lx][ly+1] == 1:
			neighbors.append([lx, ly+1])

	return neighbors

def bfs(grid, start_location):
	itms = [start_location]

	visited = set()

	count = 0

	final = False
	while len(itms) > 0:
		itm = itms.pop(0)

		print(f"itm {itm}")
		print(f"grid {grid}")

		visited.add(str(itm))

		neighbors = get_neighbors(grid, itm)
		print(f"neighbors {neighbors}")
		print("")

		appended = False
		for neigh in neighbors:
			grid[neigh[0]][neigh[1]] = 2
			if str(neigh) not in visited:
				itms.append(neigh)
				appended = True

		if final and not appended:
			break

		if not appended:
			final = True

		count += 1

	# Check to see if any fresh oranges are left
	arot = True
	for i in range(len(grid)):
		row = grid[i]
		for j in range(len(row)):
			if grid[i][j] == 1:
				arot = False

	return [count-1, arot]

def rotting_oranges(grid):
	for i in range(len(grid)):
		row = grid[i]
		for j in range(len(row)):
			if grid[i][j] == 2:
				res = bfs(grid, [i,j])
				if res[-1] == False:
					return -1
				return res[0]
	return -1

#'''
grid = [
	[2,1,1],
	[0,1,1],
	[0,0,1],
]
#'''

#grid = [[0,2]]

res = rotting_oranges(grid)

print(f"grid: {grid}")
print(f"res: {res}")
