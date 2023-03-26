#User function Template for python3

class Solution:
    def findTargetSumWays(self, arr, N, target):
        sum1=sum(arr)
        x=sum1+target
        if x%2!=0:
            return 0
        else:
            x=x//2
        arr.sort(reverse=True)
        dp={}
        def solver(n,sm):
            if n==0:
                if sm==0:
                    return 1
                else:
                    return 0
            elif (n,sm) in dp:
                return dp[(n,sm)]
            else:
                item=arr[n-1]
                if item<=sm:
                    c1=solver(n-1,sm-item)
                    c2=solver(n-1,sm)
                    c=c1+c2
                else:
                    if sm==0:
                        c=1
                    else:
                        c=0
                dp[(n,sm)]=c
                return c
        return solver(N,x)
        
        
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        target = int(input())
        ob = Solution()
        print(ob.findTargetSumWays(arr,N, target))
# } Driver Code Ends