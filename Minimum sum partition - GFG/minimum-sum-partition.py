#User function Template for python3
class Solution:
	def minDifference(self, arr, n):
	    sum1=sum(arr)
	    dp={}
	    def solver(n,p1,sum1):
	        p2=sum1-p1
	        if n==0:
	            return p1-p2
	        elif (n,p1) in dp:
	            return dp[(n,p1)]
	        else:
	            item=arr[n-1]
	            if p1-item>=p2+item:
	                c1=solver(n-1,p1-item,sum1)
	                c2=solver(n-1,p1,sum1)
	                c=min(c1,c2)
	            else:
	                c=solver(n-1,p1,sum1)
	            dp[(n,p1)] = c
	            return c
	    return solver(n,sum1,sum1)
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends