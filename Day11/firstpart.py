def simulate_stones(stones, blinks):
    for _ in range(blinks):
        new_stones = []
        for stone in stones:
            if stone == 0:
                # Rule 1: 0 becomes 1
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                # Rule 2: Split the stone into two
                stone_str = str(stone)
                mid = len(stone_str) // 2
                left = int(stone_str[:mid])
                right = int(stone_str[mid:])
                new_stones.extend([left, right])
            else:
                # Rule 3: Multiply by 2024
                new_stones.append(stone * 2024)
        stones = new_stones
    return len(stones)

# Example input
initial_stones = [125, 17]

# Read the actual input from input.txt
with open("input.txt", "r") as file:
    initial_stones = list(map(int, file.read().strip().split()))

# Simulate 25 blinks
result = simulate_stones(initial_stones, 25)

print("Number of stones after 25 blinks:", result)