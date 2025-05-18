def get_neighbors(grid, lettr_coords):
	lx = lettr_coords[0]
	ly = lettr_coords[1]

	neighbors = []

	for i in range(lx - 1, lx + 2):
		if i < 0 or i >= len(grid):
			continue

		row = grid[i]
		for j in range(ly - 1, ly + 2):
			cell = [i,j]

			if i == lx and j == ly:
				continue
			if j < 0 or j >= len(row):
				continue
			if i == lx - 1 and j == ly - 1:
				continue
			if i == lx + 1 and j == ly + 1:
				continue
			if i == lx - 1 and j == ly + 1:
				continue
			if i == lx + 1 and j == ly - 1:
				continue

			neighbors.append(cell)

	return neighbors

def bfs(grid, word, lettr, target_lettr, visited):
	itms = [lettr]
	gitm = grid[lettr[0]][lettr[1]]

	print(f"on '{gitm}'")
	print(f"seeking '{target_lettr}'")

	while len(itms) > 0:
		itm = itms.pop(0)
		visited.add(str(itm))

		if grid[itm[0]][itm[1]] == target_lettr:
			return [itm[0], itm[1]]

		neighbors = get_neighbors(grid, itm)
		print(f"neighbors {neighbors}")
		for neigh in neighbors:
			if str(neigh) not in visited:
				itms.append(neigh)

	return []

def main(grid, word):
	first_let = word[0]
	coord = []
	visited = set()

	for i,row in enumerate(grid):
		for j,itm in enumerate(row):
			if itm == first_let:
				coord = [i,j]
				for w in range(1,len(word)):
					res = bfs(grid, word, coord, word[w], visited)
					print(f"res {res}")
					if res == []:
						return False
					coord = res
				print("finished")
				return True
	return False

grid = [
	["A","B","C","E"],
	["S","U","H","S"],
	["A","D","E","E"],
]

res = main(grid, "BUS")

print(f"res: {res}")
