
# Button 1: Flips the status of all the bulbs.
# Button 2: Flips the status of all the bulbs with even labels (i.e., 2, 4, ...).
# Button 3: Flips the status of all the bulbs with odd labels (i.e., 1, 3, ...).
# Button 4: Flips the status of all the bulbs with a label j = 3k + 1 where k = 0, 1, 2, ... (i.e., 1, 4, 7, 10, ...).

n, presses = 1, 1
# Output: 2
# Status can be: [on], [off].

# n, presses = 2, 1
# Output: 3
# Status can be: [on, off], [off, on], [off, off].

# n, presses = 3, 1
# Output: 4
# Status can be: [off, on, off], [on, off, on], [off, off, off], [off, on, on].

# Stupidest programming challange of all time, can be easily hardcoded like this:
def flipLights(n, presses):
    if presses == 0:
        return 1
    if n >= 3:
        return 4 if presses == 1 else 7 if presses == 2 else 8
    if n == 2:
        return 3 if presses == 1 else 4
    if n == 1:
        return 2

print(flipLights(n, presses))


