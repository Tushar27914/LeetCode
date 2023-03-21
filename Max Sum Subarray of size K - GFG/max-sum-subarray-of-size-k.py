#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        ans=[]
        windowsum=0
        windowstart=0
        for windowend in range(len(Arr)):
            windowsum+=Arr[windowend]
            if windowend>=K-1:
                ans.append(windowsum)
                windowsum-=Arr[windowstart]
                windowstart+=1
        return max(ans)
        # ans=[]
        # for i in range(N-K+1):
        #     csum=0
        #     for j in range(i,i+K):
        #         csum+=Arr[j]
        #     ans.append(csum)
        # return max(ans)
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends