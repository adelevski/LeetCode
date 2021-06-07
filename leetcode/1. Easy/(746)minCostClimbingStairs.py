

cost = [10,15,20]
# Output: 15

# cost = [1,100,1,1,1,100,1,1,100,1]
# # Output: 6


def minCost(cost):
    n = len(cost)
    for i in range(2,n):
        cost[i] = cost[i] + min(cost[i-1], cost[i-2])
    return min(cost[-1], cost[-2])


print(minCost(cost))