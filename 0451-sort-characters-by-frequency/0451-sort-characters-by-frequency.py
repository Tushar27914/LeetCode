import operator
class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]]+=1
            else:
                d[s[i]]=1
        sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
        u=[]
        for i in sorted_d:
            u.append(i*sorted_d[i])
        return "".join(u)