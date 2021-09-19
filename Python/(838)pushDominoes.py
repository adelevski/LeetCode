
# D = "RR.L"
# Output: "RR.L"

D = ".L.R...LR..L.."
# Output: "LL.RR.LLRRLL.."

def pushDominoes(D):
    D = "L" + D + "R"
    n, prev, ans = len(D), 0, ""
    for i in range(1, n):
        diff = i - prev - 1
        if D[i] == ".": continue
        
        if D[i] == D[prev]:
            ans += D[i]*diff     
        elif D[i] == "L" and D[prev] == "R":
            m, d = divmod(diff, 2)
            ans += "R"*m + "."*d + "L"*m
        else:
            ans += "."*diff
            
        ans += D[i]
        prev = i
    
    return ans[:-1]





print(pushDominoes(D))