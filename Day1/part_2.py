from collections import Counter

# Read and parse the file
with open('input.txt', 'r') as file:
    left_list = []
    right_list = []
    
    for line in file:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

# Count occurrences in the right list
right_counts = Counter(right_list)

# Calculate similarity score
similarity_score = 0
for num in left_list:
    similarity_score += num * right_counts.get(num, 0)

print(f"Similarity Score: {similarity_score}")
