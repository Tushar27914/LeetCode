class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        s=[]
        for i in range(len(accounts)):
            s.append(sum(accounts[i]))
        return max(s)
        