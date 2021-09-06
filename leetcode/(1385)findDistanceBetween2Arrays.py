

arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 2
# Output: 2

# Naive solution O(n^2)
def findDistance(arr1, arr2, d):
    output = []
    for i in range(len(arr1)):
        a = False
        for j in range(len(arr2)):
            tmp = abs(arr1[i]-arr2[j])
            if tmp > d:
                continue
            else:
                a = True
                break
        if a == False:
            output.append(arr1[i])
    return len(output)


print(findDistance(arr1, arr2, d))