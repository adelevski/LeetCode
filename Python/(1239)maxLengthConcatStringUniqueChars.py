

arr = ["un","iq","ue"]
# Output: 4 



def maxLength(arr):
    n = len(arr)
    ans = 0
    for mask in range(1 << n):
        seen = set()
        isValid = True
        strSize = 0
        for i in range(n):
            if (mask >> i) & 1 == 0: continue
            for c in arr[i]:
                if c in seen:   # If c is already existed then it's invalid subsequence.
                    isValid = False
                    break
                seen.add(c)
                strSize += 1
            if not isValid: break
        if isValid and strSize > ans:
            ans = strSize
    return ans


print(maxLength(arr))