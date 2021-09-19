
nums = [1,0,-1,0,-2,2]
target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]


def fourSum(nums, target):
    N = len(nums)
    seen = set()
    ans = set()
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                lastNumber = target - nums[i] - nums[j] - nums[k]
                if lastNumber in seen:
                    arr = sorted([nums[i], nums[j], nums[k], lastNumber])
                    ans.add((arr[0], arr[1], arr[2], arr[3]))
        seen.add(nums[i])
    return ans




print(fourSum(nums, target))