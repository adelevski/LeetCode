
matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
# Output: 13



def kthSmallest(matrix, k):
    one = sorted([x for y in matrix for x in y])
    return one[k-1]


print(kthSmallest(matrix, k))