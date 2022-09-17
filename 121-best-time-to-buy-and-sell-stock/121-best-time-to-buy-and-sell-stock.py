class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l=0
        # r=1
        # maxp=0
        # while(r<len(prices)):
        #     if(prices[l]<prices[r]):
                
        minimum=prices[0]
        maxprofit=0
        min1=0
        for i in range(1, len(prices)):
            maxprofit=max(maxprofit,prices[i]-minimum)
            minimum=min(prices[i],minimum)
        return maxprofit