from heapq import heappop, heappush

nums = [1,-1,-2,4,-7,3]
k = 2
# Output: 7

# nums = [10,-5,-2,4,0,3]
# k = 3
# # Output: 17

# nums = [1,-5,-20,4,-1,3,-6,-3]
# k = 2
# # Output: 0


def maxResult(nums, k):
    N = len(nums)
    h = [(-nums[0], 0)]

    for i in range(1, N):
        while h[0][1]<i-k:
            heappop(h)
        max_so_far = h[0][0]
        heappush(h, (max_so_far-nums[i], i))
        if i==N-1:
            return -(max_so_far-nums[i])
    return nums[0]

print(maxResult(nums, k))