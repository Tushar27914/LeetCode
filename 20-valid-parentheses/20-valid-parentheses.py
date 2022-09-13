class Solution:
    def isValid(self, s: str) -> bool:
        start=True
        while start:
            if '()' in s:
                s=s.replace('()','')
            elif '{}' in s:
                s=s.replace('{}','')
            elif '[]' in s:
                s=s.replace('[]','')
            else:
                start=False
        if len(s)==0:
            return True
        return False
        