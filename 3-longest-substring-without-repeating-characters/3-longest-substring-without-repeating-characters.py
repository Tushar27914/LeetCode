class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        start=0
        d=set()
        m=0
        while(i<len(s)):
            while s[i] in d:
                d.remove(s[start])
                start+=1
            d.add(s[i])
            m=max(m,len(d))
            i+=1
        return m
            
            
            
            
        