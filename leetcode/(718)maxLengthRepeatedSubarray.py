

nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]
# Output: 3

# nums1 = [0,0,0,0,0]
# nums2 = [0,0,0,0,0]
# # Output: 5

def findLength(nums1, nums2):
    N, M = len(nums1), len(nums2)
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    output = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if nums1[i - 1] == nums2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            output = max(output, dp[i][j])
    return output


print(findLength(nums1, nums2))