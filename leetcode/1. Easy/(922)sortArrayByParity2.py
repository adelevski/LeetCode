

nums = [4,2,5,7]



def sortByParity(nums):
    even = []
    odd = []
    for i in range(len(nums)):
        if nums[i] == 0 or nums[i] %2 == 0:
            even.append(nums[i])
        else:
            odd.append(nums[i])
    output = []
    halfLen = len(nums)//2

    for i in range(halfLen):
        output.append(even[i])
        output.append(odd[i])
    return output

print(sortByParity(nums))


