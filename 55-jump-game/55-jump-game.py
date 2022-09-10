class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cj=nums[0]
        for i in range(1,len(nums)):
            cj-=1
            if cj<0:
                return False
            cj=max(nums[i],cj)
        return True
#         j=0
#         for i in range(len(nums)):
#             if j<i:
#                 return False
#             j=max(j,i+nums[i])
#         return True
      