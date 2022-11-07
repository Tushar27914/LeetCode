class Solution:
    def maximum69Number (self, num: int) -> int:
        t=str(num)
        u=list(t)
        for i in range(len(u)):
            if(u[i]=='6'):
                u[i]='9'
                break
        return int("".join(u))
        