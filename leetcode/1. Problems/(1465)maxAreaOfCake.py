
h = 5
w = 4
horizontalCuts = [1,2,4]
verticalCuts = [1,3]
# Output: 4

def maxArea(h,w,horizontalCuts,verticalCuts):
    
    horizontalCuts = sorted([0]+horizontalCuts+[h])
    verticalCuts = sorted([0]+verticalCuts+[w])
    
    hMax = max([horizontalCuts[i]-horizontalCuts[i-1] for i in range(1,len(horizontalCuts))])
    wMax = max([verticalCuts[i]-verticalCuts[i-1] for i in range(1,len(verticalCuts))])
    
    return (hMax*wMax)%(10**9+7)



print(maxArea(h, w, horizontalCuts, verticalCuts))