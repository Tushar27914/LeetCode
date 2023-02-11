class Solution:
	def overlappedInterval(self, Intervals):
	    #return(type(Intervals))
        stack=[]
        Intervals.sort(key=lambda x:x[0])
        stack.append(Intervals[0])
        for i in range(1,len(Intervals)):
            if(Intervals[i][0]<=stack[-1][1]):
                a=stack.pop(-1)
                stack.append([a[0],max(a[1],Intervals[i][1])])
            else:
                stack.append(Intervals[i])
        return stack
	    
	        
		#Code here


#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	n = int(input())
    	a = list(map(int, input().strip().split()))
    	Intervals = []
    	j = 0
    	for i in range(n):
    		x = a[j]
    		j += 1
    		y = a[j]
    		j += 1
    		Intervals.append([x,y])
    	obj = Solution()
    	ans = obj.overlappedInterval(Intervals)
    	for i in ans:
    		for j in i:
    			print(j, end = " ")
    	print()
# } Driver Code Ends