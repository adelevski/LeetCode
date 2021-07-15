

s = "LOVELY"
# Output: "lovely"

# Works but its too easy and considered "cheating" :/
# def toLowerCase(s):
#     return s.lower()

# ASCII implentation 
def toLowerCase(s):
    return "".join(chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in s)


print(toLowerCase(s))

