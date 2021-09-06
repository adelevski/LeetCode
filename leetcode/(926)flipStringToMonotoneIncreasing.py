
# s = "00110"
# Output: 1

# s = "010110"
# Output: 2

s = "00011000"
# Output: 2





def minFlips(s):
    ones = zeroes = 0
    result = 0

    for c in s:
        if c == '1':
            ones += 1
        else:
            if ones:
                zeroes += 1
                if zeroes == ones:
                    result += ones
                    ones = zeroes = 0

    result += zeroes
    return result




print(minFlips(s))