with open('input.txt', 'r') as file:
    left_list = []
    right_list = []

    for line in file:
        left , right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

    left_list.sort()
    right_list.sort()

total_distance = sum(abs(l-r) for l,r in zip(left_list, right_list))

print(total_distance)
