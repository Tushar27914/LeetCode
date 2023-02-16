#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
	    def subsetsum(index,sum1,arr,N,subset):
	        if index==N:
	            subset.append(sum1)
	            return
	        subsetsum(index+1,sum1+arr[index],arr,N,subset)
	        subsetsum(index+1,sum1,arr,N,subset)
	    subset=[]
	    subsetsum(0,0,arr,N,subset)
	    return(sorted(subset))
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
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends