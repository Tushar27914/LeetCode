class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                if abs(d[nums[i]]-i)<=k:
                    return True
                else:
                    d[nums[i]]=i
            else:
                d[nums[i]]=i
        return False
                 
                
            
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if nums[i]-nums[j]==0:
#                     if abs(i-j)<=k:
#                         return True
#                     else:
#                         return False
    
        
        