# User function Template for Python3

class Solution:
    def equalPartition(self, N, arr):
        def solver(n,arr,s1,s2,dp):
            if n==0:
                return s1==s2
            elif (n,s1,s2) in dp:
                return dp[(n,s1,s2)]
            dp[(n,s1,s2)] = solver(n-1,arr,s1-arr[n-1],s2,dp) or solver(n-1,arr,s1,s2-arr[n-1],dp)
            return dp[(n,s1,s2)]
        sum1=sum(arr)
        if sum1%2!=0:
            return False
        dp={}
        n=len(arr)
        return solver(n,arr,sum1//2,sum1//2,dp)
    #     if sum1%2==0:
    #         print("YES")
    #     if N==0 and sum1!=0:
    #         print("NO")
    #     if arr[N-1]>sum1:
    #         return equalPartition(N-1,arr,sum1)
    #     return self.equalPartition(N-1,arr,sum1) or self.equalPartition(N-1,arr,sum1-arr[N-1])
        
    # def solver(n,arr):
    #     sum1=sum(arr)
    #     if sum1%2!=0:
    #         print("NO")
    #     return self.equalPartition(N,arr,sum1//2)
        # sm=sum(arr)
        # if sm%2!=0:
        #     return "NO"
        # sm1=sm//2
        # def solve(arr,N,sm1):
        #     sm1=sm//2
        #     if sm1==0:
        #         print("YES")
        #     elif N==0 and sm1!=0:
        #         print("NO")
        #     #elif (arr,N,sm1) in dp:
        #      #   return dp[(arr,N,sm1)]
        #     else:
        #         item=arr[N-1]
        #         if item<=sm1:
        #             c1=solve(arr,N-1,sm1-arr[N-1])
        #             c2=solver(arr,N-1,sm1)
        #             return c1 or c2
        #         else:
        #             return solve(arr,N-1,sm1)
        #         #dp[(arr,N,sm1)] = c
        #         #return c
        # return solve(arr,N,sm1)

#{ 
 # Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends