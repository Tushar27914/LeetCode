#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def insertNewEvent(self, N, intervals, newEvent):
        intervals.append(newEvent)
        stack=[]
        intervals.sort(key=lambda x:x[0])
        stack.append(intervals[0])
        for i in range(1,len(intervals)):
            if(intervals[i][0]<=stack[-1][1]):
                a=stack.pop(-1)
                stack.append([a[0],max(a[1],intervals[i][1])])
            else:
                stack.append(intervals[i])
        return stack
        # Code here

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        intervals = [list(map(int, input().split())) for i in range(N)]
        newEvent = list(map(int, input().split()))
        ob = Solution()
        res = ob.insertNewEvent(N, intervals, newEvent)
        print('[', end = '')
        for i in range(len(res)):
            print('[', end = '')
            print(str(res[i][0])+','+str(res[i][1]), end = '')
            print(']', end = '')
            if i < len(res)-1:
                print(',', end='')
        print(']')
# } Driver Code Ends