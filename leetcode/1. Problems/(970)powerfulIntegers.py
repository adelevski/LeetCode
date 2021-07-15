
x = 2
y = 3
bound = 10


def powerfulIntegers(x, y, bound):
    X, Y, output = [1], [1], []

    while X[-1] < bound and x != 1:
        X.append(X[-1] * x)

    while Y[-1] < bound and y != 1:
        Y.append(Y[-1] * y)
    
    c = ((x,y) for x in X for y in Y)

    for i, j in c:
        if i + j <= bound:
            output.append(i + j)
    
    return list(set(output))

print(powerfulIntegers(x, y, bound))