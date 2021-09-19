
nums = [3, 1, 2, 10, 1]
# Output = [3,4,6,16,17]

# O(n) time, but also O(n) space since we are creating a new array
# def runningSum(nums):
#     temp = 0
#     outputs = []
#     for num in nums:
#         cur = num + temp
#         outputs.append(cur)
#         temp = cur
#     return outputs


# O(n) time, but no space complexity since we are doing it in-place
def runningSum(nums):
    N = len(nums)
    for i in range(1, N):
        nums[i] += nums[i-1]
    return nums
    
print(runningSum(nums))
