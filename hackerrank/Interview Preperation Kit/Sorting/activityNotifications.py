

expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
d = 5

# expenditure = [10, 20, 30, 40, 50]
# d = 3

def activityNotifications(expenditure, d):
    dic = {}

    def get_median(idx):
        s = 0
        for i in range(201):
            freq = 0
            if i in dic:
                freq = dic[i]
            s += freq
            if s>=idx:
                return i

    result = 0

    for i in range(len(expenditure)):
        val = expenditure[i]

        if i >= d:
            med = get_median(d//2 + d%2)

            if d%2 == 0:
                if val >= med + get_median(d//2 + 1):
                    result += 1
            else:
                if val>= med*2:
                    result += 1
    
        if val not in dic:
            dic[val] = 1
        else:
            dic[val] += 1

        if i >= d:
            prev = expenditure[i-d]
            dic[prev] -= 1

    return result

print(activityNotifications(expenditure, d))


