with open('input.txt', 'r') as file:
    grid = [line.strip() for line in file]

def is_valid_xmas(grid, row, col):
    rows, cols = len(grid), len(grid[0])
    directions = [
        # Diagonal directions
        [(-1, -1), (1, 1)],  # Top-left to bottom-right
        [(-1, 1), (1, -1)],  # Top-right to bottom-left
        [(-1, 0), (1, 0)],   # Vertical
        [(0, -1), (0, 1)]    # Horizontal
    ]
    
    count = 0
    for dir_pair in directions:
        for forwards in [True, False]:  # Check both forwards and backwards
            for backwards in [True, False]:
                valid = True
                mas1 = []
                mas2 = []
                
                # First MAS
                for dx, dy in dir_pair if not backwards else reversed(dir_pair):
                    r, c = row + dx, col + dy
                    if not (0 <= r < rows and 0 <= c < cols):
                        valid = False
                        break
                    mas1.append(grid[r][c])
                
                if not valid:
                    continue
                
                # Convert to string and potentially reverse
                mas1_str = ''.join(mas1)
                mas1_str = mas1_str if forwards else mas1_str[::-1]
                
                if mas1_str != 'MAS':
                    continue
                
                # Second MAS
                valid = True
                for dx, dy in (dir_pair[::-1] if not backwards else dir_pair):
                    r, c = row + dx, col + dy
                    if not (0 <= r < rows and 0 <= c < cols):
                        valid = False
                        break
                    mas2.append(grid[r][c])
                
                if not valid:
                    continue
                
                # Convert to string and potentially reverse
                mas2_str = ''.join(mas2)
                mas2_str = mas2_str if forwards else mas2_str[::-1]
                
                if mas2_str == 'MAS':
                    count += 1
    
    return count

total_xmas = 0
for row in range(len(grid)):
    for col in range(len(grid[0])):
        total_xmas += is_valid_xmas(grid, row, col)

print(total_xmas)