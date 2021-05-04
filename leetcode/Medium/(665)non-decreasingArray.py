

nums = [4, 2, 3]
# Output = True

# nums = [4, 2, 1]
# # Output = False

# nums = [3,4,2,3]
# # Output = False

def checkPossibility(nums):
    N = len(nums)
    mx, mn = float('-inf'), float('inf')
    n, m = 0, 0

    for i in range(N):
        if nums[i]<mx:
            n += 1
        mx = max(mx, nums[i])
    for i in range(N-1, -1, -1):
        if nums[i] > mn:
            m += 1
        mn = min(mn, nums[i])
    return n <= 1 or m <= 1

print(checkPossibility(nums))