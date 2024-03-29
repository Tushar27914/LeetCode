#User function Template for python3

class Solution:
    def isSubsetSum (self, N, arr, sum):
        dp={}
        def solver(N,sm):
            if sm==0:
                return 1
            elif N==0:
                return 0
            elif (N,sm) in dp:
                return dp[(N,sm)]
            else:
                item = arr[N-1]
                if item<=sm:
                    c1=solver(N-1,sm-arr[N-1])
                    c2=solver(N-1,sm)
                    c = c1 or c2
                else:
                    c = solver(N-1,sm)
                dp[(N,sm)] = c
                return c
        return solver(N,sum)
        # dp=([[0 for i in range(sum+1)] for x in range(N+1)])
        # for i in range(N+1):
        #     dp[i][0] = 1
        # for j in range(1,sum+1):
        #     dp[0][j] = 0
        # for i in range(1,N+1):
        #     for j in range(1,sum+1):
        #         if arr[i-1]<=j:
        #             dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
        #         else:
        #             dp[i][j] = dp[i-1][j]
        # return dp[N][sum]
                   
        # code here 
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends