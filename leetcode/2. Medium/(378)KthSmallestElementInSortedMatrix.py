
matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
# Output: 13


# Brute force method, actually gets accepted
def kthSmallest(matrix, k):
    one = sorted([x for y in matrix for x in y])
    return one[k-1]

# Binary search method
def kthSmallest2(matrix, k):
    l, r, N = matrix[0][0], matrix[-1][-1], len(matrix)

    def less_k(m):
        cnt = 0
        for r in range(N):
            x = bisect_right(matrix[r], m)
            cnt += x
        return cnt

    while l < r:
        mid = (l + r) // 2
        if less_k(mid) < k:
            l = mid + 1
        else:
            r = mid
    return l


print(kthSmallest(matrix, k))