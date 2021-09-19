

s = "ADOBECODEBANC"
t = "ABC"
# Output: "BANC"


def minWindow(s, t):
    if t=='': return ''
    countT,window={},{}
    for char in t:
        countT[char]=1+countT.get(char,0)
    have,need=0,len(countT)
    res,resL=[-1,-1],float('infinity')
    left=0
    for right in range(len(s)):
        char=s[right]
        window[char]=1+window.get(char,0)
        if char in countT and window[char]==countT[char]:
            have+=1
        while have==need:
            if (right-left+1)<resL:
                resL=right-left+1
                res=[left,right]
            window[s[left]]-=1
            if s[left] in countT and window[s[left]]<countT[s[left]]:
                have-=1
            left+=1
    left,right=res
    return s[left:right+1] if resL!=float('infinity') else  ''




print(minWindow(s, t))