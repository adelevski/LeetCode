

n = '82734'
# Output: 8


# My own naive method, not realizing that the max digit in the number given ends up being the answer... duhhhh....
def minPartitions(n):
    current = str(n)
    output = []
    while int(current)>0:
        tmp = ''
        for i in range(len(current)):
            if current[i] == '0':
                tmp += '0'
            else:
                tmp += '1'
        output.append(tmp)
        current = str(int(current)-int(tmp))
    return len(output)
            


# Shortest and simplest way to do this having realized that the max digit of the given number is the answer
def minPartitions(n):
    return max(n)

