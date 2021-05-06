
# Due to the nature of this problem it will not run properly in a personal environment 

class WordFilter:

    def __init__(self, words):
        tmp = {}
        for index,word in enumerate(words):
            tmp[word] = index
        self.words = [(k + '#' + k,v) for k,v in tmp.items()]


    def f(self, prefix, suffix):
        ps = suffix + '#' + prefix 
        for word,index in reversed(self.words):
            if ps in word: return index
        return -1


wordFilter = WordFilter(["apple"])
print(wordFilter.f("a", "e")) # return 0, because the word at index 0 has prefix = "a" and suffix = 'e".

