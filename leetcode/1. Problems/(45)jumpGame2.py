

nums = [2, 3, 1, 1, 4]
#       0  1  1  2  2
# Output = 2

# nums = [2, 3, 0, 1, 4]
# # Output = 2

# nums = [1, 2, 1, 1, 1]
# # Output = 3

# Nested for loop, works but we can optimize (O(n^2) time and O(n) space)
# def jump(nums):
#     N = len(nums)
#     dp = [float('inf')]*N
#     dp[0] = 0

#     for i in range(N):
#         for j in range(1, nums[i]+1):
#             if i+j < N:
#                 dp[i+j] = min(dp[i+j], dp[i]+1)
#     return dp[-1]

# Greedy approach, faster and no space (O(n) time and O(1) space)
def jump(nums):
    N = len(nums)
    i,jump,lastPos,maxPos = 0,0,0,0
    while i < N-1:
        maxPos = max(maxPos,i+nums[i])
        if i==lastPos:
            lastPos = maxPos
            jump+=1
        i+=1

    return jump


print(jump(nums))


