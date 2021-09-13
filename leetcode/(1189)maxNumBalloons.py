
# text = "nlaebolko"
# Output: 1

# text = "loonbalxballpoon"
# Output: 2

# text = "leetcode"
# Output: 0

text = 'krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw'
# Output: 10

def maxNumBalloons(text):
    singles_dict = {'b': 0, 'a': 0, 'n': 0}
    doubles_dict = {'l': 0, 'o': 0}
    n = len(text)
    for i in range(n):
        if text[i] in singles_dict.keys():
            singles_dict[text[i]] += 1
        elif text[i] in doubles_dict.keys():
            doubles_dict[text[i]] += 1
    return min(min(singles_dict.values()), min(doubles_dict.values()) // 2)

print(maxNumBalloons(text))