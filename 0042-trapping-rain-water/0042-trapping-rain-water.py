class Solution:
    def trap(self, height: List[int]) -> int:
        s=0
        l=0
        r=len(height)-1
        while(l<r):
            i=1
            if(height[l]<height[r]):
                while(height[l]>height[l+i]):
                    s+=height[l]-height[l+i]
                    i+=1
                l+=i
            else:
                while(height[r]>height[r-i]):
                    s+=height[r]-height[r-i]
                    i+=1
                r-=i
        return s
        