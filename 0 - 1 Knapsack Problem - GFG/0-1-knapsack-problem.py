#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        def solver(val,wt,w,n,dp):
            if dp[w][n]!=-1:
                return dp[w][n]
            if w==0 or n==0:
                dp[w][n] = 0
            elif w>=wt[n-1]:
                dp[w][n] = max(val[n-1] + solver(val,wt,w-wt[n-1],n-1,dp),solver(val,wt,w,n-1,dp))
            else:
                dp[w][n] = solver(val,wt,w,n-1,dp)
            return dp[w][n]
        
        dp = [[-1]*(n+1) for _ in range(W+1)]
        
        return solver(val,wt,W,n,dp)
            
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends