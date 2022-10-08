class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        s=[]
        for i in range(len(nums)-n+1):
            for j in range(n,len(nums)):
                s.append(nums[i])
                s.append(nums[j])
                i+=1
            return s
            
        
        