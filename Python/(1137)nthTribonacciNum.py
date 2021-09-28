

n = 4
# Output: 4


n = 25
# # Output: 1389537



def tribonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    output = [0, 1, 1]
    for i in range(3, n+1):
        output.append(output[i-1] + output[i-2] + output[i-3])
    return output[-1]


print(tribonacci(n))