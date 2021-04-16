
s = 'cdcd'

def sherlockAndAnagrams(s):
    d = {}
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            subString = ''.join(sorted(s[i:j+1]))
            d.setdefault(subString, 0)
            d[subString] += 1

    for entry in d:
        # count += int(((d[entry]-1)*d[entry])/2) # Using formula for triangular numbers (# of pairs given # of occurances)
        count += sum([i for i in range(d[entry])]) # Using normal summation method for finding # of pairs given # of occurances
    return count

print(sherlockAndAnagrams(s))
    
