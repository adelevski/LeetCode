
# n = 8
# s = 'mnonopoo'
# Output = 12 (m, n, o, n, o, p, o, o, non, ono, opo, oo)

n = 5
s = 'asasd'
# Output = 7 (a, s, a, s, d, asa, sas)

# n = 7
# s = 'abcbaba'
# # Output = 10 (a, b, c, b, a, b, a, bcb, bab, aba)

# n = 4
# s = 'aaaa'
# # Output = 10 (a, a, a, a, aa, aa, aa, aaa, aaa, aaaa)

def substrCount(n, s):
    result = 0
    i = 0
    while (i < n):
        char_count = 1
        while (i + 1 < n and s[i] == s[i+1]):
            i += 1
            char_count += 1
        result += int(char_count * (char_count + 1) / 2)
        i += 1
    
    for i in range(1, n):
        char_count = 1
        while(i + char_count < n and i - char_count >= 0 and 
                s[i] != s[i-1] and s[i - char_count] == s[i + char_count] and
                s[i - 1] == s[i - char_count]):
            char_count += 1
        result += char_count - 1

    return result

print(substrCount(n, s))
    

