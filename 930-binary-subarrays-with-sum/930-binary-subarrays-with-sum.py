class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        summap={0:1}
        s=0
        cnt=0
        for a in nums:
            s+=a
            if s-goal in summap:
                cnt+=summap[s-goal]
            summap[s]=summap.get(s,0)+1
        return cnt
        
        
        # c=0
        # for i in range(len(nums)):
        #     nums[i]=nums[i]+nums[i-1]
        # for j in range(len(nums)):
        #     if(nums[j]==goal):
        #         c+=1
        #     if(nums[j]-goal in nums):
        #         c+=1
        # return c

#         c=0
#         l=[]
#         for i in range(len(nums)+1):
#             for j in range(i):
#                 l.append(nums[j:i])
#         for k in l:
#             if(sum(k)==goal):
#                 c+=1
#         return c
        
     
                
        
    