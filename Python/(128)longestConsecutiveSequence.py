


nums = [100,4,200,1,3,2]
# Output: 4

# nums = [0,3,7,2,5,8,4,6,0,1]
# # Output: 9


def longestConsecutive(nums):
    nums = set(nums)
    output = 0

    for n in nums:
        if n-1 not in nums:
            start = n
            while start in nums:
                start += 1
            output = max(output, start-n)
    return output



print(longestConsecutive(nums))