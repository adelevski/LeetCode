
arr = [-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]


def minimumAbsoluteDifference(arr):
    if len(arr) != len(list(set(arr))):
        return 0
    else:
        return min(arr[i+1]-arr[i] for i in range(len(arr)-1))


arr = sorted(arr)
print(minimumAbsoluteDifference(arr))
