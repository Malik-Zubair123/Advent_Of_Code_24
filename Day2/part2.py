with open("input.txt", "r") as file:
        lines = file.readlines()

safe_count = 0

for line in lines:
        report = [int(num) for num in line.split()]
        n = len(report)

        # Check if the report is already safe
        increasing = all(report[i] < report[i + 1] for i in range(n - 1))
        decreasing = all(report[i] > report[i + 1] for i in range(n - 1))

        if (increasing or decreasing) and all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(n - 1)):
            safe_count += 1
            continue

        # Try removing each level and checking if the modified report is safe
        for i in range(n):
            modified_report = report[:i] + report[i + 1:]
            m = len(modified_report)

            # Check if the modified report is safe
            increasing = all(modified_report[j] < modified_report[j + 1] for j in range(m - 1))
            decreasing = all(modified_report[j] > modified_report[j + 1] for j in range(m - 1))

            if (increasing or decreasing) and all(1 <= abs(modified_report[j] - modified_report[j + 1]) <= 3 for j in range(m - 1)):
                safe_count += 1
                break  # No need to check further for this report

print(f"Total Safe Reports: {safe_count}")



