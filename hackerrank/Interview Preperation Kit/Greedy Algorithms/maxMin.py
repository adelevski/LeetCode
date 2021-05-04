import sys 

k = 4
arr = [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]

def maxMin(k, arr):
    arr.sort()
    unfairness = sys.maxsize
    for i in range(len(arr)-k+1):
        unfairness = min(unfairness, arr[i+k-1] - arr[i])
    return unfairness

print(maxMin(k, arr))