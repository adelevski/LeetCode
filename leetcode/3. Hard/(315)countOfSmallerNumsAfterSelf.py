
from sortedcontainers import SortedList

nums = [5,2,6,1]
# Output: [2,1,1,0]

def countSmaller(nums):

    s = SortedList()
    output = []

    for n in nums[::-1]:
        ans = SortedList.bisect_left(s, n)
        output.append(ans)
        s.add(n)
    return reversed(output)


print(countSmaller(nums))


