


nums = [4,2,4,5,6]
# Output: 17 ([2,4,5,6])

# nums = [5,2,1,2,5,2,1,2,5]
# # Output: 8 ([5,2,1] or [1,2,5])

# Sliding window technique
def maxUniqueSub(nums):
    seen = {} #integer:index
    mx,output = 0,0
    l = 0

    for i,n in enumerate(nums):
        if n in seen:
            while l<seen[n]+1:
                mx -= nums[l]
                l += 1
        seen[n] = i
        mx += n
        output = max(output,mx)
    return output

print(maxUniqueSub(nums))