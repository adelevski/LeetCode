

# nums = [3,4,5,1,2]
# Output: 1

nums = [4,5,6,7,0,1,2]
      # 0,1,2,3,4,5,6

# Output: 0

def findMin(nums):
    N = len(nums)
    l, r = 0, N-1
    
    while l < r:
        mid = (l + r) // 2
        if nums[l] < nums[r]:
            return nums[l]
        if nums[mid] >= nums[l]:
            l = mid + 1
        else:
            r = mid
    return nums[l]
            



print(findMin(nums))