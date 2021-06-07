

s = "12"
# Output: 2

s = "226"
# Output: 3


def numDecodings(s):
    if not s or s[0]=='0': return 0
    if len(s)==1: return 1
    N = len(s)
    dp = [0]*N
    dp[0] = 1

    if s[1] != '0':
        if 10<=int(s[0:2])<= 26:
            dp[1] = 2
        else:
            dp[1] = 1
    else:
        if 10<=int(s[0:2])<= 26:
            dp[1] = 1
        else:
            return 0

    for i in range(2, N):
        if s[i] != "0":
            if 10<=int(s[i-1:i+1])<= 26:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i]=dp[i-1]
        else:
            if 10<=int(s[i-1:i+1])<= 26:
                dp[i] = dp[i-2]
            else:
                return 0

    return dp[-1]



print(numDecodings(s))