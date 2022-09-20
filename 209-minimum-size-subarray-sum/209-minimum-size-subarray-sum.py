class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        total=0
        res=float("inf")
        for r in range(len(nums)):
            total+=nums[r]
            while(total>=target):
                res=min(r-l+1,res)
                total-=nums[l]
                l+=1
        if res==float("inf"):
            return 0
        return res
                
                
        
        
        
        
        
#         n=len(nums)
#         sum1=0
#         l=0
#         r=0
#         min1=max(nums)
#         if(sum(nums)<target):
#             return 0
#         while(r<n):
#             sum1+=nums[r]
#             if(sum1>=target):
#                 while(sum1>=target):
#                     sum1-=nums[l]
#                     l+=1
                    
#                 min1=min(min1,r-l+2)
#             r+=1
#         return min1==target
                    
            
        
        
        
        # count=[]
        # for i in range(len(nums)):
        #     nums[i]=nums[i]+nums[i-1]
        # for i in range(len(nums)):
        #     if(nums[-1]-nums[i]==target):
        #         count.append([nums[i],nums[-1]])
        # return len(count)
         
                
        
        # sum1=0
        # s=[]
        # i=nums[0]
        # j=nums[-1]
        # while j<i:
        #     sum1+=nums[i]+nums[j]
        #     if sum1==target:
        #         s.append([i,j])
        #     else:
        #         return 0
        #     if(nums[i]<=nums[j]):
        #         i+=1
        #     else:
        #         j-=1
        # return (s)
   