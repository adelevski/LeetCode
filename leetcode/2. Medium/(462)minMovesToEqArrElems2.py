

# nums = [1, 2, 3]
# # Output: 2

# nums = [1, 10, 2, 9]
# # Output: 16

nums = [1, 0, 0, 8, 6]
# Output: 14

### 1 0 0 8 6
# 1 0 1 1 7 5 : 14
# 0 1 0 0 8 6 : 15
# 0 1 0 0 8 6 : 15
# 8 7 8 8 0 2 : 25
# 6 5 6 6 2 9 : 28

# Bit better than naive approach since it is utilizing a dict for repeating numbers, but still too slow
# def minMoves(nums):
#     N = len(nums)
#     d = {}
#     if N == 1:
#         return 0
#     for i in range(N):
#         if nums[i] in d:
#             continue
#         else:
#             d[nums[i]] = sum([abs(x-nums[i]) for x in nums])
#     return min(d.values())

# Using median since mean does not work, time complexity is O(nlogn)
def minMoves(nums):
    nums.sort()
    N = len(nums)
    median = nums[N//2]
    output = 0
    for i in range(N):
        output += abs(nums[i]-median)
    return output

print(minMoves(nums))
