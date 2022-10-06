class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n=len(nums)
        idx=0
        for i in range(len(nums)-1,0,-1):
            if(nums[i]>nums[i-1]):
                j=i
                while(j<n and nums[j]>nums[i-1]):
                    idx=j
                    j+=1
                nums[idx],nums[i-1]=nums[i-1],nums[idx]
                nums[i:]=sorted(nums[i:])
                return 
        return nums.reverse()
        
        
        
        