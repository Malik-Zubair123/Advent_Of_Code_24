import numpy as np

def parse_input(input_data):
    robots = []
    for line in input_data.strip().split("\n"):
        position, velocity = line.split(" v=")
        px, py = map(int, position[2:].split(","))
        vx, vy = map(int, velocity.split(","))
        robots.append(((px, py), (vx, vy)))
    return robots

def simulate_robots(robots, width, height, seconds):
    final_positions = []

    for (px, py), (vx, vy) in robots:
        # Compute the position after the given seconds, accounting for wrapping
        final_x = (px + vx * seconds) % width
        final_y = (py + vy * seconds) % height
        final_positions.append((final_x, final_y))

    return final_positions

def count_quadrants(positions, width, height):
    mid_x = width // 2
    mid_y = height // 2

    quadrants = [0, 0, 0, 0]  # Top-left, Top-right, Bottom-left, Bottom-right

    for x, y in positions:
        if x == mid_x or y == mid_y:
            continue  # Ignore robots exactly in the middle

        if x < mid_x and y < mid_y:
            quadrants[0] += 1  # Top-left
        elif x >= mid_x and y < mid_y:
            quadrants[1] += 1  # Top-right
        elif x < mid_x and y >= mid_y:
            quadrants[2] += 1  # Bottom-left
        else:
            quadrants[3] += 1  # Bottom-right

    return quadrants

def calculate_safety_factor(quadrants):
    factor = 1
    for count in quadrants:
        factor *= count
    return factor

def main():
    # Read input from file
    with open("input.txt", "r") as file:
        input_data = file.read()

    # Parse input
    robots = parse_input(input_data)

    # Simulate positions after 100 seconds
    width, height = 101, 103
    seconds = 100
    final_positions = simulate_robots(robots, width, height, seconds)

    # Count robots in each quadrant
    quadrants = count_quadrants(final_positions, width, height)

    # Calculate safety factor
    safety_factor = calculate_safety_factor(quadrants)

    print("Quadrants:", quadrants)
    print("Safety Factor:", safety_factor)

if __name__ == "__main__":
    main()