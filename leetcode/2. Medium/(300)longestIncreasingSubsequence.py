from bisect import bisect_left



nums = [10,9,2,5,3,7,101,18]
# Output: 4

# nums = [0,1,0,3,2,3]
# # Output: 4

# nums = [7,7,7,7,7,7,7]
# Output: 1

# DP method but it is O(n^2)
def lengthOfLIS(nums):
    N = len(nums)
    dp = [1]*N
    
    for n in range(N):
        for i in range(n):
            if nums[i] < nums[n]:
                dp[n] = max(dp[n], dp[i] + 1)
    
    return max(dp)
        


# Using binary search to speed up the process and only appending to the array if need be instead of updating dynamically. O(nlogn)
def lengthOfLIS2(nums):
    N = len(nums)
    tmp = [nums[0]]

    for n in nums:
        x = bisect_left(tmp, n)
        if x == len(tmp):
            tmp.append(n)
        elif tmp[x] > n:
            tmp[x] = n
        
    return len(tmp)


print(lengthOfLIS2(nums))