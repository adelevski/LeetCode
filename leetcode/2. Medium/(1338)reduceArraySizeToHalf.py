
# arr = [3,3,3,3,5,5,5,2,2,7]
# Output: 2

arr = [7,7,7,7,7,7]
# # Output: 1

# arr = [1,2,3,4,5,6,7,8,9,10]
# # Output: 5

# My method
def minSetSize(arr):
    N = len(arr)
    target = N//2 + 1
    d = {}
    for i in arr:
        d.setdefault(i, 0)
        d[i] += 1

    output = 0
    for k,v in sorted(d.items(), key=lambda x: x[1], reverse=True):
        N -= v
        output += 1
        if N < target:
            break
    return output
        

print(minSetSize(arr))