#User function Template for python3
class Solution:
    def findKRotation(self,arr,  n):
        t=arr.index(min(arr))
        u=arr.index(max(arr))
        return t
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	tc=int(input())
	while tc > 0:
		n=int(input())
		a=list(map(int , input().strip().split()))
		ob = Solution()
		ans=ob.findKRotation(a, n)
		print(ans)
		tc=tc-1



# } Driver Code Ends