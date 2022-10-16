class Solution:
    
    def jump(self, nums: List[int]) -> int:
        currentreach=0
        currentmax=0
        jump=0
        for i in range(len(nums)-1):
            if(i+nums[i]>currentmax):
                currentmax=i+nums[i]
            if(i==currentreach):
                jump+=1
                currentreach=currentmax
        return jump
