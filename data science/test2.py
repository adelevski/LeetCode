strings = ['a', 'bc', 'def', 'ghij']
output = ""
for x in strings:
    if len(x) % 2 == 0:
        continue
    output += x

print(output)