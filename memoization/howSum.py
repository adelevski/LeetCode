




def howSum(targetSum, numbers, memo={}):
    if (targetSum in memo): return memo[targetSum]
    if (targetSum == 0): return []
    if (targetSum < 0): return None

    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSum(remainder, numbers)
        if (remainderResult != None):
            memo[targetSum] = [*remainderResult, num]
            return memo[targetSum]

    memo[targetSum] = None
    return None


# print(howSum(7, [2, 3]))
targetSum = 0
numbers = []
memo = {}
print(howSum(7, [5, 3, 4, 7]))
targetSum = 0
numbers = []
memo = {}
# print(howSum(7, [2, 4]))
targetSum = 0
numbers = []
memo = {}
print(howSum(8, [2, 3, 5]))
targetSum = 0
numbers = []
memo = {}
print(howSum(300, [7, 14]))