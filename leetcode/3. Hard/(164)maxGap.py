
from collections import defaultdict

nums = [3,6,9,1]
# Output: 3

# Gets accepted but is technically cheating since .sort() method is nlogn, and this needs to run in linear time (and have linear extra space)
# def maxGap(nums):
    # n = len(nums)
    # if n < 2: return 0
    
    # nums.sort()

    # output = 0
    # for i in range(1,n):
    #     output = max(output, abs(nums[i-1]-nums[i]))


# This is using the bucket technique from "Bucket Sort", and achieves N time and N space
def maxGap(nums):
    n = len(nums)
    if n < 2: return 0
    lo,hi = min(nums),max(nums)
    B = defaultdict(list)
    for num in nums:
        if num==hi:
            ind = n-1
        else:
            ind = (abs(lo-num)*(n-1))//(hi-lo)
        B[ind].append(num)
    buckets = []
    for i in range(n):
        if B[i]:
            buckets.append((min(B[i]),max(B[i])))
    output = 0
    for i in range(1, len(buckets)):
        output = max(output, abs(buckets[i-1][-1]-buckets[i][0]))
    return output

print(maxGap(nums))

