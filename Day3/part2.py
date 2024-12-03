import re

with open('input.txt', 'r') as file:
    data = file.read()

# Regex patterns for do() and don't()
pattern_do = r'do\(\)'
pattern_dont = r"don't\(\)"

# Initialize variables
enabled = True  # At the beginning, mul instructions are enabled
total_part_two = 0
index = 0

while index < len(data):
    # Find the next do() or don't() instruction
    do_match = re.search(pattern_do, data[index:])
    dont_match = re.search(pattern_dont, data[index:])

    # Determine the next toggle instruction
    next_toggle = None
    toggle_position = None
    if do_match and dont_match:
        if do_match.start() < dont_match.start():
            next_toggle = 'do'
            toggle_position = index + do_match.start()
        else:
            next_toggle = "don't"
            toggle_position = index + dont_match.start()
    elif do_match:
        next_toggle = 'do'
        toggle_position = index + do_match.start()
    elif dont_match:
        next_toggle = "don't"
        toggle_position = index + dont_match.start()
    else:
        # No more toggles; process the rest of the data
        segment = data[index:]
        if enabled:
            # Find and process mul(X, Y) instructions in the segment
            mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
            matches = re.findall(mul_pattern, segment)
            total_part_two += sum(int(x) * int(y) for x, y in matches)
        break

    # Process the segment before the next toggle
    segment = data[index:toggle_position]
    if enabled:
        # Find and process mul(X, Y) instructions in the segment
        mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
        matches = re.findall(mul_pattern, segment)
        total_part_two += sum(int(x) * int(y) for x, y in matches)

    # Update the enabled status based on the toggle
    if next_toggle == 'do':
        enabled = True
        index = toggle_position + len('do()')
    else:
        enabled = False
        index = toggle_position + len("don't()")

print("Part Two - Total sum with do()/don't() instructions:", total_part_two)
