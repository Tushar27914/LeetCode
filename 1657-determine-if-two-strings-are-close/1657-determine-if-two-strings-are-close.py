class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1=list(word1)
        word2=list(word2)
        if set(word1)!=set(word2):
            return False
        if len(set(word1))!=len(set(word2)):
            return False
        if len(word1)!=len(word2):
            return False
        if sorted(word1)==sorted(word2):
            return True
        
        d1=sorted(Counter(word1).values())
        d2=sorted(Counter(word2).values())
        if d1==d2:
            return True
        else:
            return False
        
        
        

        
#         if len(word1)!=len(word2):
#             return False
#         d={}
#         for i in range(len(word1)):
#             if word1[i] in d:
#                 d[word1[i]]+=1
#             else:
#                 d[word1[i]]=1
        
#         s={}
#         for j in range(len(word2)):
#             if word2[j] in s:
#                 s[word2[j]]+=1
#             else:
#                 s[word2[j]]=1
#        # print(s)
#        # print(d)
#         t=[]
#         u=[]
#         for i in d:
#             t.append(d[i])
#         t.sort()
#         for j in s:
#             u.append(s[j])
#         for i in t:
#             for j in u:
#                 if i==j:
#                     return True
#                 else:
#                     return False