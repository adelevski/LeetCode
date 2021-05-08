

machines = [2, 3, 2]
goal = 10
# Output = 8

# machines = [2, 3]
# goal = 5
# # Output = 6

# machines = [1, 3, 4]
# goal = 10
# # Output = 7

# machines = [4, 5, 6]
# goal = 12
# # Output = 20


def minTime(machines, goal):
    machines.sort()
    N = len(machines)
    current = 0
    day = 1
    while current < goal:
        for i in range(N):
            if machines[i]%day==0:
                current += 1
        day+=1
    return day


print(minTime(machines, goal))