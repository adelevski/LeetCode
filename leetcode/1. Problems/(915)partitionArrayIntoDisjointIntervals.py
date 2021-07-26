
nums = [5,0,3,8,6]
# Output: 3

# nums = [1,1,1,0,6,12]
# Output: 4


def partitionDisjoint(nums):
    leftMax = globalMax = nums[0]
    partition = 0
    for i in range(1, len(nums)):
        globalMax = max(globalMax, nums[i])
        if nums[i] < leftMax:  # If nums[i] < leftMax then nums[i] belong to left subarray, re-partition leftSubArr = nums[0..i]
            partition = i
            leftMax = globalMax
    return partition + 1



print(partitionDisjoint(nums))