

s = "0"
# Output: true

# s = "e"
# # Output: false

# s = "."
# # Output: false

# s = ".1"
# # Output: true


# Works but is technically cheating
# def isNumber(s):
#     try:
#         float(s)
#     except:
#         return False
#     if "nf" in s: return False
#     return True


def isNumber(s):

    digit,dec,e,symbol = False, False, False, False

    for c in s:
        if c in '0123456789':
            digit = True
        elif c in '+-':
            if symbol or digit or dec:
                return False
            else:
                symbol = True
        elif c in 'Ee':
            if not digit or e:
                return False
            else:
                e = True
                symbol = False
                digit = False
                dec = False
        elif c == '.':
            if dec or e: return False
            else:
                dec = True
        else:
            return False

    return digit

