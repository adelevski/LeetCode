

# products = ["mobile","mouse","moneypot","monitor","mousepad"]
# searchWord = "mouse"

products = ["bags","baggage","banner","box","cloths"]
searchWord = "bags"
# Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]


def suggestedProducts(products, searchWord):
    output = []
    products.sort()

    for i,c in enumerate(searchWord):
        tmp = []
        for p in products:
            if i<len(p) and c==p[i]:
                tmp.append(p)
        output.append(tmp[:3])
        products = tmp
    return output



print(suggestedProducts(products, searchWord))


