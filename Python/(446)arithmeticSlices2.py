from collections import Counter


nums = [2,4,6,8,10]
# Output: 7

def numOfSlices(nums):
    total = 0
    n = len(nums)
    dp = [Counter() for item in nums]
    print(dp)
    for i in range(n):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] += dp[j][diff] + 1
            total += dp[j][diff]
    return total

print(numOfSlices(nums))


