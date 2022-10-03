class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h1=len(haystack)
        n1=len(needle)
        
        if n1==0:
            return 0
        for i in range(len(haystack)):
            if((i+n1)<=h1 and haystack[i:i+n1]==needle):
                return i
        return -1
        
   