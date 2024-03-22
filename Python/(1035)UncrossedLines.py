
# Input: nums1 = [1,4,2], nums2 = [1,2,4]
# Output: 2

def maxUncrossedLines(nums1, nums2):
    m, n = len(nums1), len(nums2)
    if m < n:
        nums1, nums2, m, n = nums2, nums1, n, m
    dp = [0] * (n + 1)
    for i in range(1, m + 1):
        prev = 0
        for j in range(1, n + 1):
            curr = dp[j]
            if nums1[i-1] == nums2[j-1]:
                dp[j] = prev + 1
            else:
                dp[j] = max(dp[j-1], curr)
            prev = curr
    return dp[n]

nums1 = [1,4,2]
nums2 = [1,2,4]

nums1 = [2,5,1,2,5]
nums2 = [10,5,2,1,5,2]

nums1 = [1,3,7,1,7,5]
nums2 = [1,9,2,5,1]

print(maxUncrossedLines(nums1, nums2))