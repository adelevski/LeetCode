
# ratings = [1,0,2]
# Output: 5

# ratings = [1,2,2]
# # Output: 4

# ratings = [1,3,2,2,1]
# Output = 7

ratings = [1,2,87,87,87,2,1]
# Output = 13

def candy(ratings):
    N = len(ratings)
    output = [1]*N

    for i in range(1, N):
        if ratings[i] > ratings[i-1]:
            output[i] = output[i-1] + 1
    
    for i in range(N-2,-1,-1):
        if ratings[i] > ratings[i+1]:
            output[i] = max(output[i+1] + 1, output[i])

    return sum(output)

print(candy(ratings))