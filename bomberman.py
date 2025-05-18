def get_neighbors(grid, cell_i, cell_j, n_rows, n_cols):
	neighs = []

	if cell_i > 0:
		neighs.append(grid[cell_i - 1][cell_j])

	if cell_i < n_rows - 1:
		neighs.append(grid[cell_i + 1][cell_j])

	if cell_j > 0:
		neighs.append(grid[cell_i][cell_j - 1])

	if cell_j < n_cols - 1:
		neighs.append(grid[cell_i][cell_j + 1])

	return neighs

def fill_grid_state(grid, n_rows, n_cols):
	state = []

	for i in range(n_rows):
		row = []

		for j in range(n_cols):
			itm = 0

			if grid[i][j] == 'O':
				itm = 3

			row.append([i, j, itm])
		state.append(row)

	return state

def fill_grid_bombs(grid):
	for row in grid:
		for cell in row:
			if cell[2] == 0:
				cell[2] = 3

def process_grid(grid, n_rows, n_cols):
	for row in grid:
		for cell in row:
			# Count down the bomb
			if cell[2] > 0:
				cell[2] -= 1

				if cell[2] <= 0:
					# detonate
					for nn in get_neighbors(grid, cell[0], cell[1], n_rows, n_cols):
						if grid[nn[0]][nn[1]][2] > 0:
							grid[nn[0]][nn[1]][2] = 0

def main(grid, N, n_rows, n_cols):
	grid_state = fill_grid_state(grid, n_rows, n_cols)

	ln = 0
	i_count = 1

	while ln < N:
		# Fill the rest of the grid with bombs
		if i_count == 2:
			fill_grid_bombs(grid_state)
			i_count = 0

		# Check the state of the planted bomb(s)
		process_grid(grid_state, n_rows, n_cols)

		i_count += 1
		ln += 1

	print(f'ln {ln} i_count {i_count}')

	return grid_state

def print_grid_state(gstate, n_rows):
	rc = 1
	for row in gstate:
		for cell in row:
			print('.' if cell[2] == 0 else 'O',end='')
		print()

if __name__ == "__main__":
	grid = [
	".......",
	"...O...",
	"....O..",
	".......",
	"OO.....",
	"OO.....",
	]
	
	n_rows = 6
	n_cols = 7

	#seconds_sim = 0
	#seconds_sim = 1
	#seconds_sim = 2
	seconds_sim = 3

	# Run program
	gstate = main(grid, seconds_sim, n_rows, n_cols)

	print_grid_state(gstate, n_rows)
