from heapq import heappush, heappop


grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
# Output: 16



def swimInWater(grid):
    N,M = len(grid[0]),len(grid)
    h = [(grid[0][0],0,0)]
    visited = set()
    direction = [(0,1),(0,-1),(1,0),(-1,0)]
    output = 0

    while h:
        mx,r,c = heappop(h)
        output = max(mx,output)
        if (r,c)==(M-1,N-1):
            break
        for dx,dy in direction:
            rx,cx = r+dx, c+dy
            if 0<=rx<M and 0<=cx<N and (rx,cx) not in visited:
                heappush(h,(grid[rx][cx],rx,cx))
                visited.add((rx,cx))
    return output


print(swimInWater(grid))