from collections import defaultdict, deque

# Parse the input file
def parse_input(file_path):
    with open(file_path, 'r') as file:
        sections = file.read().strip().split("\n\n")
        
        # Parse rules and updates
        rules = [tuple(map(int, line.split('|'))) for line in sections[0].splitlines()]
        updates = [list(map(int, line.split(','))) for line in sections[1].splitlines()]
        
        return rules, updates

# Function to check if an update is in the correct order
def is_correct_order(update, rules):
    for x, y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True

# Function to reorder an update based on rules using topological sorting
def reorder_update(update, rules):
    # Build graph and in-degree for topological sorting
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    # Create graph only for pages in this update
    pages_in_update = set(update)
    for x, y in rules:
        if x in pages_in_update and y in pages_in_update:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0
    
    # Topological sort
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_update = []
    
    while queue:
        current = queue.popleft()
        sorted_update.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_update

# Function to compute the sum of middle pages for corrected updates
def sum_of_corrected_middle_pages(file_path):
    rules, updates = parse_input(file_path)
    
    corrected_middle_sum = 0
    
    for update in updates:
        if not is_correct_order(update, rules):
            # Reorder update
            corrected_update = reorder_update(update, rules)
            # Compute middle page and add to sum
            middle_page = corrected_update[len(corrected_update) // 2]
            corrected_middle_sum += middle_page
    
    return corrected_middle_sum

# Main execution
if __name__ == "__main__":
    input_file = 'G:\AdvenOfCode\Day_05\input.txt'  # Update this with the correct input file path
    result = sum_of_corrected_middle_pages(input_file)
    print("Total sum of middle pages for corrected updates:", result)
