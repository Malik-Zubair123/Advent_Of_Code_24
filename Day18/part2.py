from collections import deque

def read_input(file_path):
    """Reads input from the file and returns a list of byte positions."""
    byte_positions = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(int, line.strip().split(','))  # Parse x and y coordinates
            byte_positions.append((x, y))
    return byte_positions

def is_path_blocked(grid, grid_size=71):
    """Checks if there is a path from (0,0) to (grid_size-1,grid_size-1)."""
    start = (0, 0)
    end = (grid_size - 1, grid_size - 1)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([start])
    visited = set([start])

    while queue:
        x, y = queue.popleft()

        # If we reach the exit
        if (x, y) == end:
            return False  # Path exists

        # Check all possible moves
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_size and 0 <= ny < grid_size:  # Stay within bounds
                if grid[ny][nx] == '.' and (nx, ny) not in visited:  # Safe and unvisited
                    visited.add((nx, ny))
                    queue.append((nx, ny))

    return True  # No path exists

def find_blocking_byte(byte_positions, grid_size=71):
    """Finds the first byte that blocks the path."""
    # Step 1: Initialize the grid
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]

    # Step 2: Simulate falling bytes
    for i, (x, y) in enumerate(byte_positions):
        grid[y][x] = '#'  # Mark the cell as corrupted

        # Step 3: Check if the path is blocked
        if is_path_blocked(grid, grid_size):
            return f"{x},{y}"  # Return the blocking byte coordinates

    return "No blocking byte found"

# Example usage
file_path = 'input.txt'  # Replace with your input file's path
byte_positions = read_input(file_path)
result = find_blocking_byte(byte_positions, grid_size=71)
print(f"First blocking byte: {result}")
