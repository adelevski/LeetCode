

def canSum(targetSum, numbers, memo={}):
    if (targetSum in memo): return memo[targetSum]
    if (targetSum == 0): return True
    if (targetSum < 0): return False
    for num in numbers:
        remainder = targetSum - num
        if canSum(remainder, numbers, memo):
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False

# print(canSum(7, [2, 3]))
# print(canSum(5, [2, 4]))
# print(canSum(8, [2, 3, 5]))
print(canSum(300, [7, 14]))