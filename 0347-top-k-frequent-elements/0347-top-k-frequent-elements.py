import operator
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        t=[]
        sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
        for i in sorted_d:
            t.append(i)
        return t[:k]
        