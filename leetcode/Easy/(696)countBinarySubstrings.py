from collections import deque

s = "00110011"
# Output = 6, "0011", "01", "1100", "10", "0011", and "01"

# s = "10101"
# # Output = 4, "10", "01", "10", "01"

# First solution, O(n) time complexity
def countBinarySubstrings(s):
    q = deque()
    output = 0
    for c in s:
        while q and q[-1] == c and q[0] != c:
            q.pop()
        if q and q[-1] != c:
            q.pop()
            output += 1
        q.appendleft(c)
    return output

# Second solution, O(n) time complexity but no queue 
def countBinarySubstrings2(s):
    N = len(s)
    prev, cur = 0, 1
    output = 0
    for i in range(1, N):
        if s[i] != s[i-1]:
            output += min(prev, cur)
            prev = cur
            cur = 1
        else:
            cur += 1
    return output + min(prev, cur)

print(countBinarySubstrings(s))
