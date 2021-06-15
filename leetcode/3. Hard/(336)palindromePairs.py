

words = ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]

# words = ["bat","tab","cat"]
# # Output: [[0,1],[1,0]]

# words = ["a",""]
# # Output: [[0,1],[1,0]]


# Brute force O(n^2), gets time limit 
# def palindromePairs(words):
    # def isPal(w,st,end):
    #     while st<end:
    #         if w[st]!=w[end]: return False
    #         st+=1
    #         end-=1
    #     return True
    # N = len(words)

    # for i in range(N):
    #     for j in range(M):
    #         cand = words[i]+words[j]
    #         if i!=j and isPal(cand,0,len(cand)-1):
    #             output.append([i,j])
        
    # return output


# Better solution, but for some reason it does not submit
# def palindromePairs(words):
#     def isPal(w,st,end):
#         while st<end:
#             if w[st]!=w[end]: return False
#             st+=1
#             end-=1
#         return True

#     N = len(words)
#     output = []

#     lookup = {w:i for i,w in enumerate(words)}
#     for i in range(N):
#         w = words[i]
#         if w=="":
#             for j in range(N):
#                 if i!=j and isPal(words[j],0,len(words[j])-1):
#                     output.append([i,j])
#                     output.append([j,i])
#             continue
#         bw = w[::-1]
#         if bw in lookup and lookup[bw]!=i:
#             output.append([i,lookup[bw]])

#         for k in range(1,len(words)):
#             if isPal(w,0,k-1) and w[k:][::-1] in lookup:
#                 output.append([lookup[w[k:][::-1]],i])
#             if isPal(w,k,len(w)-1) and w[:k][::-1] in lookup:
#                 output.append([i,lookup[w[:k][::-1]]])
#     return output


# Brute force except it submits since it uses a hash
def palindromePairs(words):
    output = []
    n = len(words)
    index = {}
    for i in range(len(words)):
        index[words[i]]=i
    for i in range(len(words)):
        start = words[i]
        for j in words[:i]+words[i+1:]:
            check = start+j
            if check == check[::-1]:
                output.append([i,index[j]])
    return output


print(palindromePairs(words))