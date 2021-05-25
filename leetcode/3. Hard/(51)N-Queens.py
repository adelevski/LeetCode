

n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]


def solveNQueens(n):
        output = []
        def dfs(l,excluded): #{(1,2),(2,3)}
            r = len(l)
            if r<n:
                # check every column w/ tmp string
                for c in range(n):
                    if (r,c) in excluded: continue # got queen in that row/column
                    ex = set()
                    tmp = "."*(c)+"Q"+"."*(n-c-1)
                    for r1 in range(r,n): # bottom
                        ex.add((r1,c))
                    r2 = r3 = r
                    c2 = c3 = c
                    while c2 < n: # bottom diagonal right
                        r2+=1
                        c2+=1
                        ex.add((r2,c2))                    
                    while c3 > 0: # bottom diagonal left
                        r3 += 1
                        c3 -= 1
                        ex.add((r3,c3))
                    dfs(l+[tmp], excluded | ex)
            else:
                output.append(l)
        dfs([],set())
        return output

print(solveNQueens(n))

