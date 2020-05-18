def neighbours(r_index, c_index, r, c):
	rows_to_check = [r_index - 1, r_index, r_index + 1]
	cols_to_check = [c_index - 1, c_index, c_index + 1]
	if(-1 in rows_to_check):
		rows_to_check.remove(-1)
	if(r in rows_to_check):
		rows_to_check.remove(r)
	if(-1 in cols_to_check):
		cols_to_check.remove(-1)
	if(c in cols_to_check):
		cols_to_check.remove(c)
	
	neighbours = []
	for i in rows_to_check:
		for j in cols_to_check:
			neighbours.append([i, j])
	neighbours.remove([r_index, c_index])
	return neighbours

def count_live_neighbours(grid, r_index, c_index, neighbours_list):
	live_count = 0
	for n in neighbours_list:
		r = n[0]
		c = n[1]
		if(grid[r][c] == '1'):
			live_count += 1
	return live_count

def generate_next_grid(grid, live_count):
	for i, row in enumerate(grid):
		for (j, cell), live in zip(enumerate(row), live_count):
			if(cell == '1' and (live != 2 and live != 3)):
				 grid[i][j] = '0'
			if(cell == '0' and live == 3):
				grid[i][j] = '1'
	return grid

def main():
	r = int(input())
	c = int(input())
	grid = []
	live_count = []

	for index in range(r):
		grid.append(list(input().split()))
	
	for row in range(r):
		for col in range(c):
			neighbours_list = neighbours(row, col, r, c)
			live_count.append(count_live_neighbours(grid, row, col, neighbours_list))

	next_grid = generate_next_grid(grid, live_count)
	print(next_grid)
	
if __name__ == '__main__':

	main()
