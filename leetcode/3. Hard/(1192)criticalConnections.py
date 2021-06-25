# Because of the nature of this problem, it will not run in personal env

n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]

def criticalConnections(n, connections):
    dis = [0]*n
    low = [0]*n
    self.time = 0
    visited = set()
    output = []
    graph = defaultdict(list)

    for s, t in connections:
        graph[s].append(t)
        graph[t].append(s)
    
    def dfs(cur, prev):
        visited.add(cur)
        self.time += 1
        dis[cur] = low[cur] = self.time
        
        for next in graph[cur]:
            if next not in visited:
                dfs(next, cur)
                low[cur] = min(low[cur], low[next])
            elif next != prev:
                low[cur] = min(low[cur], dis[next])
            if low[next] > dis[cur]:
                output.append([cur, next])
        
    dfs(0, -1)
    return output

print(criticalConnections(n, connections))