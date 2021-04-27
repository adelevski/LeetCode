
words = ["cat","bt","hat","tree"]
chars = "atach"

def countChars(words, chars):
    d = {}
    output = 0
    for char in chars:
        d.setdefault(char, 0)
        d[char] += 1
    # print(f"our d={d}")
    for word in words:
        temp = d.copy()
        num = 0
        # print(f"checking word={word}, temp = {temp}")
        for char in word:
            # print(f"checking char={char} from word={word}. Current temp = {temp}")
            if char in temp and temp[char] > 0:
                temp[char] -= 1
                num += 1
                # print(f"new temp={temp}, new num={num}")
            else:
                # print(f'no, breaking')
                num = 0
                break
        output += num
        # print(f"finished that word, new output = {output} after adding num={num}")
    return output

print(countChars(words, chars))