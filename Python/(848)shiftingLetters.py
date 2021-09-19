
# s = "abc"
# shifts = [3,5,9]
# Output: "rpl"

s = "aaa"
shifts = [1,2,3]
# Output: "gfd"


def shiftingLetters(s, shifts):
    n = len(s)
    for i in range(n-2, -1, -1):
        shifts[i] += shifts[i+1]
        
    ans = []
    for i, c in enumerate(s):
        idx = (ord(c) - ord('a') + shifts[i]) % 26
        ans.append(chr(idx + ord('a')))
    return "".join(ans)


print(shiftingLetters(s, shifts))