class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n=len(nums)
        prefix=[0]*n
        prefix[0]=nums[0]
        for i in range(1,len(nums)):
            prefix[i]=nums[i]+prefix[i-1]
        m=float("inf")
        for i in range(n):
            s1=prefix[i]
            a1=s1//(i+1)
            s2=prefix[n-1]-prefix[i]
            if n-i-1!=0:
                a2=s2//(n-i-1)
            else:
                a2=0
            avg=abs(a1-a2)
            if avg<m:
                m=avg
                ans=i
        return ans
        
        