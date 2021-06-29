
from collections import deque

# nums = [1,1,1,0,0,0,1,1,1,1,0]
# k = 2
# # Output: 6

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
# Output: 10

# My method, 750ms
def longestOnes(nums, k):

    window = deque()
    prevLongest = 0
    count = 0
    i = 0
    while i <= len(nums)-1:
        n = nums[i]
        if n == 1:
            window.append(n)
            i += 1
        elif n == 0 and count < k:
            window.append(n)
            count += 1
            i += 1
        else:
            if k == 0:
                window.clear()
                i += 1
                continue
            else:
                num = window.popleft()
                if num == 0:
                    count -= 1
        prevLongest = max(prevLongest, len(window))
    return prevLongest


# Timothy
def longestOnes2(nums, k):
    l, mx = 0, 0

    for r, n in enumerate(nums):
        k -= (1-n)
        if k < 0:
            k += (1-nums[l])
            l += 1
        mx = max(mx, r - l + 1)
    
    return mx


print(longestOnes(nums, k))