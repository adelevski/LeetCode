
# arr = [1,2,3,4,5]
# k = 4
# x = 3
# Output: [1,2,3,4]

# arr = [1,2,3,4,5]
# k = 4
# x = -1
# Output: [1,2,3,4]

arr = [0,1,1,1,2,3,6,7,8,9]
k = 9
x = 4


def find(arr, k, x):
    d = {}
    for i in range(len(arr)):
        d.setdefault(arr[i], [0, abs(arr[i]-x)])
        d[arr[i]][0] += 1
    lst = [v for k,v in d.items()]
    return lst
        


print(find(arr, k, x))