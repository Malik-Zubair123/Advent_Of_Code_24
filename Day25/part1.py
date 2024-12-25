# Read the input file content
file_path = 'input.txt'

# Parse the file to separate locks and keys
with open(file_path, 'r') as file:
    data = file.read().strip()

# Splitting the data into individual schematics based on the blank lines
schematics = data.split("\n\n")

# Function to convert schematics into a list of heights
def schematic_to_heights(schematic, is_lock):
    rows = schematic.splitlines()
    num_rows = len(rows)
    num_cols = len(rows[0])
    
    heights = []
    for col in range(num_cols):
        height = 0
        for row in range(num_rows):
            if is_lock:
                # Lock: Count '#' from the top
                if rows[row][col] == '#':
                    height += 1
                else:
                    break
            else:
                # Key: Count '#' from the bottom
                if rows[num_rows - 1 - row][col] == '#':
                    height += 1
                else:
                    break
        heights.append(height)
    return heights

# Extract locks and keys
locks = []
keys = []
for schematic in schematics:
    if schematic.startswith("#####"):
        locks.append(schematic)
    else:
        keys.append(schematic)

# Convert locks and keys to heights
lock_heights = [schematic_to_heights(lock, is_lock=True) for lock in locks]
key_heights = [schematic_to_heights(key, is_lock=False) for key in keys]

# Determine the number of fitting lock-key pairs
valid_pairs = 0
max_height = len(locks[0].splitlines())  # The maximum available space

for lock in lock_heights:
    for key in key_heights:
        if all(lock[col] + key[col] <= max_height for col in range(len(lock))):
            valid_pairs += 1

print(valid_pairs)