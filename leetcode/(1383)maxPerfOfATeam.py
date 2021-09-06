from heapq import heappop,heappush

n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 2
# Output: 60

# n = 6
# speed = [2,10,3,1,5,8]
# efficiency = [5,4,3,9,7,2]
# k = 3
# # Output: 68

# n = 6
# speed = [2,10,3,1,5,8]
# efficiency = [5,4,3,9,7,2]
# k = 4
# # Output: 72

def maxPerf(n,speed,efficiency,k):
    tmp = sorted(zip(efficiency,speed))
    
    output = 0
    h = []
    sm = 0
    for e in range(n-1,-1,-1):
        heappush(h,tmp[e][1])
        sm += tmp[e][1]
        if len(h)>k:
            sm-=heappop(h)
        output = max(output, sm*tmp[e][0])
    return output % (10**9+7)


print(maxPerf(n, speed, efficiency, k))


