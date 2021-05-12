
s = ["h","e","l","l","o"]



def reverseString(s):
    for i in range(len(s)//2):
        s[i],s[-i-1] = s[-i-1],s[i]
    return s


print(reverseString(s))