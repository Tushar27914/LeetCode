class Solution:
    def reverseWords(self, s: str) -> str:
        t=s.split()[::-1]
        return(" ".join(t))
        