from bisect import bisect_left, bisect_right

# nums = [5, 7, 7, 7, 8, 8, 8, 9, 10]
# target = 8
# # Output: [4, 6]

# nums = [5, 7, 7, 7, 8, 9, 10]
# target = 8
# # Output: [4, 4]

nums = [5, 7, 7, 8, 8, 10]
target = 8
# Output: [3, 4]

# nums = [5, 7, 7, 8, 8, 10]
# target = 6
# # Output: [-1, -1]

# nums = []
# target = 0
# # Output: [-1, -1]

# Naive approach
def searchRange(nums, target):
    firstIndex = -1
    secondIndex = -1
    for num in nums:
        if num == target:
            firstIndex = nums.index(num)
            secondIndex = firstIndex
            break
    i = 0
    for second in nums[firstIndex+1:]:
        if second == target:
            i += 1
            secondIndex = firstIndex+i
    return [firstIndex, secondIndex]

# Optimized approach (binary search)
# def searchRange(nums, target):
#     if not nums: return [-1, -1]
#     N = len(nums)
#     st, end = -1, -1
#     l, r = 0, N
#     #binary search left
#     while l<r:
#         mid = (l+r)//2
#         if nums[mid] >= target:
#             r = mid
#         else:
#             l = mid + 1
#     if l < N and nums[l] == target: st=l

#     #binary search right
#     l, r = 0, N
#     while l<r:
#         mid = (l+r)//2
#         if nums[mid] <= target:
#             l = mid + 1
#         else:
#             r = mid
#     if nums[r-1] == target: end = r-1
#     return [st, end]

# Optimized approach (binary search) with bisect function cheat
# def searchRange(nums, target):
#     if not nums: return [-1, -1]
#     N = len(nums)
#     st, end = -1, -1
#     l = bisect_left(nums,target)
#     r = bisect_right(nums, target)
#     if l<N and nums[l] == target: st = l
#     if nums[r-1] == target: end = r - 1

#     return [st, end]

print(searchRange(nums, target))
