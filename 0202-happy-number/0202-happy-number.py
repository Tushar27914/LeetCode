class Solution:
    def isHappy(self, n: int) -> bool:
        s=set()
        while n not in s:
            s.add(n)
            n=self.sumofdigit(n)
            if n==1:
                return True
        return False
    def sumofdigit(self,n: int)-> int:
        output=0
        while n:
            digit=n%10
            digit=digit**2
            output+=digit
            n=n//10
        return output