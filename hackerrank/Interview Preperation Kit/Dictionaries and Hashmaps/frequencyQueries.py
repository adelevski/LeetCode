from collections import Counter

queries = [(1, 3), (2, 3), (3, 2), (1, 4), (1, 5), (1, 5), (1, 4), (3, 2), (2, 4), (3, 2)]

def freqQuery(queries):
    d = Counter()
    dvals = Counter()
    responses = []
    for op, value in queries:
        if op == 1:
            dvals[d[value]] -=1
            d[value] += 1
            dvals[d[value]] += 1
        if op == 2:
            if d[value] > 0:
                dvals[d[value]] -= 1
                d[value] -= 1
                dvals[d[value]]+= 1
        if op == 3:
            responses.append(1 if dvals[value] > 0 else 0)
    return responses
            
print(freqQuery(queries))