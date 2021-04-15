
import time

arr1 = [2, 3, 4, 1, 5, 7, 6, 9, 8, 11, 10, 12]
arr2 = [2, 3, 4, 1, 5, 7, 6, 9, 8, 11, 10, 12]

# First implementation, for AND while loop
def minimumSwaps(arr):
    swaps = 0
    for i in range(len(arr)):
        while(arr[i] != i+1):
            swapIndex = arr[i] - 1
            valAtIndex = arr[i]
            valAtSwapIndex = arr[swapIndex]
            arr[i] = valAtSwapIndex
            arr[swapIndex] = valAtIndex
            swaps += 1

    return swaps, arr

# Second implementation, just one while loop
def minimumSwaps2(arr):
    i = 0
    swaps = 0
    while i < len(arr):
        if arr[i] - 1 == i:
            i+=1
        else:
            k = arr[i] - 1
            arr[k],arr[i] = arr[i],arr[k]
            swaps += 1
    return swaps, arr

print(minimumSwaps(arr1))
print(minimumSwaps2(arr2))

