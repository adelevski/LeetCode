
# arr = [1,2,3,4,5]
# k = 4
# x = 3
# Output: [1,2,3,4]

arr = [1,2,3,4,5]
k = 4
x = -1
# Output: [1,2,3,4]


def find(arr, k, x):
    d = {}
    for i in range(len(arr)):
        d[arr[i]] = abs(arr[i]-x)
    # return d
    return sorted([k for k,v in sorted(d.items(), key=lambda x: x[1])][:k])
        


print(find(arr, k, x))