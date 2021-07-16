





arr = [9,4,2,10,7,8,8,1,9]
# Output: 5


def maxTurbulenceSize(arr):
    N = len(arr)
    dp = [[1, 1] for i in range(N)]
    output = 1
    for i in range(1, N):
        if arr[i] < arr[i-1]:
            dp[i][0] = dp[i-1][1] + 1
        elif arr[i] > arr[i-1]:
            dp[i][1] = dp[i-1][0] + 1
        output = max(output, max(dp[i]))
    return dp


print(maxTurbulenceSize(arr))