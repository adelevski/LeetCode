

nums = [1, 1, 0, 1, 1, 1]
#Output = 3

def findMaxConsecutiveOnes(nums):
    mx, count = 0, 0
    for i in nums:
        if i == 1:
            count += 1
            mx = max(mx, count)
        else:
            count = 0
    return mx
        




print(findMaxConsecutiveOnes(nums))