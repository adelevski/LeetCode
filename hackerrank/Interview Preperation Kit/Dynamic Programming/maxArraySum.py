
arr = [-2, 1, 3, -4, 5]

def maxSubsetSum(arr):
    N = len(arr)
    dp = [0]*N
    if N == 1:
        return arr[0]
    if N == 2:
        return max(arr[0], arr[1])
    else:
        dp[0], dp[1] = arr[0], max(arr[0], arr[1])
        for i in range(2,N):
            dp[i] = max(arr[i], dp[i-1], dp[i-2]+arr[i])
    return max(dp)


print(maxSubsetSum(arr))