
# text = "nlaebolko"
# Output: 1

# text = "loonbalxballpoon"
# Output: 2

# text = "leetcode"
# Output: 0

text = 'krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw'
# Output: 10

def maxNumBalloons(text):
    d = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
    n = len(text)
    for i in range(n):
        if text[i] in d.keys():
            d[text[i]] += 1
    return min(d['b'], d['a'], d['l']//2, d['o']//2, d['n'])

print(maxNumBalloons(text))