
# n = 3
# Output: 2
# Explanation: arr = [1, 3, 5]

n = 6
# Output: 9
# Explanation: arr = [1, 3, 5, 7, 9, 11, 13]

def minOps(n):
    arr = []
    for i in range(n):
        arr.append(2*i+1)
    
    target = sum(arr)/n
    output = 0

    if n%2 == 0:
        for i in arr[n//2:]:
            output += i-target
        return int(output)

    else:
        for i in arr[n//2+1:]:
            output += i-target
        return int(output)



print(minOps(n))