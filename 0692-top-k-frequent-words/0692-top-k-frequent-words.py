class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(sorted(words)).most_common(k)
        ans = []
        for i in range(k):
            ans.append(c[i][0])
        return ans
        
        # d={}
        # for i in range(len(words)):
        #     if words[i] in d:
        #         d[words[i]]+=1
        #     else:
        #         d[words[i]]=1
        # t=[]
        # sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
        # for i in sorted_d:
        #     t.append(sorted_d[i])
        # return t
        
        