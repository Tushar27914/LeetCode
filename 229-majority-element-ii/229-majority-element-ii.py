class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        r=[]
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        for i in d:
            if(d[i]>len(nums)/3):
                r.append(i)
        return r
        
        