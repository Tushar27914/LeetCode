class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max1=nums[0]
        sum1=0
        for i in range(len(nums)):
            sum1+=nums[i]
            if(sum1>max1):
                max1=sum1
            if(sum1<0):
                sum1=0
        return max1