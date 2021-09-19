
s = "(123)"
# Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]

# s = "(00011)"
# # Output:  ["(0.001, 1)", "(0, 0.011)"]
# # Explanation: 0.0, 00, 0001 or 00.01 are not allowed.

# s = "(0123)"
# # Output: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]

# s = "(100)"
# # Output: [(10, 0)]
# # Explanation: 1.0 is not allowed.



def ambiguousCoordinates(s):
    s = s[1:-1]
    N = len(s)
    output = []
    for i in range(1, N):
        a = s[:i]
        b = s[i:]
        for first in unpack(a):
            for second in unpack(b):
                output.append(f"({first}, {second})")
    return output

def unpack(x):
    tmp = []
    N = len(x)
    # without decimal point?
    if x[0] != "0" or x == "0":
        tmp.append(x)

    for i in range(1, N):
        if (x[:i] == "0" or x[0] != "0") and x[-1] != "0":
            cand = x[:i] + "." + x[i:]
            tmp.append(cand)
    return tmp

print(ambiguousCoordinates(s))