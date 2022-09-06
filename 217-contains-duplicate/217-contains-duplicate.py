class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                return True
            else:
                d[nums[i]]=1
        return False

            
            
       # stack=nums
#         for i in range(len(nums)):
#             while stack.pop()==nums[i]:
#                 return True
#             return False
            
        