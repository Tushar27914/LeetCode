class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum1=sum(nums)
        t=0
        s=[]
        for i in range(1,len(nums)+1):
            s.append(sum1-sum(nums[i:]))
        return s
            
#         s=[]
#         for i in range(len(nums)):
#             nums[i]=nums[i]+nums[i-1]
#             s.append(nums[i])
#         return s
           
        