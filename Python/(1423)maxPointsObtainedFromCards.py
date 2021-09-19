

# cardPoints = [1,2,3,4,5,6,1]
# k = 3
# # Output = 12

# cardPoints = [2,2,2]
# k = 2
# # Output = 4

# cardPoints = [9,7,7,9,7,7,9]
# k = 7
# # Output = 55

# cardPoints = [1,1000,1]
# k = 1
# # Output = 1

cardPoints = [1,79,80,1,1,1,200,1]
k = 3
# Output = 202

def maxScore(cardPoints, k):
    frontSum, backSum = [0],[0]
    for i in range(k):
        frontSum.append(frontSum[-1]+cardPoints[i])
        backSum.append(backSum[-1]+cardPoints[-i-1])
    allCombinations = [frontSum[i]+backSum[k-i] for i in range(k+1)]
    print(allCombinations)
    return max(allCombinations)

print(maxScore(cardPoints, k))