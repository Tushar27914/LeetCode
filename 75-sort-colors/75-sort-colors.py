class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i, lt, gt = 0, 0, len(nums)-1
        pivot = 1
        while i <= gt:
            if nums[i] == pivot:
                i = i + 1
            elif nums[i] < pivot:
                nums[lt], nums[i] = nums[i], nums[lt]
                lt,i = lt+1, i+1
            else:
                nums[gt], nums[i] = nums[i], nums[gt]
                gt = gt - 1
        return
        
        """
        Do not return anything, modify nums in-place instead.
        """
        