
k = 3
contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]


def luckBalance(k, contests):
    totalLuck = 0
    numImportant = 0
    for contest in contests:
        if contest[1] == 1:
            numImportant += 1
    contests.sort(key=lambda x: x[0])
    for contest in contests:
        if contest[1] == 1 and numImportant > k:
            numImportant -= 1
            totalLuck -= contest[0]
            continue
        else:
            totalLuck += contest[0]
    return totalLuck

print(luckBalance(k, contests))