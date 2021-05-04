

# cost = [2, 1, 3, 5, 6]
# money = 5
# # Output = 1 3

# cost = [1, 4, 5, 3, 2]
# money = 4
# # Output = 1 4

cost = [2, 2, 4, 3]
money = 4
# Output = 1 2

def whatFlavors(cost, money):
    saved = {}
    for i,n in enumerate(cost):
        if money-n in saved:
            print(saved[money-n], i+1)
        saved[n] = i+1

print(whatFlavors(cost, money))
