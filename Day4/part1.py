from input import data

def convert_string_to_grid(input_string):
    size = int(len(input_string) ** 0.5)
    
    return [input_string[i:i + size] for i in range(0, len(input_string), size)]

def count_xmas_occurrences(input_string):

    grid = convert_string_to_grid(input_string)
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    target = "XMAS"
    
    directions = [
        (0, 1),   
        (1, 0),   
        (1, 1),   
        (1, -1),  
        (0, -1),  
        (-1, 0),  
        (-1, -1), 
        (-1, 1)   
    ]
    
    def check_direction(x, y, dx, dy):
        if not (0 <= x + dx * 3 < rows and 0 <= y + dy * 3 < cols):
            return False
        
        word = ""
        for i in range(4):
            curr_x, curr_y = x + dx * i, y + dy * i
            word += grid[curr_x][curr_y]
        
        return word == target
    
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if check_direction(i, j, dx, dy):
                    count += 1
    
    return count

if __name__ == "__main__":
    data = data.replace("\n", "")
        
    result = count_xmas_occurrences(data)
    print(f"Number of 'XMAS' occurrences: {result}")