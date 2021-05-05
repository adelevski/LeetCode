
# nums = [2, 3, 1, 1, 4]
# #       0  1  2  3  4
# #       0: 1, 2
# #          1: 2, 3, 4
# #             2: 3
# #                3: 4
# # Output = True

# nums = [3, 2, 1, 0, 4]
# #       0  1  2  3  4
# #       0: 1  2  3
# #          1: 2  3
# #             2: 3
# #                3: n/a
# # Output = False

# nums = [0, 2, 3]
# #       0  1  2
# #       0: n/a
# # Output = False

# nums = [0]
# # Output = True

nums = [1, 0, 1, 0]
#       0  1  2  3
#       0: 1
#          1: n/a
# Output = False

# Naive approach that I came up with, should work but is too slow
# def canJump(nums):
#     if len(nums) == 1:
#         return True
#     if nums[0] == 0:
#         return False
#     d = {}
#     N = len(nums)
#     last = N-1
#     i = 0
#     while i < N:
#         jumps = nums[i]
#         d.setdefault(i, [])
#         if jumps == 0:
#             j = 0
#             while i + j <= last and nums[i+j] == 0:
#                 j += 1
#             canGoBack = False
#             for key in d:
#                 if i + j in d[key]:
#                     i = i + j
#                     canGoBack = True
#                     break
#             if canGoBack == True:
#                 jumps = nums[i]
#             else:
#                 return False
#         for j in range(1, jumps+1):
#             if i+j <= last:
#                 d[i].append(i+j)
#                 if last in d[i]:
#                     return True
#         i += 1
#     return False

# Recursive method with memoization. Recursion alone would be too slow, but this is actually still too slow as well
# def canJump(nums):
#     N = len(nums)
#     if N < 2: return True
#     dp = [False for _ in range(N)]
#     dp[0] = True
#     visited = set()
#     def rec(pos,dp):
#         maxJump = nums[pos]
#         for i in range(1,maxJump+1):
#             if pos+1 > N-1: break
#             dp[pos+1] = True
#             if pos+i not in visited: rec(pos+i, dp)
#         visited.add(pos)
#     rec(0, dp)

#     return dp[N-1]

# Greedy aproach, super fast and no extra space
def canJump(nums):
    maxJump,N,i = 0,len(nums)-1,0
    while i <= maxJump and i < N:
        if maxJump >= N:
            break
        maxJump = max(maxJump,i+nums[i])
        i += 1
    return maxJump >= N

print(canJump(nums))