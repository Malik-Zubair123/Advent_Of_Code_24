from collections import deque

def read_input(file_path):
    """Reads input from the file and returns a list of byte positions."""
    byte_positions = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(int, line.strip().split(','))  # Parse x and y coordinates
            byte_positions.append((x, y))
    return byte_positions

def shortest_path(byte_positions, grid_size=71, num_bytes=1024):
    "Finds the shortest path from (0,0) to (70,70) avoiding corrupted cells."
    # Step 1: Initialize the grid
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]

    # Step 2: Simulate falling bytes
    for i in range(min(num_bytes, len(byte_positions))):
        x, y = byte_positions[i]
        grid[y][x] = '#'  # Mark the cell as corrupted

    # Step 3: BFS to find the shortest path
    start = (0, 0)
    end = (grid_size - 1, grid_size - 1)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Down, Right, Up, Left
    queue = deque([(start, 0)])  # (current position, steps taken)
    visited = set([start])  # Track visited cells

    while queue:
        (x, y), steps = queue.popleft()

        # If we reached the exit
        if (x, y) == end:
            return steps

        # Check all possible moves
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_size and 0 <= ny < grid_size:  # Stay within bounds
                if grid[ny][nx] == '.' and (nx, ny) not in visited:  # Safe and unvisited
                    visited.add((nx, ny))
                    queue.append(((nx, ny), steps + 1))

    # No path found
    return -1

# Example usage
file_path = 'input.txt'  # Replace with your input file's path
byte_positions = read_input(file_path)
result = shortest_path(byte_positions, grid_size=71, num_bytes=1024)
print(f"Shortest path steps: {result}")
