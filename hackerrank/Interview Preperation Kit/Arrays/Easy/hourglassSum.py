
arr = [[1, 1, 1, 0, 0, 0],
       [0, 5, 0, 0, 5, 0],
       [1, 1, 1, 0, 0, 0],
       [0, 0, 2, 4, 4, 0],
       [0, 5, 0, 2, 5, 0],
       [0, 0, 1, 2, 4, 0]]


def hourglassSum(arr):
    currentMax = -63 # Minimum hourglass sum since the smallest possible value is -9, and an hourglass of all -9's is -63 (-9*7)
    for i in range(1, 5):
        for j in range(1, 5):
            glass = (arr[i-1][j-1]+arr[i-1][j]+arr[i-1][j+1]+
                    arr[i][j]+
                    arr[i+1][j-1]+arr[i+1][j]+arr[i+1][j+1])
            if glass >= currentMax:
                currentMax = glass
    return currentMax



print(hourglassSum(arr))

