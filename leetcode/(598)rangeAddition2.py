

# m = 3
# n = 3
# ops = [[2,2],[3,3]]
# Output: 4

# m = 3
# n = 3
# ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
# Output: 4

m = 3
n = 3
ops = []
# Output: 9

def maxCount(m, n, ops):
    if ops:
        left_min = min(ops, key=lambda x: x[0])
        right_min = min(ops, key=lambda x: x[1])
        return left_min[0]*right_min[1]
    else:
        return m*n


print(maxCount(m, n, ops))