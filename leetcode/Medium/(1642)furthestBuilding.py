from heapq import heappop, heappush

heights = [4,2,7,6,9,14,12]
bricks = 5
ladders = 1
# Output: 4

# heights = [4,12,2,7,3,18,20,3,19]
# bricks = 10
# ladders = 2
# #Output = 7

# heights = [14,3,19,3]
# bricks = 17
# ladders = 0
# #output = 3

def furthestBuilding(heights, bricks, ladders):
    N = len(heights)
    heap = []
    for i in range(N-1):
        h = heights[i+1]-heights[i]
        if h <= 0: 
            continue
        heappush(heap, h)
        if len(heap) > ladders:
            min_h = heappop(heap)
            bricks -= min_h
        if bricks < 0:
            return i
    return N-1

print(furthestBuilding(heights, bricks, ladders))
                    
            


