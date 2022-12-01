class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        str(s)
        t=list(s)
        mid=len(t)//2
        q=t[:mid]
        w=t[mid:]
        c1=0
        c2=0
        for i in q:
            if i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='u' or i=='U':
                c1+=1
        for j in w:
            if j=='a' or j=='A' or j=='e' or j=='E' or j=='i' or j=='I' or j=='o' or j=='O' or j=='u' or j=='U':
                c2+=1
        if c1==c2:
            return True
        else:
            return False
            
        
        