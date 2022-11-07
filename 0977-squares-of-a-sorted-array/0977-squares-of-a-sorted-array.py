class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
       # nums.sort()
        s=[]
        for i in range(len(nums)):
            s.append(nums[i]**2)
        s.sort()
        return s
        