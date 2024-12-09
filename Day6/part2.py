def find_loop_positions(grid):
    # Convert grid to list of lists for easier manipulation
    grid = [list(row) for row in grid.strip().split('\n')]
    rows, cols = len(grid), len(grid[0])
    
    # Find starting position
    start_pos = None
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '^':
                start_pos = (i, j)
                grid[i][j] = '.'  # Replace start marker with empty space
                break
        if start_pos:
            break
    
    # Direction vectors: up, right, down, left (in clockwise order)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    def simulate_path(obstacle_pos):
        # Return None if no loop found, or set of positions in loop if found
        if obstacle_pos == start_pos:
            return None
            
        # Create temporary grid with new obstacle
        temp_grid = [row[:] for row in grid]
        temp_grid[obstacle_pos[0]][obstacle_pos[1]] = '#'
        
        current_pos = start_pos
        current_dir = 0  # Start facing up
        path = [(current_pos, current_dir)]
        positions_seen = {(current_pos, current_dir)}
        
        while True:
            y, x = current_pos
            
            # Check next position
            next_y = y + directions[current_dir][0]
            next_x = x + directions[current_dir][1]
            
            # Check if guard would leave the map
            if not (0 <= next_y < rows and 0 <= next_x < cols):
                return None
                
            # Check if obstacle ahead
            if temp_grid[next_y][next_x] == '#':
                # Turn right
                current_dir = (current_dir + 1) % 4
            else:
                # Move forward
                current_pos = (next_y, next_x)
            
            # Check if we've seen this position and direction before (loop detected)
            state = (current_pos, current_dir)
            if state in positions_seen:
                # Find start of loop
                loop_start = path.index(state)
                loop_positions = set(pos for pos, _ in path[loop_start:])
                return loop_positions
                
            positions_seen.add(state)
            path.append(state)
    
    # Try each empty position as a potential obstacle
    valid_positions = set()
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '.':
                if simulate_path((i, j)) is not None:
                    valid_positions.add((i, j))
    
    return len(valid_positions)

# Test with the example input
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

result = find_loop_positions(example_input)
print(f"Number of possible obstruction positions: {result}")