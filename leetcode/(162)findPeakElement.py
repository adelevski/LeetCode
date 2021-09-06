

nums = [1,2,3,1]
# Output: 2

# nums = [1,2,1,3,5,6,4]
# Output: 5


def findPeakElement(nums):
    l, r = 0, len(nums) - 1

    while l < r:
        mid = (l + r) // 2
        if nums[mid] < nums[mid + 1]:
            l = mid + 1
        else:
            r = mid
    return l


print(findPeakElement(nums))