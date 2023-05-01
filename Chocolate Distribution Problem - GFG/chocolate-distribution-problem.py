#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):
        # ans=[]
        # A.sort()
        # ws=0
        # res=[]
        # for we in range(N):
        #     ans.append(A[we])
        #     if we>=M-1:
        #         res.append(max(ans)-min(ans))
        #         ans.remove(A[ws])
        #         ws+=1
        # return min(res)
        
        
        # ans=[]
        # A.sort()
        # for i in range(N-M+1):
        #     t=[]
        #     for j in range(i,i+M):
        #         t.append(A[j])
        #     u=max(t)-min(t)
        #     ans.append(u)
        # return min(ans)
        i=0
        j=M-1
        d=max(A)
        A.sort()
        while j<N:
            d=min(d,A[j]-A[i])
            i+=1
            j+=1
        return(d)
        
            

        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends