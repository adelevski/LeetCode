



# n = 5
# # Output: true

n = 7
# Output: false

# n = 11
# # Output: false

# Traditional method, no function calls
# def hasAltBit(n):
#     b = []
#     while n>0:
#         d=n%2
#         b.append(d)
#         n=n//2
#     b.reverse()
#     for i in range(len(b)-1):
#         if b[i+1] == b[i]:
#             return False
#     return True

# Using bin function
# def hasAltBit(n):
#     b = bin(n)
#     for i in range(1,len(b)):
#         if b[i-1] == b[i]:
#             return False
#     return True

# Using f-strings 
# def hasAltBit(n):
#     b = f"{n:b}"
#     for i in range(1,len(b)):
#         if b[i-1] == b[i]:
#             return False
#     return True

# Using format()
def hasAltBit(n):
    b = format(n, "b")
    for i in range(1, len(b)):
        if b[i-1] == b[i]:
            return False
    return True
    

print(hasAltBit(n))