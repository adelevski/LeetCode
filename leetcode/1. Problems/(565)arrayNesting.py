

nums = [5,4,0,3,1,6,2]
# Output: 4





def arrayNesting(nums):
    ans = 0
    for x in nums:
        if x == -1: continue
        cnt = 0
        while nums[x] != -1:
            cnt += 1
            nums[x], x = -1, nums[x]
        ans = max(ans, cnt)
            
    return ans
    


print(arrayNesting(nums))