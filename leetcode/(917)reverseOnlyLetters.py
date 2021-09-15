

s = "ab-cd"
# Output: "dc-ba"

s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"

s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"

def reverseOnlyLetters(s):
    lst = []
    for char in s:
        lst.append(char)
    left = 0
    right = len(lst) - 1
    while left < right:
        if (65 <= ord(lst[left]) <= 90 or 97 <= ord(lst[left]) <= 122) and (65 <= ord(lst[right]) <= 90 or 97 <= ord(lst[right]) <= 122):
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1
        elif (65 <= ord(lst[left]) <= 90 or 97 <= ord(lst[left]) <= 122):
            right -= 1
        elif (65 <= ord(lst[right]) <= 90 or 97 <= ord(lst[right]) <= 122):
            left += 1
        else:
            left += 1
            right -= 1
    return "".join(lst)




print(reverseOnlyLetters(s))