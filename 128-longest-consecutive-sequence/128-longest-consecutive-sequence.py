class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)==0):
            return 0
        nums.sort()
        max1=1
        count=1
        for i in range(len(nums)):
            if(nums[i]-nums[i-1]==1):
                count+=1
                max1=max(count,max1)
            elif(nums[i]==nums[i-1]):
                continue
            else:
                count=1
        return max1
         