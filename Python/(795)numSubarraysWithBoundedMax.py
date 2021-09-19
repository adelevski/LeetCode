
# nums = [2,1,4,3]
# left = 2
# right = 3
# # Output: 3


nums = [2,9,2,5,6]
left = 2
right = 8
# Output: 7


def numSubarrays(nums,left,right):
    l_stack,i_stack,output = 0,0,0
    last_i = -1

    for i,n in enumerate(nums):
        if n<left:
            if i_stack > 0:
                output += i_stack + l_stack
                output -= i-last_i-1
            l_stack += 1
        elif left<=n<=right:    
            output += i_stack + l_stack + 1
            i_stack += 1
            last_i = i
        else:
            l_stack = 0
            i_stack = 0


    return output

print(numSubarrays(nums, left, right))