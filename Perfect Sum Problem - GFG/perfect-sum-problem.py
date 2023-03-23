#User function Template for python3
class Solution:
	def perfectSum(self, arr, n, sum):
	    arr.sort(reverse=True)
	    dp={}
	    mod=10**9+7
	    def solve(n,sm):
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
	                c1=solve(n-1,sm-item)
	                c2=solve(n-1,sm)
	                c=(c1+c2)%mod
	            else:
	                if sm==0:
	                    c=1
	                else:
	                    c=0
	            dp[(n,sm)] = c
	            return c
	    return solve(n,sum)
	   
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends