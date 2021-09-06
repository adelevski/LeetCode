
n = 2
# # Output: [0,1,3,2]

# n = 1
# Output: [0,1]





def grayCode(n):
    results = [0]
    for i in range(n):
        results += [x + pow(2, i) for x in reversed(results)]
    return results



print(grayCode(n))