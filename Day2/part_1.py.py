with open("input.txt", "r") as file:
        lines = file.readlines()

safe_count = 0

for line in lines:
        report = [int(num) for num in line.split()]
        n = len(report)

        # Check monotonicity
        increasing = all(report[i] < report[i + 1] for i in range(n - 1))
        decreasing = all(report[i] > report[i + 1] for i in range(n - 1))

        if not (increasing or decreasing):
            continue  # Skip if not monotonic

        # Check differences
        valid_differences = all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(n - 1))
        if valid_differences:
            safe_count += 1

print(f"Total Safe Reports: {safe_count}")
