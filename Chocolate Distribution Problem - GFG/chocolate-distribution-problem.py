#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):
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