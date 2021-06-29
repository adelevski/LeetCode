
# s = "abbaca"
# Output: "ca"

s = "azxxzy"
# Output: "ay"


## Recursion.... very shitty (O(n^2))
def removeDuplicates(s):
    
    def rec(s):
        if len(s) >= 2:
            for i in range(1, len(s)):
                if s[i-1] != s[i]:
                    continue
                else:
                    s = s[:i-1]+s[i+1:]
                    return rec(s)
        return s

    return rec(s)

# Using a stack, much more efficient (O(n))
def removeDuplicates2(s):
    stack = []

    for c in s:
        if stack and stack[-1]==c:
            stack.pop()
        else:
            stack.append(c)

    return "".join(stack)

print(removeDuplicates(s))
print(removeDuplicates2(s))