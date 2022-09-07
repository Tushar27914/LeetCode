class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k<1 or t<0:
            return False
        d={}
        for i,n in enumerate(nums):
            bucket=n//(t+1)
            if bucket in d:
                return True
            if bucket-1 in d and abs(n-d[bucket-1])<=t:
                return True
            if bucket+1 in d and abs(n-d[bucket+1])<=t:
                return True
            d[bucket]=n
            if i>=k:
                del d[nums[i-k]//(t+1)]
        return False