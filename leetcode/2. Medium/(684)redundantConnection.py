

edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]


def findEdges(edges):
    root = [0] + list(set([num for pair in edges for num in pair]))
        
    def rec(x):
        if root[x] == x:
            return x
        return rec(root[x])

    for x,y in edges:
        xr,yr = rec(x), rec(y)
        if xr == yr: return [x,y]
        elif x == xr: root[x] = yr
        elif y == yr: root[y] = xr
        else:
            root[xr] = yr
    

print(findEdges(edges))