#User function Template for python3


class Solution:
    def Countpair (self, arr, n, k):
        s=[]
        for i in range(len(arr)-1):
            for j in range(i,len(arr)):
                if (arr[i]+arr[j])==k and arr[i]!=arr[j]:
                    s.append((arr[i],arr[j]))
        if len(s)>=1:
            return len(s)
        return -1
        # if sum(arr)<k:
        #     return -1
        # d={}
        # for i in range(len(arr)):
        #     if arr[i] in d:
        #         d[arr[i]]+=1
        #     else:
        #         d[arr[i]]=1
        # #print(d)
        # s=[]
        # for i in d:
        #     #print(i)
        #     for j in d:
        #         if i+j==k and i!=j:
        #             s.append((i,j))
        #         i+=1
        # return len(s)
            
            
        




#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    K = int(input())
    res = Solution().Countpair(arr, n, K)
    print(res)



# } Driver Code Ends