with open('input.txt', 'r') as file:
    grid = [line.strip() for line in file]

def part2(grid):
    def check_side(side1, side2, pattern):
        return side1 == pattern[0] and side2 == pattern[1]

    cnt = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'A':  # Center of the "X-MAS" pattern
                try:
                    # Extract diagonal elements
                    top_left = grid[i - 1][j - 1] if i > 0 and j > 0 else None
                    bot_right = grid[i + 1][j + 1] if i + 1 < rows and j + 1 < cols else None
                    bot_left = grid[i + 1][j - 1] if i + 1 < rows and j > 0 else None
                    top_right = grid[i - 1][j + 1] if i > 0 and j + 1 < cols else None

                    # Check rules for valid "X-MAS"
                    rule1 = (top_left and bot_right and 
                             (check_side(top_left, bot_right, ['M', 'S']) or check_side(top_left, bot_right, ['S', 'M'])))
                    rule2 = (top_right and bot_left and 
                             (check_side(top_right, bot_left, ['M', 'S']) or check_side(top_right, bot_left, ['S', 'M'])))

                    if rule1 and rule2:
                        cnt += 1
                except IndexError:
                    # Skip cells where neighbors go out of bounds
                    continue

    return cnt

# Solve Part 2
print("Part 2:", part2(grid))
