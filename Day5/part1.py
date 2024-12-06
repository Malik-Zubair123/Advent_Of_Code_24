from collections import defaultdict

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
    # Iterate through each rule and check compliance
    for x, y in rules:
        if x in update and y in update:
            # Check if x appears before y in the update
            if update.index(x) > update.index(y):
                return False
    return True

# Function to compute the sum of middle pages of valid updates
def sum_of_middle_pages(file_path):
    # Parse input to get rules and updates
    rules, updates = parse_input(file_path)
    
    middle_pages_sum = 0
    for update in updates:
        if is_correct_order(update, rules):
            # Compute the middle page index
            middle_page = update[len(update) // 2]
            middle_pages_sum += middle_page

    return middle_pages_sum

# Main execution
if __name__ == "__main__":
    input_file = 'input.txt'  # Update this with the correct input file path
    result = sum_of_middle_pages(input_file)
    print(f"The sum of the middle page numbers for correctly-ordered updates is: {result}")
