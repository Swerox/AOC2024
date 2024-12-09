def simulate_guard_path(grid):
    grid = [list(row) for row in grid.strip().split('\n')]
    rows, cols = len(grid), len(grid[0])
    
    start_pos = None
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '^':
                start_pos = (i, j)
                break
        if start_pos:
            break
    
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    current_dir = 0 
    
    visited = set()
    current_pos = start_pos
    visited.add(current_pos)
    
    while True:
        y, x = current_pos
        
        next_y = y + directions[current_dir][0]
        next_x = x + directions[current_dir][1]
        
        if not (0 <= next_y < rows and 0 <= next_x < cols):
            break
            
        if grid[next_y][next_x] == '#':
            # Turn right (clockwise)
            current_dir = (current_dir + 1) % 4
        else:
            current_pos = (next_y, next_x)
            visited.add(current_pos)
            
    return len(visited)

example_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

result = simulate_guard_path(example_input)
print(f"Number of distinct positions visited: {result}")