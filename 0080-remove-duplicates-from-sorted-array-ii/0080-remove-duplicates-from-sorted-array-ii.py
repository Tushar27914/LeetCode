class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tail=0
        for num in nums:
            if tail<2 or num!=nums[tail-1] or num!=nums[tail-2]:
                nums[tail]=num
                tail+=1
        return tail
                
        