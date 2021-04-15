
m = ['two', 'times', 'three', 'is', 'not', 'four']
n = ['two', 'times', 'two', 'is', 'four']

def checkMagazine(magazine, note):
    magDict = {}
    noteDict = {}
    for word in magazine:
        if word not in magDict:
            magDict[word] = 1
        else:
            magDict[word] += 1
    for word in note:
        if word not in noteDict:
            noteDict[word] = 1
        else:
            noteDict[word] += 1

    for word in note:
        if word not in magDict:
            print('No')
            return
        elif word in magDict and magDict[word] == 1:
            magDict.pop(word)
        else:
            magDict[word] -= 1
    print('Yes')
    return

print(checkMagazine(m, n))