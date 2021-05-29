

n = 4
# Output: 2


def totalQueens(n):
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
    return len(output)

# More efficient method 
def totalQueens(n):
    self.output = 0

    def dfs(row,ex):
        if row < n:
            for col in range(n):
                if (row,col) in ex:
                    continue
                ex_sub = set()
                r1 = r2 = r3 = row
                c1 = c2 = c3 = col

                while r1<n:
                    r1 += 1
                    ex_sub.add((r1,c1))
                while c2<n:
                    c2 += 1
                    r2 += 1
                    ex_sub.add((r2,c2))
                while c3>0:
                    c3 -= 1
                    r3 += 1
                    ex_sub.add((r3, c3))
                dfs(row+1, ex | ex_sub)
        else:
            self.output += 1
    
    dfs(0, set())

    return self.output


print(totalQueens(n))