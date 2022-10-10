class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        nums.sort()
        g=gcd(*numsDivide)
        for i,n in enumerate(nums):
            if(g%n==0):
                return i
        return -1
            
        