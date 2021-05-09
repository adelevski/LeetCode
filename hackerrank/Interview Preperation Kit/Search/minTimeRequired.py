

# machines = [2, 3, 2]
# goal = 10
# # Output = 8

# machines = [2, 3]
# goal = 5
# # Output = 6

# machines = [1, 3, 4]
# goal = 10
# # Output = 7

machines = [4, 5, 6]
goal = 12
# Output = 20


def minTime(machines, goal):
    machines, count = sorted(machines), len(machines)
    min_day = (goal // count + 1) * machines[0]
    max_day = (goal // count + 1) * machines[-1]

    while min_day < max_day:
        day = (max_day + min_day) // 2
        day_sum = sum(day // m for m in machines)

        if day_sum >= goal:
            max_day = day
        else:
            min_day = day + 1

    return min_day

print(minTime(machines, goal))
