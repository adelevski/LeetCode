# Due to the nature of this problem, it will not run in a personal environment

left = 4
right = 1000

nums = []
for i in range(1, 10**5):
    odd = int(str(i)+str(i)[:-1][::-1])**2
    even = int(str(i)+str(i)[::-1])**2
    if str(odd)==str(odd)[::-1]: nums.append(odd)
    if str(even)==str(even)[::-1]: nums.append(even)
nums = sorted(list(set(nums)))

def superpalindromesInRange(self, left, right):
    output = []
    for n in self.nums:
        if int(left)<=n<=int(right):
            output.append(n)
    return len(output)

print(superPalindromes(left, right))